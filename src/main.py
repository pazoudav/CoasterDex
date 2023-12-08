import cv2 as cv
import argparse
import numpy as np
import time

from coasterFinder import CoasterFinder
from coasterMatcher import CoasterMatcher
from displayHelpers import add_fps, display_matches, display_points, add_bounding_box

parser = argparse.ArgumentParser()
parser.add_argument('--source', '-s', type=str, choices=['webcam', 'ip'], default='webcam', 
                        help='select the source device')
parser.add_argument('--no_display', action='store_true', 
                        help='turn of display window')
parser.add_argument('-no_match', action='store_true')
parser.add_argument('-no_find', action='store_true')


 
def get_source(args):
    if args.source == 'webcam':
        cap = cv.VideoCapture(0)
    elif args.source == 'ip':
        cap = cv.VideoCapture('https://192.168.1.4:8080/video')
    return cap


def main_loop(matcher, finder):
    ret, img = cap.read()     
    bbox, best_matches = [], []
    if not args.no_find:
        bbox, = finder.find(img)         
    if not args.no_match:
        matcher_data = matcher.match(img, bbox=bbox) 
        if not args.no_display:
            if len(matcher_data['scan key points']) > 15:
                display_matches(matcher_data)
                add_bounding_box(img, matcher_data['matched key points'])
            display_points(img, matcher_data['key points'])
            display_points(img, matcher_data['matched key points'], color=(0,255,0))
            
             
    
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
    
    




