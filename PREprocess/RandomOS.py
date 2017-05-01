from Sampling import Sampling
from imblearn.over_sampling.random_over_sampler import RandomOverSampler

class RandomOS(Sampling):
    
    def __init__(self): 
        self.ros = RandomOverSampler() 
    
    def doSampling(self, X, Y):
      
        x_res, y_res = self.ros.fit_sample(X, Y)
        
        return x_res, y_res
        