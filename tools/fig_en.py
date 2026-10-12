#!/usr/bin/env python3
"""Make English versions of figures with Dutch text (originals untouched).

Usage: fig_en.py SPEC.json [SPEC.json ...]
Spec: {"src": "Trend-zonder.png", "items": [ {...}, ... ]}
Item keys:
  nl     Dutch phrase to find via OCR (fuzzy, reading order, may span lines)
  en     English text (str) or list of lines
  word   true -> replace every single-word match of nl individually
  align  "c" (default) or "l"
  rot    0/90/270: orientation in which the text reads horizontally
  box    [x,y,w,h] manual box (skips OCR); in rotated coordinates if rot
  size / bold / color   overrides
  all    false -> only first occurrence
Output: <src stem>-en.png next to the source. Log lists misses/overflows.
"""
import json, sys, os, subprocess, csv, io, difflib, re
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

FONT = '/usr/share/fonts/truetype/sand-box/google/Carlito/Carlito-%s.ttf'
IMGDIR = os.path.join(os.path.dirname(__file__), '..', 'static', 'images', 'blog')
MARGIN = 8

def font(sz, bold):
    return ImageFont.truetype(FONT % ('Bold' if bold else 'Regular'), max(5, int(round(sz))))

def norm(s):
    return re.sub(r'[^a-z0-9àáäëéèïöüç/&€+-]', '', s.lower())

def ocr_words(im, key=None):
    import pickle, hashlib
    cache = None
    if key:
        os.makedirs('/tmp/figocr', exist_ok=True)
        cache = '/tmp/figocr/' + hashlib.md5(key.encode()).hexdigest()
        if os.path.exists(cache):
            return pickle.load(open(cache, 'rb'))
    words = []
    for S in ((3,) if im.width * im.height > 400000 else (3, 4)):
        big = im.resize((im.width * S, im.height * S), Image.LANCZOS)
        tmp = '/tmp/_fig_ocr_%d.png' % os.getpid()
        big.save(tmp)
        for psm in ('11', '6', '3'):
            out = subprocess.run(['tesseract', tmp, '-', '-l', 'nld+eng', '--psm', psm, 'tsv'],
                                 capture_output=True, text=True).stdout
            for r in csv.DictReader(io.StringIO(out), delimiter='\t', quoting=csv.QUOTE_NONE):
                if r['level'] != '5' or not (r['text'] or '').strip():
                    continue
                x, y, w, h = [int(r[a]) / S for a in ('left', 'top', 'width', 'height')]
                t = r['text'].strip()
                if not norm(t):
                    continue
                cand = dict(t=t, n=norm(t), x0=x, y0=y, x1=x + w, y1=y + h, c=float(r['conf']))
                dup = False
                for o in words:
                    ix = max(0, min(o['x1'], cand['x1']) - max(o['x0'], cand['x0']))
                    iy = max(0, min(o['y1'], cand['y1']) - max(o['y0'], cand['y0']))
                    a = (cand['x1'] - cand['x0']) * (cand['y1'] - cand['y0'])
                    if a and ix * iy / a > 0.5:
                        if cand['c'] > o['c'] and len(cand['n']) >= len(o['n']):
                            o.update(cand)
                        dup = True
                        break
                if not dup:
                    words.append(cand)
    # reading order: cluster into lines
    words.sort(key=lambda w: (w['y0'] + w['y1']) / 2)
    lines = []
    for w in words:
        cy = (w['y0'] + w['y1']) / 2
        for L in lines:
            if abs(L['cy'] - cy) < max(3, 0.45 * (w['y1'] - w['y0'])):
                L['w'].append(w); break
        else:
            lines.append(dict(cy=cy, w=[w]))
    order = []
    for li, L in enumerate(sorted(lines, key=lambda L: L['cy'])):
        for w in sorted(L['w'], key=lambda w: w['x0']):
            w['line'] = li; order.append(w)
    if cache:
        pickle.dump(order, open(cache, 'wb'))
    return order

def sim(a, b):
    if not a or not b:
        return 0
    return difflib.SequenceMatcher(None, a, b).ratio()

