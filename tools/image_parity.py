#!/usr/bin/env python3
"""Read-only NL/EN image parity audit for the live Hugo blog."""
import hashlib, os, re, sys, glob
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

BASE = "https://enterpriseagileblogs.github.io/"
REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(REPO, "screenshots", "image-parity-report.md")
S = requests.Session()
_hash = {}
VARIANT = re.compile(r"(zwart|black|dark|styli[sz]ed|noir|-v\d+)", re.I)

def get(url):
    r = S.get(url, timeout=30); return r

def img_hash(url):
    if url not in _hash:
        try:
            r = get(url)
            _hash[url] = (r.status_code, hashlib.sha1(r.content).hexdigest()[:10] if r.ok else None)
        except Exception as e:
            _hash[url] = (str(e), None)
    return _hash[url]

def path(u): return urlparse(u).path

def overview(lang):
    cards, url, seen = {}, urljoin(BASE, f"/{lang}/blog/"), set()
    while url and url not in seen:
        seen.add(url)
        soup = BeautifulSoup(get(url).text, "html.parser")
        for c in soup.select("article.card"):
            a = c.select_one("h3 a") or c.find("a")
            img = c.find("img")
            u = urljoin(url, a["href"])
            cards[u] = {"title": a.get_text(strip=True),
                        "card": urljoin(url, img["src"]) if img and img.get("src") else None}
        nxt = soup.select_one('a[rel=next], .pagination a.next, a.next')
        url = urljoin(url, nxt["href"]) if nxt else None
    return cards

def post(url):
    r = get(url); soup = BeautifulSoup(r.text, "html.parser")
    content = soup.select_one("div.content") or soup.select_one("article") or soup
    imgs = [urljoin(url, i["src"]) for i in content.find_all("img") if i.get("src")]
    og = soup.find("meta", property="og:image")
    alt = {}
    for l in soup.find_all("link", rel="alternate", hreflang=True):
        alt[l["hreflang"]] = urljoin(url, l["href"])
    for a in soup.find_all("a", hreflang=True):
        alt.setdefault(a["hreflang"], urljoin(url, a["href"]))
    return {"status": r.status_code, "imgs": imgs, "og": og["content"] if og else None, "alt": alt}

def key(u):  # identity of an image: content hash, fallback path
    st, h = img_hash(u); return h or ("BROKEN:" + path(u))

def ekey(u):  # EN '-en' translated figure counts as equal to its NL base
    b = re.sub(r"-en(\.\w+)$", r"\1", u)
    return key(b) if b != u else key(u)

