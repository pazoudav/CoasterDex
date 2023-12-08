import cv2 as cv
from matcher.encoder import Encoder, VLAD
from matcher.featureExtractor import FeaturesExtractor, SIFT, RootSIFT, SURF
from matcher.lookup import Lookup, ANNlookup
from matcher.helper import *
from joblib import load, dump
import numpy as np
from skimage.measure import ransac
from skimage.transform import AffineTransform
import random



    
def build_codebook_from_coco():
    fe = SURF()
    descriptors = []
    
    print('loading descriptors from coco128')
    for file in folder_iterator('dataset/coco128'):
        image, _ = open_image(file)
        _, des = fe.extract(image)
        descriptors.append(des)
    print('descriptors loaded')    
    
    enc : VLAD = VLAD()
    enc.build_codebook(descriptors).save('VLAD-SURF')
    print('codebook build')   
    
    
def build_lookup_from_database(database):
    fe = SURF()
    en = VLAD().load('VLAD-SURF')
    lk = ANNlookup()
    descriptors = []
    for file in folder_iterator(database):
        image, name = open_image(file)
        _, des = fe.extract(image)
        descriptors.append(des)
    features = en.encode(descriptors)
    lk.make(features).save('ANN-VLAD-SURF')
    

class CoasterMatcher:
    def __init__(self, dataset='dataset/coaster-scans/'):
        self.featureExtractor : FeaturesExtractor = RootSIFT()
        self.encoder : Encoder = VLAD().load('VLAD-RootSIFT')
        self.lookup : Lookup = ANNlookup().load('ANN-VLAD-RootSIFT')
        self.index = {}
        self.dataset = dataset
        self.clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
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
    
    def preprocess(self, img):
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    
        img = self.clahe.apply(img)
        img = resize_to_width(img, 640)
        return img
        
    def match(self, image, k=5, **kwargs):
        best_matches = []
        h,w,_= image.shape
        image = self.preprocess(image)
        key_points, descriptors = self.featureExtractor.extract(image)
        if descriptors is not None:
            features = self.encoder.encode([descriptors])
            idxs, dists = self.lookup.find(features, k=k)
            idxs = idxs[0]
        else:
            # in case no features are extracted from the image
            idxs = [0]*k
            dists = [[1000.0]*k]
            
        # load best matches and resize to the same width
        for idx in idxs:
            img_name = self.index[idx]
            img = cv.imread(f'{self.dataset}{img_name}.jpg')
            best_matches.append(img)     
                
        h_, w_ = image.shape
        key_points = key_points*[w/w_, h/h_] if len(key_points) > 0 else key_points # scale to original size
        photo_key_points, scan_key_points = self.find_matching_points(best_matches[0], descriptors, key_points)        
        
        ret_dict = {'matches': best_matches,
                    'distances': dists[0],
                    'key points': key_points,
                    'matched key points': photo_key_points,
                    'scan key points': scan_key_points
                    }
        return ret_dict


    def find_matching_points(self, img, img_descriptors, img_points):
        best_key_points, best_descriptors = self.featureExtractor.extract(img)
        matches = cv.BFMatcher().knnMatch(img_descriptors, best_descriptors, k=2)
        good, good_ = set(), set()
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good.add(m.queryIdx)
                good_.add(m.trainIdx)
        return img_points[list(good)], best_key_points[list(good_)]

    
    
    def add_coaster(self, img, bbox, name):
        (x0,y0), (x1,y1) = bbox
        image = img[y0:y1,x0:x1]
        cv.imwrite(f'dataset/coaster-scans/{name}.jpg', image)
        resize_to_width(image, 200)
        key_points, descriptors = self.featureExtractor.extract(image)
        if descriptors is not None:
            features = self.encoder.encode([descriptors])
            self.lookup.add_feature(features)
            self.index[len(self.index)] = name
            self.save_index('updated')
       
    
    
    
if __name__ == '__main__':
    # build_codebook_from_coco()
    # build_lookup_from_database('dataset/coaster-scans/')
    ...
    matcher = CoasterMatcher()
    image = cv.imread('dataset/coaster-photos/3.jpg')
    matcher.add_coaster(image.copy(), ((100,800), (850,1500)), 'aaaa')
    data = matcher.match(image)
    for idx, img in enumerate(data['matches']):
        cv.imwrite(f'test_{idx}.jpg', img)