def find(order, phrase, used, all_occ=True, word=False):
    toks = [norm(t) for t in phrase.split() if norm(t)]
    def ok(w, t):
        return sim(w['n'], t) >= (0.75 if len(t) > 3 else 0.99)
    hits = []
    if word:
        for i, w in enumerate(order):
            if i not in used and sim(w['n'], toks[0]) >= (0.8 if len(toks[0]) > 3 else 1.0):
                hits.append([i]); used.add(i)
                if not all_occ: break
        return hits
    def nexts(gidx, prev):
        p = order[prev]; h = max(4, p['y1'] - p['y0'])
        gx0 = min(order[i]['x0'] for i in gidx); gx1 = max(order[i]['x1'] for i in gidx)
        for j, w in enumerate(order):
            if j in used or j in gidx: continue
            same = abs((w['y0'] + w['y1']) / 2 - (p['y0'] + p['y1']) / 2) < 0.5 * h and 0 <= w['x0'] - p['x1'] + 2 < 2.2 * h
            below = 0 <= w['y0'] - p['y1'] + 3 < 1.6 * h and (w['x0'] + w['x1']) / 2 > gx0 - 3 * h and (w['x0'] + w['x1']) / 2 < gx1 + 3 * h
            if same or below:
                yield j
    def extend(gidx, k, miss):
        if k == len(toks):
            return gidx
        best = None
        for j in nexts(gidx, gidx[-1]):
            w = order[j]
            if k + 1 < len(toks) and len(w['n']) >= len(toks[k] + toks[k + 1]) and sim(w['n'], toks[k] + toks[k + 1]) >= 0.85:
                r = extend(gidx + [j], k + 2, miss)
                if r: return r
            if ok(w, toks[k]):
                r = extend(gidx + [j], k + 1, miss)
                if r: return r
            elif miss < len(toks) // 3 and len(toks[k]) > 3 and sim(w['n'], toks[k]) >= 0.4:
                best = best or (j, miss + 1)
        if best:
            return extend(gidx + [best[0]], k + 1, best[1])
        return None
    for i, w in enumerate(order):
        if i in used: continue
        r = None
        if len(toks) > 1 and len(w['n']) >= len(toks[0] + toks[1]) and sim(w['n'], toks[0] + toks[1]) >= 0.85:
            r = extend([i], 2, 0)
        if not r and ok(w, toks[0]):
            r = extend([i], 1, 0)
        if r:
            hits.append(r); used.update(r)
            if not all_occ: break
    return hits

def bg_color(arr, x0, y0, x1, y1):
    H, W = arr.shape[:2]
    p = 3
    X0, Y0, X1, Y1 = max(0, int(x0) - p), max(0, int(y0) - p), min(W, int(x1) + p + 1), min(H, int(y1) + p + 1)
    ring = np.concatenate([arr[Y0:Y0 + 2, X0:X1].reshape(-1, 3), arr[Y1 - 2:Y1, X0:X1].reshape(-1, 3),
                           arr[Y0:Y1, X0:X0 + 2].reshape(-1, 3), arr[Y0:Y1, X1 - 2:X1].reshape(-1, 3)])
    vals, cnt = np.unique(ring, axis=0, return_counts=True)
    return tuple(int(v) for v in vals[cnt.argmax()])

def fg_color(arr, box, bg):
    x0, y0, x1, y1 = [int(round(v)) for v in box]
    reg = arr[max(0, y0):y1 + 1, max(0, x0):x1 + 1].reshape(-1, 3).astype(int)
    d = np.abs(reg - np.array(bg)).sum(1)
    if d.max() < 60:
        return (0, 0, 0)
    top = reg[d >= np.percentile(d, 92)]
    return tuple(int(v) for v in np.median(top, 0))

def est_size(text, h, bold):
    f = font(100, bold)
    bb = f.getbbox(text or 'Hg')
    rh = bb[3] - bb[1]
    return max(6, h * 100 / max(1, rh))

