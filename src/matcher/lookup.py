import pynndescent
from joblib import load, dump
from sklearn.neighbors import NearestNeighbors
import numpy as np
import nanopq
import nearpy

class Lookup:
    def __init__(self) -> None:
        pass
    
    def find(self, features, k=5):
        return [[]], [[]]
    
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
            print('updating index')
            self.index.update(feature) 
            self.index.prepare()
        return self  
           
    def find(self, features, k=5):
        if not self.index:
            return [[]], [[]]
        idxs, dists = self.index.query(features, k=k)
        return idxs, dists
    
    
class NearestNeighbors_(Lookup):
    def __init__(self, k=5) -> None:
        super().__init__()
        self.func = NearestNeighbors(n_neighbors=k, algorithm='kd_tree', leaf_size=16)
        self.features = []
        self.k = k
    
    def make(self, features):
        self.features = features
        self.func.fit(self.features)
        return self
        
    def add_feature(self, feature):
        self.features = np.vstack((self.features,feature))
        self.func.fit(self.features)
        return self  
           
    def find(self, features, k=5):
        if len(self.features) == 0:
            return [[]], [[]]
        dists, idxs = self.func.kneighbors(features, k)
        return idxs, dists
    
    
class KDTree(NearestNeighbors_):
    def __init__(self, k=5) -> None:
        super().__init__()
        self.func = NearestNeighbors(n_neighbors=k, algorithm='kd_tree')
    
    
class BallTree(NearestNeighbors_):
    def __init__(self, k=5) -> None:
        super().__init__()
        self.func = NearestNeighbors(n_neighbors=k, algorithm='ball_tree')

class ProductQuantization(Lookup):
    def __init__(self, M=512, Ks=64) -> None:
        super().__init__()
        self.pq = nanopq.PQ(M=M, Ks=Ks, verbose=True)
        self.M = M
        self.Ks = Ks
        self.X_code = None
        self.features = []
        
    def make(self, features):
        self.features = features.astype(np.float32)
        self.pq.fit(self.features)
        self.X_code = self.pq.encode(self.features)
        return self
    
    def add_feature(self, feature):
        feature = feature.astype(np.float32)
        self.features = np.vstack((self.features, feature))
        self.pq.fit(self.features)
        self.X_code = self.pq.encode(self.features)
        return self
    
    def find(self, features, k=5):
        if self.X_code is None:
            return [[]], [[]]
        query = features[0].astype(np.float32)
        dt = self.pq.dtable(query=query)  
        dists = dt.adist(codes=self.X_code)
        idxs = np.argsort(dists)[:k]
        dists = dists[idxs]
        return [idxs], [dists]

class LocallySensitiveHashing(Lookup):
    def __init__(self) -> None:
        super().__init__()
        dimension = 2**15
        rbp = nearpy.hashes.RandomBinaryProjections('rbp', 8)
        self.engine = nearpy.Engine(dimension, lshashes=[rbp])

    def make(self, features):
        for idx,f in enumerate(features):
            self.engine.store_vector(f, idx)
        return self
    
    def find(self, features, k=5):
        query = features[0]
        N = self.engine.neighbours(query)
        idxs = []
        dists = []
        for line in N:
            v, idx, dist = line
            idxs.append(idx)
            dists.append(dist)
        return [idxs], [dists]
