#!/usr/bin/env python3
"""Rebuild 12345(-1).jpg overview from the (EN) step figures. Usage: compose_12345.py [en|nl] out.png"""
import sys, os
import numpy as np
from PIL import Image
D = os.path.join(os.path.dirname(__file__), '..', 'static', 'images', 'blog')
SRC = ['stap-1', 'Stap-2', 'Stap-3', 'Stap-4', 'Stap-5']
PANELS = [(6, 288, 18, 176), (321, 614, 9, 174), (664, 936, 13, 175), (997, 1239, 14, 140), (1318, 1587, 14, 98)]
def bbox(im):
    a = np.array(im.convert('L')) < 200; ys, xs = np.where(a)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
mode, out = sys.argv[1], sys.argv[2]
canvas = Image.new('RGB', (1600, 184), 'white')
for s, (x0, x1, y0, y1) in zip(SRC, PANELS):
    ref = Image.open(os.path.join(D, s + '.png')).convert('RGB')
    rb = bbox(ref)  # geometry from the original
    im = Image.open(os.path.join(D, s + ('-en.png' if mode == 'en' else '.png'))).convert('RGB')
    sx = (x1 - x0) / (rb[2] - rb[0]); sy = (y1 + 1 - y0) / (rb[3] - rb[1])
    big0 = im.resize((round(im.width * sx), round(im.height * sy)), Image.LANCZOS)
    big = Image.new('RGB', (big0.width + 400, big0.height + 400), 'white'); big.paste(big0, (0, 0))
    ox, oy = round(x0 - rb[0] * sx), round(y0 - rb[1] * sy)
    # paste full scaled panel clipped to its slot
    cx0, cx1 = max(0, x0 - 6), min(1600, x1 + 6)
    crop = big.crop((cx0 - ox, 0, cx1 - ox, big.height))
    canvas.paste(crop.crop((0, max(0, -oy), crop.width, max(0, -oy) + 184)), (cx0, max(0, oy)))
canvas.save(out)
print(out)