def ink_metrics(arr, box, bg):
    x0, y0, x1, y1 = [int(round(v)) for v in box]
    reg = arr[max(0, y0):y1 + 1, max(0, x0):x1 + 1].astype(int)
    ink = (np.abs(reg - np.array(bg)).sum(2) > 150).astype(np.uint8)
    if ink.sum() < 5:
        return None, None
    rows = ink.sum(1).astype(float)
    band = (rows > 0.45 * rows.max()).sum()
    xh = max(2, band)
    edges = cv2.morphologyEx(ink, cv2.MORPH_GRADIENT, np.ones((2, 2), np.uint8)).sum()
    sw = 2 * ink.sum() / max(1, edges) * 1.0
    return xh, sw

def is_bold(arr, box, bg, size, text):
    x0, y0, x1, y1 = [int(round(v)) for v in box]
    reg = arr[max(0, y0):y1 + 1, max(0, x0):x1 + 1].reshape(-1, 3).astype(int)
    ink = (np.abs(reg - np.array(bg)).sum(1) > 120).mean()
    res = {}
    for b in (False, True):
        f = font(size, b); bb = f.getbbox(text)
        im = Image.new('L', (bb[2] + 4, bb[3] + 4), 0); ImageDraw.Draw(im).text((2 - bb[0], 2 - bb[1]), text, font=f, fill=255)
        a = np.array(im); a = a[2:2 + bb[3] - bb[1], 2:2 + bb[2] - bb[0]]
        res[b] = (a > 128).mean() if a.size else 0
    return abs(res[True] - ink) < abs(res[False] - ink)

def space_w(f):
    return max(f.getlength(' '), 0.30 * f.size)

def tlen(d, t, f):
    ws = t.split(' ')
    return sum(f.getlength(w) for w in ws) + space_w(f) * (len(ws) - 1)

