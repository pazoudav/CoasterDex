import cv2 as cv
import numpy  as np

class FeaturesExtractor:
    def extract(self, image):
        return [], []

class SIFT(FeaturesExtractor):
    def __init__(self) -> None:
        super().__init__()
        self.sift : cv.SIFT = cv.SIFT_create()
        
    def extract(self, image):
        key_points, descriptors = self.sift.detectAndCompute(image, None)
        key_points = cv.KeyPoint.convert(key_points)
        return key_points, descriptors
    
    
class RootSIFT(SIFT):
    def extract(self, image):
        key_points, descriptors =  super().extract(image)
        # in case no key-points found:
        if descriptors is None:
            return key_points, descriptors
        
        descriptors = descriptors / descriptors.sum(axis=1, keepdims=True)
        descriptors = np.sqrt(descriptors)
        return key_points, descriptors


class SURF(FeaturesExtractor):
    def __init__(self, hess_threshold=400) -> None:
        super().__init__()
        self.hess_threshold = hess_threshold
        self.surf = cv.xfeatures2d.SURF_create(hess_threshold)
        self.surf.setExtended(True)  
        
    def extract(self, image):
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        key_points, descriptors = self.surf.detectAndCompute(gray, None)
        key_points = cv.KeyPoint.convert(key_points)
        return key_points, descriptors


