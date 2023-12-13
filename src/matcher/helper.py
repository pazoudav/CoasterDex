import cv2 as cv
import os
import numpy as np

def folder_iterator(folder):
    for file in os.listdir(folder):
        if 'gitignore' in file:
            continue
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

def get_img_shape(img):
	if len(img.shape) == 2:
		h,w = img.shape
	elif len(img.shape) == 3:
		h,w,_ = img.shape
	return w, h
	
def extract_img(img, bbox):
	w,h = get_img_shape(img)
	(x0,y0),(x1,y1) = bbox
	x0 = max(0,x0)
	y0 = max(0,y0)
	x1 = min(w,x1)
	y1 = min(h,y1)
	img_ = img[y0:y1, x0:x1]
	return img_, x0, y0