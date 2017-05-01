from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, zero_one_loss
import numpy as np

class PostProcess(object):
    
    def __init__(self):
        pass
    
    def getMetrics(self, tipo, y_test, X_test):
        
        if tipo == 'accuracy_score':
            return accuracy_score(np.argmax(y_test, axis=-1), X_test)
        elif tipo == 'confusion_matrix':
            return confusion_matrix(np.argmax(y_test, axis=-1), X_test)
        elif tipo == 'precision_score':
            return precision_score(np.argmax(y_test, axis=-1), X_test, average = None)
        elif tipo == 'recall_score':
            return recall_score(np.argmax(y_test, axis=-1), X_test, average=None)
        elif tipo == 'zero_one_loss':
            return zero_one_loss(np.argmax(y_test, axis=-1), X_test) 