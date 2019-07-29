import os
import glob
from datetime import datetime
import numpy


def read_xy(filename):
    with open(filename, 'r') as f:
        l = f.readline()
    l = l.split()
    return int(l[0]), int(l[1])

base = '/media/ligong/Picasso/Share/cbimfs'
src_txt = f'{base}/Research/MURI/r3.txt'
src_vid = f'{base}/Research/MURI/clips-r3'
src_lmk = f'{base}/Research/MURI/openface/clips-r3'
src_lmk2 = f'{base}/Research/MURI/openface/clips-r3_wrong-fps'
dst = f'{base}/Research/MURI/aligned-r3'

if not os.path.exists(dst):
    os.makedirs(dst)

with open(src_txt, 'r') as f:
    filenames = [l.rstrip('\n') for l in f.readlines()]

names = [f'{l.split("_")[0]}-{int(l.split("_")[1]):03d}_{l.split("_")[2]}_R3' for l in filenames]

# with open('/home/lh599/Research/MURI/openface/clips-r3/AZ-005_1_R3/AZ-005_1_R3.csv', 'r') as f:
#     h = [hh.strip(' ') for hh in f.readline().rstrip('\n').split(',')]
# cols_x = [f'x_{i}' for i in range(68)]
# cols_y = [f'y_{i}' for i in range(68)]

wrong_list = '/media/ligong/Picasso/Active/muri-scan/sourcefiles/wrong-fps.txt'
with open(wrong_list, 'r') as f:
    wrong_names_old = [l.rstrip('\n').replace('.mp4', '') for l in f.readlines()]
    wrong_names = [f'{l.split("_")[0]}-{int(l.split("_")[1]):03d}_{l.split("_")[2]}_R3' for l in wrong_names_old]

for name in names:
    if name in wrong_names:
        name2 = wrong_names_old[wrong_names.index(name)]
        img_path = os.path.join(src_lmk2, name, f'{name2}_aligned')
        vid_path = os.path.join(dst, f'{name}.mp4')
        os.system(f'ffmpeg -r 30 -f image2 -i {img_path}/frame_det_00_%06d.bmp -vcodec libx264 -crf 25 -pix_fmt yuv420p {vid_path}')
    else:
        in_file = os.path.join(src_lmk, name, 'aligned.mp4')
        out_file = os.path.join(dst, f'{name}.mp4')
        os.system(f'cp {in_file} {out_file}')
    # vid_file = os.path.join(src_vid, f'{name}.mp4')
    # lmk_file = os.path.join(src_lmk, name, f'{name}.csv')
    print(f'--> {name}')
