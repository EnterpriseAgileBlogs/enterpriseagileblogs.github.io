"""Rebuild silo5-en.png: paste the EN team circles (team1/2/4-en) over the zoomed circles in silo5-en."""
import numpy as np, cv2, sys
from PIL import Image, ImageDraw
B = sys.argv[1] if len(sys.argv) > 1 else 'static/images/blog/'
base = Image.open(B + 'silo5-en.png').convert('RGB'); arr = np.array(base).astype(int)
for team in ['team1', 'team2', 'team4']:
    src = Image.open(B + team + '.png').convert('RGB'); en = Image.open(B + team + '-en.png').convert('RGB')
    s = np.array(src).astype(int)
    # main fill colour of the team circle = most common non-white colour
    q = s.reshape(-1, 3); q = q[(q < 240).any(1)]
    vals, cnt = np.unique(q // 8, axis=0, return_counts=True); fill = vals[cnt.argmax()] * 8 + 4
    def bbox(a):
        m = (np.abs(a - fill).sum(2) < 40).astype(np.uint8)
        n, lab, st, _ = cv2.connectedComponentsWithStats(m)
        i = 1 + st[1:, cv2.CC_STAT_AREA].argmax(); x, y, w, h = st[i, :4]; return x, y, w, h
    sx, sy, sw, sh = bbox(s)          # circle in team image
    dx, dy, dw, dh = bbox(arr)        # circle in silo5
    # the fill bbox misses the outline: grow both by outline width proportionally
    crop = en.crop((sx, sy, sx + sw, sy + sh)).resize((dw, dh), Image.LANCZOS)
    mask = Image.new('L', (dw, dh), 0); ImageDraw.Draw(mask).ellipse((1, 1, dw - 2, dh - 2), fill=255)
    base.paste(crop, (dx, dy), mask)
    print(team, 'src', (sx, sy, sw, sh), 'dst', (dx, dy, dw, dh))
base.save(B + 'silo5-en.png')
