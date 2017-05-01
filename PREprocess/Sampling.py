from abc import ABCMeta, abstractmethod

class Sampling(object):
    _metaclass_ = ABCMeta
 
    @abstractmethod 
    def doSampling(self, X, Y): pass
    

               
        