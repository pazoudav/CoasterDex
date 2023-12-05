import cv2 as cv
from matcher.vlad.utils import RootSIFT as rtsift

class FeaturesExtractor:
    def extract(self, image):
        return [], []

class SIFT(FeaturesExtractor):
    def __init__(self) -> None:
        super().__init__()
        self.sift : cv.SIFT = cv.SIFT_create()
        
    def extract(self, image):
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        key_points = self.sift.detect(gray, None)
        key_points, descriptors = self.sift.detectAndCompute(gray,None)
        key_points = cv.KeyPoint.convert(key_points)
        return key_points, descriptors
    
class rootSIFT(SIFT):
    def extract(self, image):
        key_points, descriptors =  super().encode(image)
        return key_points, rtsift(descriptors)


