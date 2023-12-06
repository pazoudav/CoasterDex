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

# def set_scans_to_200_width(folder):
#     for file in folder_iterator(folder):
#         image, name = open_image(file)
#         # h, w, _ = image.shape
#         # empty = np.zeros((h, 200, 3),dtype=int)
#         # empty[:h,:w,:] = image
#         # print(empty.shape)
#         # print(empty)
#         empty = cv.resize(image, (200, image.shape[0]))
#         print(empty.shape)
#         while True:
#             cv.imshow('test', empty)
#             if cv.waitKey(1) & 0xFF == ord('q'):
#                 break
        
# set_scans_to_200_width('dataset/coaster-scans/')
