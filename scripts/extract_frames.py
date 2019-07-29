import os
import glob
from datetime import datetime
import numpy

# import the necessary packages
import cv2

src = '/media/ligong/Picasso/Share/cbimfs/Research/MURI/aligned-r3'
dst = '/media/ligong/Picasso/Datasets/muri/frames-r3'
fmt = 'img_%05d.jpg'
fps = 5

for filename in os.listdir(os.path.join(src)):
    in_file = os.path.join(src, filename)
    name = filename.replace('.mp4', '')
    if not os.path.exists(os.path.join(dst, name)):
        os.makedirs(os.path.join(dst, name))
    out_file = os.path.join(dst, name, fmt)
    cmd = f'ffmpeg -i {in_file} -vf fps={fps} {out_file} -hide_banner'
    os.system(cmd)
    print(f'--> {filename}')