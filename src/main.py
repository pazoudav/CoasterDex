import cv2 as cv
import argparse
import numpy as np
import os
import time

from coasterFinder import CoasterFinder
from coasterMatcher import CoasterMatcher
from displayHelpers import add_fps, display_matcher_data, freeze_display, ImageInput, FolderInput, display_bboxs
from matcher.helper import resize_to_width

parser = argparse.ArgumentParser()
parser.add_argument('--source', '-s', type=str, default='webcam', 
                        help='select the source device')
parser.add_argument('--no_display', action='store_true', 
                        help='turn of display window')
parser.add_argument('-no_match', action='store_true')
parser.add_argument('-no_find', action='store_true')
parser.add_argument('--display', '-d', nargs='+', type=str, choices=['f_bbox', 'm_bbox', 'm_kp', 'm_mkp'], default=[])
 
def get_source(args):
    if args.source == 'webcam':
        cap = cv.VideoCapture(0)
    elif args.source == 'ip':
        cap = cv.VideoCapture('https://192.168.1.4:8080/video')
    elif os.path.isfile(args.source):
        cap = ImageInput(args.source)
    elif os.path.isdir(args.source):
        cap = FolderInput(args.source)
    else:
        raise ValueError("invalid source")
    return cap


def main_loop(matcher, finder):
    ret, img = cap.read()  
    org_img = img.copy()
    bboxs, best_matches = [], []
    if not args.no_find:
        bboxs, = finder.find(org_img)  
        display_bboxs(img, bboxs, args)
    if not args.no_match:
        matcher_data =  matcher.match_wrap(org_img, bboxs=bboxs, k=3)
        display_matcher_data(img, matcher_data, args) 
        
    
    if not args.no_display:
        add_fps(img)
        # img = resize_to_width(img, 360) 
        cv.imshow('frame', img)
          
    key = cv.waitKey(1)
    if key == ord('q'):
        return False    
    elif key == ord('c'):
        freeze_display(org_img, matcher.add_coaster)
        
    return ret
 

if __name__ == '__main__':  
    args = parser.parse_args()
    cap = get_source(args)
    
    matcher = None if args.no_match else CoasterMatcher() # file to the images of test scans
    finder = None if args.no_find else CoasterFinder()

    while main_loop(matcher, finder):
        ...
        
    cap.release()
    cv.destroyAllWindows()    
    
