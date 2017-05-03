from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, zero_one_loss
import numpy as np
from PyQt4.Qt import QStringList

class PostProcess(object):
    
    def __init__(self):
        pass
    
    def getMetrics(self, tipo, y_test, X_test):
        x = QStringList()
        listUnique = list()
        for i in X_test:
            if not listUnique.__contains__(i):
                listUnique.append(i)
        listOrderClass = sorted(listUnique)
        if tipo == 'accuracy_score':
            x.append('       accuracy_score         ')
            m = accuracy_score(np.argmax(y_test, axis=-1), X_test)
            x.append(str(m))
            return x
        elif tipo == 'confusion_matrix':
            x.append('       confusion_matrix         ')
            m = confusion_matrix(np.argmax(y_test, axis=-1), X_test)
            #for i in m:
            #    x.append(str(i))
            for i in xrange(0, len(listOrderClass)):
                x.append('Clase:   ' + str(listOrderClass.__getitem__(i)) + '   '  +str(m.__getitem__(i)))
            return x
        elif tipo == 'Precision Score':
            m = list()
            x.append('       precision_score         ')
            m = precision_score(np.argmax(y_test, axis=-1), X_test, average = None)
            for i in xrange(0, len(listOrderClass)):
                #print str(listOrderClass.__getitem__(i))
                x.append('Clase:   ' + str(listOrderClass.__getitem__(i)) + '     valor de precision   ' + str(m.__getitem__(i)))
            return x
        elif tipo == 'Recall_score':
            x.append('       recall_score         ')
            m = recall_score(np.argmax(y_test, axis=-1), X_test, average=None)
            for i in xrange(0, len(listOrderClass)):
                x.append('Clase: ' + str(listOrderClass.__getitem__(i)) + '    muestras positivas    ' + str(m.__getitem__(i)))
            return x
        elif tipo == 'zero_one_loss':
            x.append('       zero_one_loss         ')
            m = zero_one_loss(np.argmax(y_test, axis=-1), X_test)
            x.append(str(m))
            return x
        