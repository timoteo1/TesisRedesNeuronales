from abc import ABCMeta, abstractmethod

class AbstractSplit(object):
    
    _metaclass_ = ABCMeta
    
        
    
    def getClass(self, train):
        test = list()
        x = train[0]
        p = len(x) - 1
        for t in train:
            test.append(t[p])
        return test
    
    @abstractmethod
    def splitDS(self, valor, X, y): pass