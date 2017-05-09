from PREprocess.TrainTest import TrainTest
from PREprocess.Kfold import Kfold
from PREprocess.RandomUS import RandomUS
from PREprocess.RandomOS import RandomOS
from sklearn import preprocessing
from PREprocess.DataSet1 import DataSet1
from PREprocess.DataSet2 import DataSet2
from keras.utils.np_utils import to_categorical
from PyQt4.Qt import QStringList

class PreProcess(object):
    
    def __init__(self):
        pass

    def Constructor(self, tipoDataSet):
        #self.dataSet = self.readFile()    
        #self.dataSet = (['a', 'b', 'd', 'bueno'],['m','n', 'y', 'v', 'o', 'j', 'bueno'],['g','g','h','y','l','malo'],['u','r','y','j','k','regular'],['d','a','s','b','h','bueno'],['g','f','x','j','t','o','p','bueno'],['t','i','m','o','t','e','regular'],['g','o','n','z','a','malo'],['l','e','z','h','o','l','bueno'], ['l','a','l','a','l','regular'],['p','e','p','a','bueno'],['p','i','g','g','regular'],['h','o','l','a','q','u','e','t','bueno'],['a','l','malo'],['s','s','s','bueno'] )
        self.X, self.Y, self.clases, self.lenMin, self.cant_clases = self.openDataSet(tipoDataSet)
        self.vocabulary = self.Getvocabulary()
        self.dataSetInt = self.convertInt()
        #self.ViewBalance()    
    
    def getCant_clases(self):
        return self.cant_clases
    
    def verPruebaBorrarDespues(self):
        #print self.pad_sequences(10)
        print 'clases'
        print self.clases
        print 'lista de clases normalizadas'
        print self.Y
        
        
        
    def lenMinSequence(self):
        return self.lenMin
         
        
    def lenVocabulary(self):
        return len(self.vocabulary)
    
    def Getvocabulary(self):
        voc = {}
        contador = 0
        for i in self.X:
            for m in i:
                if not m in voc:
                    voc[m] = contador
                    contador = contador + 1
        return voc
    
    
    
    def convertInt(self):
        listInt = list()
        for i in self.X:
            aux = list()
            for m in i:
                aux.append(self.vocabulary.get(m))
            listInt.append(aux)
        return listInt
    
    
    
    def pad_sequences(self, leng):
        """ Garantizo que el valor seteado por el usuario sea valido """
        if leng <= 0 or self.lenMin < leng:
            longitud = self.lenMin
        else:
            longitud = leng
        x = list()
        for i in self.dataSetInt:
            m = list()
            m.append(i[:longitud])
            x = x + m
        return x
    
    
    
    def split(self, x, y, tipo, valor):
                
        if tipo == 'TrainTest':
            sp = TrainTest(valor)
            X_train, y_train, X_test, y_test = sp.splitDS(x, y)
        elif tipo == 'K-Fold':
            sp = Kfold()
            X_train, y_train, X_test, y_test = sp.splitDS(x, y)
            
        
        return X_train, y_train, X_test, y_test    
    
        
    """ Retorno el numero de repeticiones de cada una de los label """     
    def ViewBalance(self):
        labelUnique = list()
        x = QStringList()
        for i in self.Y:
            if not labelUnique.__contains__(i):
                labelUnique.append(i)
                #x.append('clase ' + i + ' instancias '+ str(self.Y.count(i)))
                x.append('clase ' + str(i) + ' instancias '+ str(self.Y.count(i)))
        return x
    
    
                
    """ Recibe como entrada la lista con las etiquetas y el dataset ya cortado (pad_sequences)
        Devuelve la matriz de instancias y la lista labels sampleadas
    """ 
    def Sampling(self, dataSetPS, parametro):
   
        if parametro == 'UnderSampling':
            rus = RandomUS()
            x_resampled, y_resampled = rus.doSampling(dataSetPS, self.Y)
        elif parametro == 'OverSampling': 
            ros = RandomOS()
            x_resampled, y_resampled = ros.doSampling(dataSetPS, self.Y)
        return x_resampled, y_resampled
         
    
    def normalize(self, X_train):
    #def normalize(self, X_train, Y_train, X_test, Y_test):
              
        X_train = preprocessing.normalize(X_train)
        #Y_train = preprocessing.normalize(Y_train)
        
        #X_test = preprocessing.normalize(X_test)
        #Y_test = preprocessing.normalize(Y_test)
                
        #return X_train, Y_train, X_test, Y_test
        return X_train
    
    
    def openDataSet(self, tipoDataSet):
        if tipoDataSet == 'Formato 1':
            dataSet1 =DataSet1()
            X, Y, clases, lenMin, cant_clases = dataSet1.readDataSet()
        elif tipoDataSet == 'Formato 2':
            dataSet2 = DataSet2()
            X, Y, clases, lenMin, cant_clases = dataSet2.readDataSet()
        
        return X, Y, clases, lenMin, cant_clases
    
    
    #def toCategorical(self, y_train, y_test, clases):
    def toCategorical(self, y_train, y_test, clases):
        """ Convierte los vectores a una matriz binaria, donde recibe como parametro el numero de clases."""    
        
        y_train = to_categorical(y_train, nb_classes= clases)
        #y_train = to_categorical(y_train)
        y_test = to_categorical(y_test, nb_classes= clases)
        #y_test = to_categorical(y_test)
        
        return y_train, y_test
    
    
    def SpltKfold(self, X_trainSplit, y_trainSplit, X_testSplit, y_testSplit, x_resampled, y_resampled):
        X_train = list()
        y_train = list()
        X_test = list()
        y_test = list()
        
        
        for i in X_trainSplit:
            X_train.append(x_resampled[i])
        for i in y_trainSplit:
            y_train.append(y_resampled[i])
        for i in X_testSplit:
            X_test.append(x_resampled[i]) 
        for i in y_testSplit:
            y_test.append(y_resampled[i])
            
        return X_train, y_train, X_test, y_test
        
   

    """
    def readFile(self):
         OBTENGO EL DATASET, Y LO ALMACENO COMO UNA LISTA DE LISTA
        with open('C:\\Tesis\\DataSet\\magazines\\AssetsImportCompleteSample.csv','rb') as f:
            reader = csv.reader(f)
            x = list(reader)
        return x
    
    """
    
    """ Retorno el numero de repeticiones de cada una de los label     
    def ViewBalance(self):
        print('Nivel de balanceo del dataSet')
        label = list()
        label_unique= list() 
        for x in self.dataSetInt:
            p = len(x)-1
            label.append(x[p])
            if not label_unique.__contains__(x[p]):
                label_unique.append(x[p])
        for i in label_unique:     
            print "label: " + str(i) + " cantidad= " + str(label.count(i))                        
            #x.add([i, label.count(i)])
        return label
    """