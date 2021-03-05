#!/usr/bin/env python3

from PIL import Image

import os

SOURCE = "/home/student-01-7207a75628ea/supplier-data/images"
FILE_TYPE = 'JPEG'
IMG_SIZE = (600, 400)

files = os.listdir(SOURCE)
for fname in files:
    if not (".jpeg" in fname or ".tiff" in fname):
        continue
    img = Image.open(os.path.join(SOURCE, fname))
    img = img.convert("RGB")
    img = img.resize(IMG_SIZE)
    fname = fname.replace(".tiff", ".jpeg")
    img.save(os.path.join(SOURCE, fname), FILE_TYPE)
