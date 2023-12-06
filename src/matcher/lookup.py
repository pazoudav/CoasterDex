import pynndescent
from joblib import load, dump

class Lookup:
    def __init__(self) -> None:
        pass
    
    def find(self, features):
        return []
    
    def add_feature(self, feature):
        return self
    
    def save(self, name):
        dump(self, f'matcher_files/{name}.lkp')
        
    def load(self, name):
        self = load(f'matcher_files/{name}.lkp')
        return self
    
    
class ANNlookup(Lookup):
    def __init__(self) -> None:
        super().__init__()
        self.index = None
    
    def make(self, features):
        self.index = pynndescent.NNDescent(features)
        self.index.prepare()
        return self
        
    def add_feature(self, feature):
        if self.index:
            self.index.update([feature]) 
        return self  
           
    def find(self, features, k=5):
        if not self.index:
            return [], []
        idxs, dists = self.index.query(features, k=k)
        return idxs, dists
        
   