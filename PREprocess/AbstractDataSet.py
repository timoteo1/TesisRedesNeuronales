from abc import ABCMeta, abstractmethod

class AbstractDataSet(object):
    
    _metaclass_ = ABCMeta
    
    @abstractmethod
    def readDataSet(self): pass 