def draw_spaced(d, x, y, t, f, fill):
    if f.size >= 14:
        for w in t.split(' '):
            d.text((x, y), w, font=f, fill=fill); x += f.getlength(w) + space_w(f)
        return
    # small text: render 4x and downsample so glyph spacing is not hinted/rounded per glyph
    S_ = 4
    F = ImageFont.truetype(f.path, f.size * S_)
    words = t.split(' ')
    sp = max(F.getlength(' '), 0.30 * F.size)
    width = int(sum(F.getlength(w) for w in words) + sp * (len(words) - 1)) + 8 * S_
    height = int(F.size * 1.6) + 4 * S_
    lay = Image.new('L', (width, height), 0); ld = ImageDraw.Draw(lay)
    cx = 2 * S_
    for w in words:
        ld.text((cx, 2 * S_), w, font=F, fill=255); cx += F.getlength(w) + sp
    ox, oy = x - 2, y - 2
    fx, fy = ox - int(ox), oy - int(oy)
    lay = lay.transform(lay.size, Image.AFFINE, (1, 0, -fx * S_, 0, 1, -fy * S_), resample=Image.BILINEAR)
    small = lay.resize((width // S_, height // S_), Image.LANCZOS)
    img = d._image
    solid = Image.new(img.mode, small.size, tuple(fill))
    img.paste(solid, (int(ox), int(oy)), small)

def wrap(text, n, f, d):
    words = text.split()
    if n <= 1 or len(words) < 2:
        return [text]
    best = None
    import itertools
    for cuts in itertools.combinations(range(1, len(words)), min(n - 1, len(words) - 1)):
        parts = [' '.join(words[a:b]) for a, b in zip((0,) + cuts, cuts + (len(words),))]
        m = max(tlen(d, p, f) for p in parts)
        if best is None or m < best[0]:
            best = (m, parts)
    return best[1]

def process(spec_path, log):
    spec = json.load(open(spec_path))
    src = os.path.join(IMGDIR, spec['src'])
    stem, ext = os.path.splitext(spec['src'])
    dst = os.path.join(IMGDIR, stem + '-en.png')
    base = Image.open(src).convert('RGB')
    items = spec['items']
    for rot in sorted(set(it.get('rot', 0) for it in items)):
        im = base.rotate(rot, expand=True) if rot else base
        its = [it for it in items if it.get('rot', 0) == rot]
        order = ocr_words(im, spec['src'] + str(rot)) if any('box' not in it for it in its) else []
        used = set()
        plans = []
        for it in sorted(its, key=lambda it: -len(it['nl'].split()) if 'nl' in it else 0):
            if 'tmpl' in it:
                x, y, w, h = it['tmpl']
                g8 = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
                res = cv2.matchTemplate(g8, g8[y:y + h, x:x + w], cv2.TM_CCOEFF_NORMED)
                pts = sorted(zip(*np.where(res >= it.get('thr', 0.8))), key=lambda p: -res[p])
                groups, taken = [], []
                for (py, px) in pts:
                    if any(abs(px - a) < w * 0.6 and abs(py - b) < h * 0.6 for a, b in taken): continue
                    taken.append((px, py)); groups.append([dict(x0=px, y0=py, x1=px + w, y1=py + h, t=it.get('nl', 'Hg'))])
                if not groups: log.append(f"{spec['src']}: TEMPLATE LEEG {it['tmpl']}")
            elif 'box' in it:
                boxes = it['box'] if isinstance(it['box'][0], list) else [it['box']]
                groups = [[dict(x0=x, y0=y, x1=x + w, y1=y + h, t=it.get('nl', 'Hg'))] for x, y, w, h in boxes]
            else:
                hits = find(order, it['nl'], used, it.get('all', True), it.get('word', False))
                if not hits:
                    log.append(f"{spec['src']}: NIET GEVONDEN '{it['nl']}'"); continue
                groups = [[order[i] for i in h] for h in hits]
            for g in groups:
                if 'bgnear' in it:
                    a_ = np.array(im)
                    bgc = bg_color(a_, min(w['x0'] for w in g), min(w['y0'] for w in g), max(w['x1'] for w in g), max(w['y1'] for w in g))
                    if np.abs(np.array(bgc, int) - np.array(it['bgnear'])).sum() > 90:
                        continue
                plans.append((it, g))
        arr = np.array(im)
        # erase all first
        mask = np.zeros(arr.shape[:2], np.uint8)
        meta = []
        for it, g in plans:
            lines = {}
            for w in g:
                lines.setdefault(w.get('line', 0), []).append(w)
            lboxes = []
            for li in sorted(lines):
                ws = lines[li]
                lboxes.append([min(w['x0'] for w in ws), min(w['y0'] for w in ws), max(w['x1'] for w in ws), max(w['y1'] for w in ws),
                               ' '.join(w['t'] for w in ws)])
            info = []
            for b in lboxes:
                bg = bg_color(arr, *b[:4])
                fg = tuple(it['color']) if 'color' in it else fg_color(arr, b[:4], bg)
                info.append((b, bg, fg))
                x0, y0, x1, y1 = [int(round(v)) for v in b[:4]]
                p = it.get('pad', 2)
                reg = arr[max(0, y0 - p):y1 + p + 1, max(0, x0 - p):x1 + p + 1].astype(int)
                if it.get('maskfg'):
                    m = (np.abs(reg - np.array(fg)).sum(2) < it.get('maskthr', 200)).astype(np.uint8) * 255
                else:
                    m = (np.abs(reg - np.array(bg)).sum(2) > 40).astype(np.uint8) * 255
                mask[max(0, y0 - p):y1 + p + 1, max(0, x0 - p):x1 + p + 1] |= m
            meta.append((it, lboxes, info))
        mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)
        # flat fill where background is uniform, inpaint elsewhere
        out = cv2.inpaint(arr, mask, 3, cv2.INPAINT_TELEA)
        for it, lboxes, info in meta:
            for b, bg, fg in info:
                x0, y0, x1, y1 = [int(round(v)) for v in b[:4]]
                p = it.get('pad', 2) + 1
                sub = mask[max(0, y0 - p):y1 + p + 1, max(0, x0 - p):x1 + p + 1] > 0
                region = out[max(0, y0 - p):y1 + p + 1, max(0, x0 - p):x1 + p + 1]
                ring_std = 0
                if it.get('flat', True) == 'row':
                    # row-wise median of the non-text pixels (vertical gradients)
                    Y0, X0 = max(0, y0 - p), max(0, x0 - p)
                    for r_ in range(region.shape[0]):
                        keep = ~sub[r_]
                        if keep.sum() >= 2:
                            region[r_][sub[r_]] = np.median(arr[Y0 + r_, X0:X0 + region.shape[1]][keep], axis=0).astype(np.uint8)
                elif it.get('flat', True):
                    region[sub] = bg
        pil = Image.fromarray(out)
        d = ImageDraw.Draw(pil)
        W = pil.width
        for it, lboxes, info in meta:
            b0, bg0, fg0 = info[0]
            hs = sorted(b[3] - b[1] for b in lboxes)
            h = hs[len(hs) // 2]
            sample = max(lboxes, key=lambda b: b[2] - b[0])[4]
            xh, sw = ink_metrics(np.array(im), b0[:4], bg0)
            bold = it.get('bold', None)
            if bold is None:
                bold = spec.get('bold', False)
            size = it.get('size')
            if not size and (('box' not in it and 'tmpl' not in it) or it.get('fit')):
                # Carlito shares Calibri metrics: fit the NL ink width of the widest line
                wl = max(lboxes, key=lambda b: b[2] - b[0])
                ref = tlen(d, wl[4], font(100, bold))
                if ref > 0:
                    size = 100 * (wl[2] - wl[0]) / ref
                    xs = xh / 0.45 if xh and xh >= 3 else None
                    if xs and not (0.6 * xs <= size <= 1.4 * xs):
                        size = xs
            if not size:
                size = xh / 0.45 if xh and xh >= 3 else est_size(sample, h, False)
            if os.environ.get('FIGDBG'): print('DBG', it.get('nl','')[:30], 'h', round(h,1), 'size', round(size,1), 'sw', sw and round(sw,2), 'xh', xh, 'box', [round(v) for v in b0[:4]])
            f = font(size, bold)
            en = it['en']
            nlines = len(lboxes)
            parts = en if isinstance(en, list) else wrap(en, nlines, f, d)
            gx0 = min(b[0] for b in lboxes); gx1 = max(b[2] for b in lboxes)
            gy0 = min(b[1] for b in lboxes); gy1 = max(b[3] for b in lboxes)
            pitch = it.get('pitch') or ((lboxes[-1][1] - lboxes[0][1]) / (nlines - 1) if nlines > 1 else size * 1.2)
            align = it.get('align', 'c')
            def width_ok(ps):
                for p_ in ps:
                    tw = tlen(d, p_, f)
                    x = max(gx0, MARGIN) if align == 'l' else (gx0 + gx1) / 2 - tw / 2
                    if x < MARGIN or x + tw > W - MARGIN:
                        return False
                return True
            if not isinstance(en, list) and not width_ok(parts):
                for n in range(len(parts) + 1, 4):
                    parts = wrap(en, n, f, d)
                    if width_ok(parts): break
            if not width_ok(parts):
                log.append(f"{spec['src']}: TE BREED '{en}'")
            n = len(parts)
            cy = (gy0 + gy1) / 2
            asc = f.getbbox('Hg')
            for k, p_ in enumerate(parts):
                tw = tlen(d, p_, f)
                x = gx0 if align == 'l' else (gx0 + gx1) / 2 - tw / 2
                x = min(max(x, MARGIN), W - MARGIN - tw)
                ly = cy + (k - (n - 1) / 2) * pitch
                draw_spaced(d, x, ly - (asc[1] + asc[3]) / 2, p_, f, fg0)
        # spec-level redraw blocks (only on the unrotated pass)
        if not rot:
            a2 = np.array(pil)
            for blk in spec.get('draw', []):
                x, y, w, h = blk['erase']
                bg = bg_color(np.array(im), x, y, x + w, y + h)
                a2[y:y + h, x:x + w] = bg
            pil = Image.fromarray(a2); d = ImageDraw.Draw(pil)
            for blk in spec.get('draw', []):
                for (tx, tyc, txt, tsz, tb, tcol) in blk['texts']:
                    f = font(tsz, tb); asc = f.getbbox('Hg')
                    draw_spaced(d, tx, tyc - (asc[1] + asc[3]) / 2, txt, f, tuple(tcol))
        res = pil
        if rot:
            res = res.rotate(-rot, expand=True)
        base = res
    base.save(dst)
    return dst

if __name__ == '__main__':
    log = []
    for s in sys.argv[1:]:
        print('ok', process(s, log))
    print('\n'.join(log) if log else 'geen meldingen')
