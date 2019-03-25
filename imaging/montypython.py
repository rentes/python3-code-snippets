#!/usr/bin/env python3
"""
    Python 3 image to ascii art example (based upon https://gist.github.com/cdiener/10567484)
    Author: Miguel Rentes
    https://github.com/rentes/python3-code-snippets/imaging/montypython.py
    Dependencies: PIL (or Pillow), NumPy
    Python version: 3.7.2
"""
import sys
from PIL import Image
import numpy as np

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

if len(sys.argv) != 4: 
    print( 'Usage: ./montypython.py image scale factor' )
    sys.exit()

f, SC, GCF, WCF = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), 7/4
img = Image.open(f)
S = (round(img.size[0]*SC*WCF), round(img.size[1]*SC))
img = np.sum(np.asarray(img.resize(S)), axis=2)
img -= img.min()
img = (1.0 - img/img.max())**GCF*(chars.size-1)

print('\n' + "\n".join(("".join(r) for r in chars[img.astype(int)])))