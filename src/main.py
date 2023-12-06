import cv2 as cv
import argparse
import numpy as np
import time

from coasterFinder import CoasterFinder
from coasterMatcher import CoasterMatcher

parser = argparse.ArgumentParser()
parser.add_argument('--source', '-s', type=str, choices=['webcam', 'ip'], default='webcam', 
                        help='select the source device')
parser.add_argument('--no_display', action='store_true', 
                        help='turn of display window')
parser.add_argument('-no_match', action='store_true')
parser.add_argument('-no_find', action='store_true')

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
 
def get_source(args):
    if args.source == 'webcam':
        cap = cv.VideoCapture(0)
    elif args.source == 'ip':
        cap = cv.VideoCapture('https://192.168.1.16:8080/video')
    return cap
 
 
def display_matches(matches, distances):
    if args.no_display:
        return
    img = np.vstack(matches)
    cv.putText(img, f'best match: {distances[0]:.2f}', (8,30), font, 0.7, (0,255,0), 2, cv.LINE_AA)
    cv.imshow('matches', img)
 
 
def main_loop(matcher, finder):
    ret, img = cap.read()     
    bbox, best_matches = [], []
    if not args.no_find:
        bbox, = finder.find(img)         
    if not args.no_match:
        best_matches, distances = matcher.match(img, bbox=bbox) 
        display_matches(best_matches, distances)
    
    if not args.no_display:
        add_fps(img)
        cv.imshow('frame', img)
        
    if cv.waitKey(1) & 0xFF == ord('q'):
        return False    
    return True
 


 

if __name__ == '__main__':  
    args = parser.parse_args()
    cap = get_source(args)
    
    matcher = None if args.no_match else CoasterMatcher()
    finder = None if args.no_find else CoasterFinder()
    
    while main_loop(matcher, finder):
        ...
        
    cap.release()
    cv.destroyAllWindows()    
    
    