def main():
    nl, en = overview("nl"), overview("en")
    for lang, cards in (("nl", nl), ("en", en)):
        for u, c in cards.items(): c.update(post(u))
    pairs, used_en = [], set()
    for u, c in nl.items():
        e = c["alt"].get("en")
        if e and e.rstrip("/") + "/" in en: e = e.rstrip("/") + "/"
        pairs.append((u, e if e in en else None)); used_en.add(e)
    orphans_en = [u for u in en if u not in used_en]
    static = [os.path.relpath(p, os.path.join(REPO, "static")) for p in glob.glob(os.path.join(REPO, "static", "**", "*.*"), recursive=True)]
    static += [os.path.relpath(p, REPO) for p in glob.glob(os.path.join(REPO, "assets", "**", "*.*"), recursive=True) if not p.endswith((".css", ".js"))]
    variants = [p for p in static if VARIANT.search(os.path.basename(p))]
    rows, details, broken, info = [], [], [], []
    def chk(lang, title, where, u):
        st, _ = img_hash(u)
        if st != 200: broken.append(f"- {lang} **{title}** – {where}: `{u}` → {st}")
    for nu, eu in pairs:
        n = nl[nu]; e = en.get(eu)
        if n["card"]: chk("NL", n["title"], "card", n["card"])
        for i in n["imgs"]: chk("NL", n["title"], "body", i)
        if not e:
            rows.append((n["title"], "—", "NOT OK", "no EN translation")); continue
        if e["card"]: chk("EN", e["title"], "card", e["card"])
        for i in e["imgs"]: chk("EN", e["title"], "body", i)
        diffs = []
        if (key(n["card"]) if n["card"] else None) != (ekey(e["card"]) if e["card"] else None):
            diffs.append(f"Card image differs: NL `{n['card']}` vs EN `{e['card']}`")
        kn, ke = [key(i) for i in n["imgs"]], [ekey(i) for i in e["imgs"]]
        if kn != ke:
            if len(kn) != len(ke): diffs.append(f"Body image count differs: NL {len(kn)} vs EN {len(ke)}")
            for idx in range(max(len(kn), len(ke))):
                a = n["imgs"][idx] if idx < len(kn) else None; b = e["imgs"][idx] if idx < len(ke) else None
                if (kn[idx] if a else None) != (ke[idx] if b else None):
                    diffs.append(f"Body image #{idx+1}: NL `{a and path(a)}` vs EN `{b and path(b)}`")
            if sorted(kn) == sorted(ke): diffs.append("(same set of images, different order)")
        on, oe = n["og"], e["og"]
        if (on and oe and key(on) != key(oe)): diffs.append(f"og:image differs: NL `{path(on)}` vs EN `{path(oe)}`")
        # black/stylized variant check
        used = {path(x) for x in [n["card"], e["card"], *n["imgs"], *e["imgs"]] if x}
        stems = {re.sub(r"\.\w+$", "", os.path.basename(p)) for p in used}
        for v in variants:
            vb = re.sub(r"(-v\d+)?\.\w+$", "", os.path.basename(v))
            base = VARIANT.sub("", re.sub(r"\.\w+$", "", os.path.basename(v))).strip("-_")
            if any(s.startswith(base) or base.startswith(s) for s in stems if len(s) > 3):
                inn = any(path(x).endswith(os.path.basename(v)) for x in [n["card"], *n["imgs"]] if x)
                ine = any(path(x).endswith(os.path.basename(v)) for x in [e["card"], *e["imgs"]] if x)
                if inn != ine:
                    diffs.append(f"Variant `/{v}` used only in {'NL' if inn else 'EN'}")
                elif not inn:
                    info.append(f"- **{n['title']}**: variant file `/{v}` exists but is used in neither language")
        for lang, c in (("NL", n), ("EN", e)):
            if c["card"] and c["imgs"] and key(c["card"]) != key(c["imgs"][0]):
                info.append(f"- {lang} **{c['title']}**: card `{path(c['card'])}` ≠ first body image `{path(c['imgs'][0])}`")
        rows.append((n["title"], e["title"], "OK" if not diffs else "NOT OK", ""))
        if diffs: details.append((n["title"], e["title"], nu, eu, diffs))
    nl_md = len(glob.glob(os.path.join(REPO, "content/nl/blog/[!_]*.md")))
    en_md = len(glob.glob(os.path.join(REPO, "content/en/blog/[!_]*.md")))
    lm = get(BASE).headers.get("Last-Modified", "n/a")
    L = ["# NL/EN image parity report", "", f"Site: {BASE}  ", f"Live Last-Modified header: {lm}  ",
         f"Live cards: NL {len(nl)}, EN {len(en)}; content/ md files: NL {nl_md}, EN {en_md}  ",
         f"Pairs checked: {len(pairs)}; OK: {sum(r[2]=='OK' for r in rows)}; unpaired EN: {len(orphans_en)}", "",
         "| # | NL title | EN title | Result |", "|---|---|---|---|"]
    for i, r in enumerate(rows, 1): L.append(f"| {i} | {r[0]} | {r[1]} | {r[2]}{(' – '+r[3]) if r[3] else ''} |")
    L += ["", "## Differences"] + (["None."] if not details else [])
    for nt, et, nu, eu, d in details:
        L += ["", f"### {nt} / {et}", f"NL: {nu}  ", f"EN: {eu}", ""] + [f"- {x}" for x in d]
    L += ["", "## Unpaired EN posts"] + ([f"- {en[u]['title']} {u}" for u in orphans_en] or ["None."])
    L += ["", "## Broken images (non-200)"] + (broken or ["None."])
    L += ["", "## Black/stylized variant files in static/assets"] + ([f"- `/{v}`" for v in variants] or ["None found."])
    L += ["", "## Info (not failures)"] + (info or ["None."])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w").write("\n".join(L) + "\n")
    print("\n".join(L))

if __name__ == "__main__":
    main()
