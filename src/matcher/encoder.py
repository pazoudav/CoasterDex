from matcher.vlad import VLAD as VLAD_
from joblib import dump, load

class Encoder:
    def __init__(self) -> None:
        self.codebook = None
    
    def load_codebook(self, path):
        self = load(path)
        return self
        
    def build_codebook(self, descriptors):
        return self
        
    def encode(self, descriptors):
        ...

    
    
class VLAD(Encoder):
    def __init__(self) -> None:
        super().__init__()
        self.codebook = VLAD_()
        
    def build_codebook(self, descriptors):
        print('building codebook...')
        self.codebook.fit(descriptors)
        return self
    
    def save(self, name):
        dump(self, f'matcher_files/{name}.enc')
        return self
    
    def load(self, name, verbose=False):
        self = load(f'matcher_files/{name}.enc')
        self.codebook.verbose = verbose
        return self
        
    def encode(self, descriptors):
        return self.codebook.transform(descriptors)
        