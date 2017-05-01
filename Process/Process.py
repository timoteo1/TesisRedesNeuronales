from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM, Dropout
from keras.models import load_model

class Process(object):
        
    def __init__(self):
        self.modelo = Sequential()
        self.contador = 0
        
    """ ETAPA DE CREAR EL MODELO """
    
    def addLayer(self, tipo, parametros):
        if(tipo == 'Embedding'):
            """ La entrada input_dim debe ser seteada con la longitud del vocabulario + 1"""
            #self.modelo.add(Embedding(input_dim = parametros['input_dim'], output_dim= parametros['output'], input_length= parametros['input_length']))
            self.modelo.add(Embedding(parametros['input_dim'], output_dim= parametros['output']))
            self.contador = self.contador + 1
        elif(tipo == 'Dense'): 
            if(self.contador == 0):
                """
                    input_dim = dimension de la entrada
                    activation = nombre de la funcion de activacion
                    init = nombre de la funcion de inicializacion de los pesos de la capa
                """
                self.modelo.add(Dense(parametros['output'], input_dim = parametros['input_dim'], activation=parametros['activation'])) 
            else:
                self.modelo.add(Dense(parametros['output'], activation = parametros['activation']))
               
            self.contador = self.contador + 1
        elif(tipo == 'Dropout'):
            """ Debe existir una capa anterior a la capa de Dropout a agregar"""
            """ rate = float between 0 and 1. Fraction of the input units to drop. """
            if(self.contador > 0):
                self.modelo.add(Dropout(parametros['rate']))
                """ Dropout: flotante entre 0 y 1, fracciones de las unidades de entrada a "apagar" """
        elif(tipo == 'LSTM'):
            if(self.contador == 0):
                self.modelo.add(LSTM(parametros['output'], input_dim = parametros['input_dim']))
            else:
                self.modelo.add(LSTM(parametros['output']))
        print self.modelo.get_config()        
        
    """ ETAPA DE COMPILAR EL MODELO """
    def compilerModel(self):
        self.modelo.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy'])
        
    """ ETAPA DE ENTRENAR EL MODELO """
    
    def fitModel(self, X_train, y_train, batch, epoch):
        
        self.modelo.fit(X_train, y_train, batch_size= batch, nb_epoch= epoch)
        
    """ ETAPA DE EVALUACION DEL MODELO 
    
    Esto generara una prediccion para cada par de entrada y salida y recogera las puntuaciones, 
    incluyendo la perdida promedio y cualquier metrica que haya configurado, como la precision."""
   
    def evaluateModel(self, X_test, y_test, batch):
        return self.modelo.evaluate(X_test, y_test, batch_size= batch)
        
    def predictModel(self, X_test):
        return self.modelo.predict(X_test)
    
    def predictClassModel(self, X_test):
        return self.modelo.predict_classes(X_test)
    
    def save(self, direct):
        self.modelo.save(direct)
        
    def getModel(self, direct):
        self.modelo = load_model('modelo.hdf')
    
    
    def predictModelKfold(self, X_test, lista, fold):
        x = self.modelo.predict(X_test)
        
        if fold > 0 and fold < 9:
            aux = list()
            for i in xrange(len(x)):
                t = lista[i]
                p = x[i]
                m=list()
                for j in xrange(len(p)):
                    m.append(t[j] + p[j])
                aux.append(m)
            return aux
        elif fold == 9:
            aux = list()
            for i in xrange(len(x)):
                t = lista[i]
                p = x[i]
                m=list()
                for j in xrange(len(p)):
                    m.append((t[j] + p[j])/10)
                aux.append(m)
            return aux
        elif fold == 0:
            return x
    
    def predictClassModelKfold(self, X_test, lista, fold):
        x = self.modelo.predict_classes(X_test)
        lista.append(x)
        if fold == 9:
            resultado = list()
            for i in xrange(0, len(lista[0])):
                listUnique = list()
                for aux in lista:
                    print 'longitud  ' + str(len(aux)) + ' posicion ' + str(i)
                    if len(aux) > i:
                        if not listUnique.__contains__(aux[i]):
                            listUnique.append(aux[i])
                valor = -1
                count = -1
                for j in listUnique:
                    cant = listUnique.count(j)
                    if cant > count:
                        valor = j
                        count = cant
                resultado.append(valor)
            return resultado
        return lista
                    
    """ 
    elif(tipo == 'LSTM'):
            if(self.contador == 0):
                self.modelo.add(parametros['output'], input_dim = parametros['input_dim'], input_length = parametros['input_length'], init = parametros['kernel_initializer'],  forget_bias_init = parametros['bias_initializer'], activation = parametros['activation'])
                 return_sequences = True, solo cuando voy a tener una pila de capas recurrentes
            else:
                self.modelo.add(LSTM(output_dim= parametros['output'], init = parametros['kernel_initializer'],  forget_bias_init = parametros['bias_initializer'], activation = parametros['activation']))
                 return_sequences = True, solo cuando voy a tener una pila de capas recurrentes
    """
    