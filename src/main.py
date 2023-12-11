import cv2 as cv
import argparse
import numpy as np

from coasterFinder import CoasterFinder
from coasterMatcher import CoasterMatcher
from displayHelpers import add_fps, display_matcher_data, freeze_display

parser = argparse.ArgumentParser()
parser.add_argument('--source', '-s', type=str, default='webcam', 
                        help='select the source device')
parser.add_argument('--no_display', action='store_true', 
                        help='turn of display window')
parser.add_argument('-no_match', action='store_true')
parser.add_argument('-no_find', action='store_true')

class Img:
    def __init__(self, path):
        self.img = cv.imread(path)
    def read(self):
        return True, self.img.copy()
 
def get_source(args):
    if args.source == 'webcam':
        cap = cv.VideoCapture(0)
    elif args.source == 'ip':
        cap = cv.VideoCapture('https://192.168.1.4:8080/video')
    else:
        cap = Img(args.source)
    return cap


def main_loop(matcher, finder):
    ret, img = cap.read()     
    org_img = img.copy()
    bbox, best_matches = [], []
    if not args.no_find:
        bbox, = finder.find(img)         
    if not args.no_match:
        matcher_data = matcher.match(img, bbox=bbox) 
        display_matcher_data(img, matcher_data, args)  
    
    if not args.no_display:
        add_fps(img)
        cv.imshow('frame', img)
        
    key = cv.waitKey(1)
    if key == ord('q'):
        return False    
    elif key == ord('c'):
        freeze_display(org_img, matcher.add_coaster)
        
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
    
    




