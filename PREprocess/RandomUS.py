from Sampling import Sampling
from imblearn.under_sampling import RandomUnderSampler


class RandomUS(Sampling):
    
    def __init__(self): 
        self.rus = RandomUnderSampler()
    
    def doSampling(self, X, Y):
        x_resampled, y_resampled = self.rus.fit_sample(X, Y)
        #print('Resampled dataset shape {}'.format(Counter(y_resampled)))
        return x_resampled, y_resampled
        