import cv2 as cv
import os
import numpy as np

def folder_iterator(folder):
    for file in os.listdir(folder):
        f = os.path.join(folder, file)
        if os.path.isfile(f):
            yield f


def open_image(path: str):
    name = path.split('.')[-2].split('/')[-1]
    image = cv.imread(path)
    return image, name

def resize_to_width(img, width):
    shape = img.shape
    if len(shape) == 2:
        h,w = shape
    elif len(shape) == 3:
        h,w,_ = shape
    ratio = width/w
    height = int(ratio*h)
    img = cv.resize(img, (width,height))
    return img
