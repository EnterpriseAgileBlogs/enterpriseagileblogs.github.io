#!/usr/bin/env python3
"""Rebuild verschillen-besturing-en.png: same table style as the NL original (Word table, Calibri)."""
import os
from PIL import Image, ImageDraw, ImageFont
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'images', 'blog')
FD = '/usr/share/fonts/truetype/sand-box/google/Carlito/Carlito-%s.ttf'
W, COL, PAD, SIZE, PITCH = 945, 473, 14, 23, 28.5
BLUE, LIGHT, LINE = (68, 114, 196, 255), (217, 226, 243, 255), (142, 170, 219, 255)
HEAD = ("Classic governance for non-agile organizations (chains)", "Lean-Agile governance for agile organizations (chains)")
ROWS = [
 ("Annual plans", "Quarterly plans with rolling forecast"),
 ("Annual budgets per department", "Quarterly budgets for value streams"),
 ("Steering on costs", "Steering on value creation and quality"),
 ("Costs and spending per project", "Fixed costs for a value stream (product / service)"),
 ("Risks known upfront on paper", "Risks identified and eliminated in the work"),
 ("Distrust and control of finances", "Trust and participation in the quality chain"),
 ("Contracts and SLAs on content", "Partnerships with agreements on process (agile contracting), and delegation of responsibilities"),
 ("Year-end accountability for achieving annual plan goals / reports", "Regular review within the organization in the chain of how value is created"),
 ("Thinking in efficiency", "Thinking in effectiveness"),
 ("Thinking in departments and department plans", "Thinking in products and product vision"),
 ("Thinking everything is feasible as long as there is budget", "Thinking in prioritization of work based on value"),
 ("Fixed-price assignments to mitigate financial risk", "Partnerships and hiring of multidisciplinary teams on a ‘time & material’ basis"),
 ("Business and IT are separated, not ‘Digital’ minded", "Business and IT no longer exist separately; merged into multidisciplinary teams and teams of teams, ‘Digital’ mindset"),
 ("Illusion of certainty in plans", "Rolling forecasts with increasing uncertainty margins (cone of uncertainty)"),
 ("Business strategy translated into department strategy", "Business strategy translated into product or service strategy and vision (agile strategy)"),
 ("Employees are brought ‘to the work’ (temporary project teams)", "Work is brought to stable multidisciplinary product teams"),
 ("Scope is fixed, costs and lead times are variable", "Costs and lead times are fixed, scope is variable"),
 ("Management decides everything", "Management delegates as much as possible"),
 ("Management steers on results and costs", "Management develops the organization so that it achieves the results and keeps working more effectively, reducing costs as a result"),
 ("Staff departments are islands with their own goals", "Staff departments are integrated into multidisciplinary teams focused on the company’s products and services"),
 ("Fixed mindset", "Growth mindset"),
]
def wrap(t, f, maxw):
    out, cur = [], ''
    for w in t.split():
        c = (cur + ' ' + w).strip()
        if f.getlength(c) <= maxw: cur = c
        else: out.append(cur); cur = w
    return out + [cur]
fr, fb = ImageFont.truetype(FD % 'Regular', SIZE), ImageFont.truetype(FD % 'Bold', SIZE)
maxw = COL - 2 * PAD
def rowlines(r, f): return [wrap(r[0], f, maxw), wrap(r[1], f, maxw)]
rows = [(HEAD, fb, BLUE, (255, 255, 255, 255))] + [(r, fr, LIGHT if i % 2 == 0 else (0, 0, 0, 0), (0, 0, 0, 255)) for i, r in enumerate(ROWS)]
H = 0; layout = []
for r, f, bg, fg in rows:
    ls = rowlines(r, f); n = max(len(l) for l in ls); h = round(n * PITCH)
    layout.append((H, h, ls, f, bg, fg)); H += h + 1
img = Image.new('RGBA', (W, H + 1), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
for y, h, ls, f, bg, fg in layout:
    d.rectangle([0, y, W - 1, y + h], fill=bg)
    for c, lines in enumerate(ls):
        x = (PAD if c == 0 else COL + PAD)
        for k, t in enumerate(lines):
            d.text((x, y + 3 + k * PITCH), t, font=f, fill=fg)
    d.line([0, y + h + 1 if False else y + h, W - 1, y + h], fill=LINE)
for x in (0, COL, W - 1): d.line([x, layout[1][0], x, H], fill=LINE)
d.line([0, H, W - 1, H], fill=LINE)
for y, h, ls, f, bg, fg in layout:
    for c, lines in enumerate(ls):
        for t in lines: assert f.getlength(t) <= maxw, t
out = os.path.join(D, 'verschillen-besturing-en.png'); img.save(out); print(out, img.size)
