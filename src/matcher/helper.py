import cv2 as cv
import os

def folder_iterator(folder):
    for file in os.listdir(folder):
        f = os.path.join(folder, file)
        if os.path.isfile(f):
            yield f


def open_image(path: str):
    name = path.split('.')[-2].split('/')[-1]
    image = cv.imread(path)
    return image, name
