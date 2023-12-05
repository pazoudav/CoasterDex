import cv2 as cv
from matcher.encoder import Encoder, VLAD
from matcher.featureExtractor import FeaturesExtractor, SIFT
from matcher.helper import *

    
def build_codebook_from_coco():
    fe = SIFT()
    descriptors = []
    
    print('loading descriptors')
    for file in folder_iterator('dataset/coco128'):
        image, _ = open_image(file)
        _, des = fe.extract(image)
        descriptors.append(des)
    print('descriptors loaded')    
    
    enc = VLAD().load()
    enc.build_codebook(descriptors).save()
    print('codebook build')   
    
    
class Lookup:
    ...


class CoasterMatcher:
    def __init__(self):
        self.featureExtractor : FeaturesExtractor = SIFT()
        self.encoder : Encoder = VLAD().load()
        self.lookup : Lookup = Lookup()  
        
    def match(self, image, **kwargs):
        best_matches = None
        key_points, descriptors = self.featureExtractor.extract()
        return best_matches, 
    
    
    
if __name__ == '__main__':
    build_codebook_from_coco()

    