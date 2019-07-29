import os
import glob
from datetime import datetime
import numpy

# import the necessary packages
# from ..convenience import is_cv3
import cv2


def count_frames(path, override=False):
    # grab a pointer to the video file and initialize the total
    # number of frames read
    video = cv2.VideoCapture(path)
    total = 0

    # if the override flag is passed in, revert to the manual
    # method of counting frames
    if override:
        total = count_frames_manual(video)

    # otherwise, let's try the fast way first
    else:
        # lets try to determine the number of frames in a video
        # via video properties; this method can be very buggy
        # and might throw an error based on your OpenCV version
        # or may fail entirely based on your which video codecs
        # you have installed
        try:
            # check if we are using OpenCV 3
            # if is_cv3():
            #     total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            #
            # # otherwise, we are using OpenCV 2.4
            # else:
            #     total = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
            total = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))

        # uh-oh, we got an error -- revert to counting manually
        except:
            total = count_frames_manual(video)

    # release the video file pointer
    video.release()

    # return the total number of frames in the video
    return total


def count_frames_manual(video):
    # initialize the total number of frames read
    total = 0

    # loop over the frames of the video
    while True:
        # grab the current frame
        (grabbed, frame) = video.read()

        # check to see if we have reached the end of the
        # video
        if not grabbed:
            break

        # increment the total number of frames read
        total += 1

    # return the total number of frames in the video file
    return total


src = '/media/ligong/Picasso/Share/cbimfs/Research/MURI/aligned-r3'
in_file = '/media/ligong/Picasso/Share/cbimfs/Active/muri-scan/code/data/val.txt'
out_file = '/media/ligong/Picasso/Active/tsn-pytorch/sourcefiles/val.txt'
label_file = '/media/ligong/Picasso/Share/cbimfs/Active/muri-scan/labels.txt'
data_root = 'data/frames-r3'

with open(in_file, 'r') as f:
    lines = [l.split()[0] for l in f.readlines()]

lines = list(set(lines))

with open(label_file, 'r') as f:
    labels = {l.split()[0]: l.split()[1] for l in f.readlines()}

with open(out_file, 'w') as f:
    for l in lines:
        # num_frames = count_frames(f'{os.path.join(src, l)}.mp4')
        num_frames = len(os.listdir(os.path.join('..', data_root, l)))
        label = labels[l.replace('_R3', '')]
        f.write(f'{os.path.join(data_root, l)} {num_frames} {label}\n')
        print(f'--> {l}')

