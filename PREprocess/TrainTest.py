from AbstractSplit import AbstractSplit
from sklearn.model_selection import train_test_split
class TrainTest(AbstractSplit):
   
    def __init__(self, valor): 
        self.valor = valor
       
    """ Divido el dataset en TRAIN y TEST, el porcentaje utilizado para test lo indica el usuario """    
    def splitDS(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = self.valor, random_state=0)        
        return X_train, y_train, X_test, y_test