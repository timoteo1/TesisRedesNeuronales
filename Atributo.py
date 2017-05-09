
class Atributo(object):
    
    def __init__(self, X_resampled, y_resampled, X_trainSplit, y_trainSplit, X_testSplit, y_testSplit, Split):
        self.X_resampled = X_resampled
        self.y_resampled = y_resampled
        self.X_trainSplit = X_trainSplit 
        self.y_trainSplit = y_trainSplit 
        self.X_testSplit = X_testSplit 
        self.y_testSplit = y_testSplit
        self.tipoSplit = Split
        self.y_test = 0
        self.predictClass = 0
        self.pad_sequences = 0
        self.cantidad_clases = 0
        
    def setCantClases(self, y):
        self.cantidad_clases = y
        
    def setPad_sequences(self, y):
        self.pad_sequences = y    

    def setPredictClass(self, y):
        self.predictClass = y

    def setY_test(self, y):
        self.y_test = y

    def setX_resampled(self, X):
        self.X_resampled = X
    
    def setY_resampled(self, y):
        self.y_resampled = y
    
    def setX_trainSplit(self, X):
        self.X_trainSplit = X
    
    def sety_trainSplit(self, y):
        self.y_trainSplit = y
        
    def setX_testSplit(self, X):
        self.X_testSplit = X
    
    def sety_testSplit(self, y):
        self.y_testSplit = y
       
    def getX_resampled(self):
        return self.X_resampled
    
    def getY_resampled(self):
        return self.y_resampled
    
    def getX_trainSplit(self):
        return self.X_trainSplit
    
    def gety_trainSplit(self):
        return self.y_trainSplit
        
    def getX_testSplit(self):
        return self.X_testSplit 
    
    def gety_testSplit(self):
        return self.y_testSplit
    
    def get_TipoSplit(self):
        return self.tipoSplit

    def getY_test(self):
        return self.y_test
    
    def getPredictClass(self):
        return self.predictClass
    
    def getPad_sequences(self):
        return self.pad_sequences
    
    def getCantClases(self):
        return self.cantidad_clases
    
    """ 
    def __init__(self, atributo, valor):
        self.atributo = atributo
        self.valor = valor
        
    def getAtributo(self):
        return self.atributo
    
    def getValor(self):
        return self.valor
    """