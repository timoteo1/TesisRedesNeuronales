from AbstractDataSet import AbstractDataSet
from keras.preprocessing.text import text_to_word_sequence, base_filter
import csv

class DataSet1(AbstractDataSet):
    
    def __init__(self):pass
    
    def readDataSet(self):
        """" OBTENGO EL DATASET, Y LO ALMACENO COMO UNA LISTA DE LISTA"""
        lenMin = -1
        y = list()
        x = list()
        f = open('C:\\Tesis\\DataSet\\TesisParalelo\\train.csv','rb')
        reader = csv.reader(f)
        for reg in reader:
            y.append(reg[0])
            z = list()
            r = list()
            r.append(reg[2])
            z.append(reg[3])
            r = text_to_word_sequence(str(r), filters = base_filter() + "'" + "'")
            z = text_to_word_sequence(str(z), filters = base_filter() + "'" + "'")
            for i in z:
                r.append(i) 
            x.append(r)
            if lenMin == -1:
                lenMin = len(r)
            elif lenMin > len(r):
                lenMin = len(r) 
        f.close()
        
        contador = 0
        clases = {}
        yfinal = list()
        for i in y:
            if not clases.__contains__(i):
                yfinal.append(contador)
                clases[i] = contador
                contador = contador + 1
            else:
                yfinal.append(clases[i])
        
        """ y = lista de clases
            x = lista de oraciones
            lenMin = longitud minima de todas las secuencias"""
        return x, yfinal, clases, lenMin, contador      