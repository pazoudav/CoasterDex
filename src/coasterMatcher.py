import cv2 as cv
from matcher.encoder import Encoder, VLAD
from matcher.featureExtractor import FeaturesExtractor, SIFT
from matcher.lookup import Lookup, ANNlookup
from matcher.helper import *
from joblib import load, dump
import numpy as np


    
def build_codebook_from_coco():
    fe = SIFT()
    descriptors = []
    
    print('loading descriptors from coco128')
    for file in folder_iterator('dataset/coco128'):
        image, _ = open_image(file)
        _, des = fe.extract(image)
        descriptors.append(des)
    print('descriptors loaded')    
    
    enc : VLAD = VLAD()
    enc.build_codebook(descriptors).save('VLAD-SIFT')
    print('codebook build')   
    
    
def build_lookup_from_database(database):
    fe = SIFT()
    en = VLAD().load('VLAD-SIFT')
    lk = ANNlookup()
    descriptors = []
    for file in folder_iterator(database):
        image, name = open_image(file)
        _, des = fe.extract(image)
        descriptors.append(des)
    features = en.encode(descriptors)
    lk.make(features).save('ANN-VLAD-SIFT')
    

class CoasterMatcher:
    def __init__(self, dataset='dataset/coaster-scans/'):
        self.featureExtractor : FeaturesExtractor = SIFT()
        self.encoder : Encoder = VLAD().load('VLAD-SIFT')
        self.lookup : Lookup = ANNlookup().load('ANN-VLAD-SIFT')
        self.index = {}
        self.dataset = dataset
        self.load_index('basic')
        
    def save_index(self, name):
        dump(self.index, f'matcher_files/{name}.idx')
        
    def load_index(self, name):
        self.index = load(f'matcher_files/{name}.idx')
        return self
        
    def make_index(self):
        for idx, file in enumerate(folder_iterator(self.dataset)):
            _, name = open_image(file)
            self.index[idx] = name
        return self
        
    def match(self, image, k=3, **kwargs):
        best_matches = []
        h,w,_ = image.shape
        image = cv.resize(image, (640, 640))
        key_points, descriptors = self.featureExtractor.extract(image)
        if descriptors is not None:
            features = self.encoder.encode([descriptors])
            idxs, dists = self.lookup.find(features, k=k)
            idxs = idxs[0]
        else:
            # in case no features are extracted from the image
            idxs = [0]*k
            dists = [[1000.0]*k]
            
        for idx in idxs:
            img_name = self.index[idx]
            img = cv.imread(f'{self.dataset}{img_name}.jpg')
            best_matches.append(cv.resize(img, (200, img.shape[0])))     
        ret_dict = {'matches': best_matches,
                    'distances': dists[0],
                    'key points': key_points*(w/640, h/640)}
        return ret_dict
    
    
    
if __name__ == '__main__':
    # build_codebook_from_coco()
    # build_lookup_from_database('dataset/coaster-scans/')
    ...
    