#!/usr/bin/env python3
"""Remove the brand logo (top-right) and fractal1 footer from boston1-5 / fractal1 (NL + EN)."""
import cv2, numpy as np, os
D=os.path.join(os.path.dirname(__file__),'..','static','images','blog')
for n in ['boston1','boston2','boston3','boston4','boston5','fractal1']:
    for suf in ['','-en']:
        p=os.path.join(D,n+suf+'.png'); im=cv2.imread(p)
        if n.startswith('boston'):
            im[3:54,726:793]=255
        else:
            m=np.zeros(im.shape[:2],np.uint8)
            for x0,y0,x1,y1 in [(726,3,793,54),(370,420,432,438)]:
                g=cv2.cvtColor(im[y0:y1,x0:x1],cv2.COLOR_BGR2GRAY)
                sat=im[y0:y1,x0:x1].max(2).astype(int)-im[y0:y1,x0:x1].min(2)
                m[y0:y1,x0:x1]=((g<215)|(sat>25)).astype(np.uint8)*255
            m=cv2.dilate(m,np.ones((3,3),np.uint8))
            im=cv2.inpaint(im,m,4,cv2.INPAINT_TELEA)
        cv2.imwrite(p,im)
