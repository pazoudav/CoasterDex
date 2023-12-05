import cv2 as cv
import argparse

from coasterFinder import CoasterFinder
from coasterMatcher import CoasterMatcher

parser = argparse.ArgumentParser()
parser.add_argument('--source', '-s', type=str, choices=['webcam', 'ip'], default='webcam', 
                        help='select the source device')
parser.add_argument('--no_display', action='store_true', 
                        help='turn of display window')
parser.add_argument('-no_match', action='store_true')
parser.add_argument('-no_find', action='store_true')

# font = cv.FONT_HERSHEY_SIMPLEX 
# now = time.time() 
 
 
def get_source(args):
    if args.source == 'webcam':
        cap = cv.VideoCapture(0)
    elif args.source == 'ip':
        cap = cv.VideoCapture('https://192.168.1.16:8080/video')
    return cap
 
 
def main_loop(matcher, finder):
    ret, img = cap.read()     
    
    if not args.no_find:
        bbox, = finder.find(img)         
    if not args.no_match:
        best_matches, = matcher.match(img, bbox=bbox)    
    
    if not args.no_display:
        cv.imshow('frame', img)
        
    if cv.waitKey(1) & 0xFF == ord('q'):
        return False    
    return True
 


 

if __name__ == '__main__':  
    args = parser.parse_args()
    cap = get_source(args)
    
    if args.no_match:
        matcher = None
    else:
        matcher = CoasterMatcher()
    if args.no_find:
        finder = None
    else:
        finder = CoasterFinder()
    
    while main_loop(matcher, finder):
        ...
        
    cap.release()
    cv.destroyAllWindows()    
    
    




