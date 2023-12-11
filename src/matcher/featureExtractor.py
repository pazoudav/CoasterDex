import cv2 as cv
import numpy  as np

class FeaturesExtractor:
    def __init__(self) -> None:
        self.extractor = ...
        
    def extract(self, image):
        key_points, descriptors = self.extractor.detectAndCompute(image, None)
        key_points = cv.KeyPoint.convert(key_points)
        return key_points, descriptors

class SIFT(FeaturesExtractor):
    def __init__(self) -> None:
        super().__init__()
        self.extractor : cv.SIFT = cv.SIFT_create()
    
    
class RootSIFT(SIFT):
    def extract(self, image):
        key_points, descriptors =  super().extract(image)
        # in case no key-points found:
        if descriptors is None:
            return key_points, descriptors
        
        descriptors = descriptors / descriptors.sum(axis=1, keepdims=True)
        descriptors = np.sqrt(descriptors)
        return key_points, descriptors


class ORB(FeaturesExtractor):
    def __init__(self) -> None:
        super().__init__()
        self.extractor = cv.ORB().create()
                            

                            

