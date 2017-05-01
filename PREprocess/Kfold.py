from AbstractSplit import AbstractSplit
from sklearn.model_selection import KFold

class Kfold(AbstractSplit):

    
        
    def splitDS(self, X, y):   
        
        """ El dataSet se divide en 10 partes (SIEMPRE QUE EL NUMERO DE MUESTRAS ES >= 10, SINO ES IGUAL AL NUMERO DE MUESTRAS), 10-fold """
        """ Devuelve lista de lista con los numeros de instancias a obtener en cada epoch"""
        
        if len(X) >= 10: 
            kf = KFold(n_splits=10)
        else:
            kf = KFold(n_splits=len(X))
        X_train = list()
        X_test = list()
        y_train = list()
        y_test = list()
        for train_index, test_index in kf.split(X):
            
            X_train.append(train_index)
            y_train.append(train_index)
            X_test.append(test_index)
            y_test.append(test_index)
    
        return X_train, y_train, X_test, y_test
        
        """"
        print X_train
        print X_test
        print y_train
        print y_test"""
        
        
        
        """
        testFinal = list()
        trainingFinal = list()
        rs = ShuffleSplit(n_splits=10, test_size=.25, random_state=0)
        rs.get_n_splits(self.dataset)
        for train_index, test_index in rs.split(self.dataset):
            test = list()
            training = list()
            for m in train_index:
                training.append(m)
            trainingFinal.append(training)
                #training.append(np.asarray(self.dataset[m]))
            for n in test_index:    
                #test.append(np.asarray(self.dataset[n]))
                test.append(n)
            testFinal.append(test)
        print(trainingFinal)
        print(testFinal)
        """