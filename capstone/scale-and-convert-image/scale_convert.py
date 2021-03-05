#!/usr/bin/python3

import os
from PIL import Image

# define all the constant
SOURCE_DIR = os.path.join(os.path.abspath(os.curdir), 'images')
DESTINATION_DIR = '/opt/icons' # debug: DESTINATION_DIR = './result/'
IMG_SIZE = (128, 128)
FILE_TYPE = 'JPEG'

# get image names from SOURCE__DIR
image_names = os.listdir(SOURCE_DIR)

if os.path.isfile(os.path.join(SOURCE_DIR, '.DS_Store')):
    image_names.remove('.DS_Store')

# check if DESTINATION_DIR exists, create it if not
if not os.path.exists(DESTINATION_DIR):
    os.makedirs(DESTINATION_DIR)

# iterate the image to rotate and resize it
for name in image_names:
    img = Image.open(os.path.join(SOURCE_DIR, name)).convert('RGB')
    img = img.rotate(90)
    img = img.resize(IMG_SIZE)
    img.save(os.path.join(DESTINATION_DIR, name), FILE_TYPE)