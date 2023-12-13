import cv2 as cv
from matcher.encoder import Encoder, VLAD
from matcher.featureExtractor import FeaturesExtractor, SIFT, RootSIFT, ORB, MAC
from matcher.lookup import Lookup, ANNlookup, KDTree, BallTree, ProductQuantization, LocallySensitiveHashing
from matcher.helper import *
from joblib import load, dump
import numpy as np
import time
import random



    
def build_codebook_from_coco():
    fe = RootSIFT()
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
    

def build_codebook_from_coco_and_scans():
    fe = RootSIFT()
    descriptors_ = []
    
    print('loading descriptors from coco128 and scans')
    for file in folder_iterator('dataset/coco128'):
        image, _ = open_image(file)
        _, des = fe.extract(image)
        descriptors_.append(des)
    for file in folder_iterator('dataset/coaster-scans'):
        image, _ = open_image(file)
        _, des = fe.extract(image)
        descriptors_.append(des)
    print('descriptors loaded')  
    
    descriptors = random.sample(descriptors_, 128)
    
    enc : VLAD = VLAD()
    enc.build_codebook(descriptors).save('VLAD-RootSIFT-mixed')
    print('codebook build')  

    
def build_lookup_from_database(database):
    fe = RootSIFT()
    en = VLAD().load('VLAD-RootSIFT')
    lk = LocallySensitiveHashing()
    descriptors = []
    for file in folder_iterator(database):
        image, name = open_image(file)
        _, des = fe.extract(image)
        descriptors.append(des)
    features = en.encode(descriptors)
    lk.make(features).save('LSH-VLAD-RootSIFT')
    

class CoasterMatcher:
    def __init__(self, dataset='dataset/coaster-scans/'):
        self.featureExtractor : FeaturesExtractor = RootSIFT()
        self.encoder : Encoder = VLAD().load('VLAD-RootSIFT')
        self.lookup : Lookup = BallTree().load('BallTree-VLAD-RootSIFT')
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
        
    def match_wrap(self, image, bboxs, k=5, **kwargs):
        ...    
    
    def match(self, image, k=5, **kwargs):
        best_matches = []
        photo_key_points, scan_key_points = [], []
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
            img_name = f'{self.dataset}{self.index[idx]}.jpg' 
            if os.path.exists(img_name):
                img = cv.imread(img_name)
                best_matches.append(img)     
          
        if len(image.shape) == 2:      
            h_,w_ = image.shape
        elif len(image.shape) == 3:
            h_,w_,_ = image.shape
        else:
            raise ValueError("wrong image dimensions")
        
        key_points = key_points*[w/w_, h/h_] if len(key_points) > 0 else np.array(key_points) # scale to original size
        if len(best_matches) > 0:
            photo_key_points, scan_key_points = self.find_matching_points(best_matches[0], descriptors, key_points) 
        
        ret_dict = {'matches': best_matches,
                    'distances': dists[0],
                    'key points': key_points,
                    'matched key points': photo_key_points,
                    'scan key points': scan_key_points
                    }
        return ret_dict


    def find_matching_points(self, img, img_descriptors, img_points):
        if len(img_points) == 0:
            return [], []
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
        
        # save thumbnail
        small_img = resize_to_width(image.copy(), 200)
        name = f'{name}-{int(time.time())}' # adding time tag to prevent name collisions
        cv.imwrite(f'dataset/coaster-scans/{name}.jpg', small_img)
        
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    
        image = self.clahe.apply(image)
        image = resize_to_width(image, 200)
        key_points, descriptors = self.featureExtractor.extract(image)
        if descriptors is not None:
            features = self.encoder.encode([descriptors])
            self.lookup.add_feature(features)
            self.index[len(self.index)] = name
            self.save_index('updated')
       
    
    
    
if __name__ == '__main__':
    # build_codebook_from_coco_and_scans()
    build_lookup_from_database('dataset/coaster-scans/')
    ...
