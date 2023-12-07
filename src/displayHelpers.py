import time
import cv2 as cv
import numpy as np

font = cv.FONT_HERSHEY_SIMPLEX 
now = time.time() 
 
def tick():
    global now
    delta = time.time() - now
    now = time.time()
    if delta <  0.001:
        delta = 0.001
    return delta

def add_fps(img):
    fps = 1/tick() # int(1/tick()) # 
    cv.putText(img, f'{fps:.2f}', (10,30), font, 1, (0,0,255), 2, cv.LINE_AA)
    return fps

def display_matches(matcher_data : dict):
    img = np.vstack(matcher_data['matches'])
    cv.putText(img, f'best match: {matcher_data["distances"][0]:.2f}', (8,30), font, 0.7, (0,255,0), 2, cv.LINE_AA)
    cv.imshow('matches', img)
    
def display_points(img, points, color=(255,0,0)):
    for point in points:
        cv.drawMarker(img, point.astype(int), color, markerType=cv.MARKER_CROSS, markerSize=10, thickness=1)