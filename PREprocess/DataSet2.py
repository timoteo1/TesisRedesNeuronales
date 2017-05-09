from AbstractDataSet import AbstractDataSet
from keras.preprocessing.text import text_to_word_sequence, base_filter
from keras.preprocessing.text import text_to_word_sequence

class DataSet2(AbstractDataSet):

    def __init__(self):pass
    
    def readDataSet(self): 
        """" OBTENGO EL DATASET, Y LO ALMACENO COMO UNA LISTA DE LISTA"""
        lenMin = -1
        y = list()
        x = list()
        clases = {}
        contador = 0
        try:
            fdata = open('C:\\Tesis\\DataSet\\magazines\\all.review', 'rb')
            l = list()
            for l in fdata:
                l = l.strip()
                if l == '<review>':
                    rating = None
                    r = list()
                    obtener_rating = False
                    obtener_texto = False
                elif l == '<rating>':
                    obtener_rating = True
                elif l == '</rating>':
                    obtener_rating = False
                elif l == '<review_text>':
                    obtener_texto = True
                elif l == '</review_text>':
                    obtener_texto = False
                elif l == '</review>':
                    if len(r) > 0 and rating is not None:
                        if lenMin == -1:
                            lenMin = len(r)
                        elif lenMin > len(r):
                            lenMin = len(r)
                        x.append(r)
                        y.append(rating)
                else:
                    if obtener_rating:
                        rating = int(float(l))
                        if not clases.__contains__(rating):
                            clases[rating] = contador
                            rating = contador
                            contador = contador + 1
                        else:
                            rating = clases[rating]
                    elif obtener_texto: 
                        l = l.split(' ')
                        l = text_to_word_sequence(str(l), filters = base_filter() + "'" + "'")
                        for m in l:
                            r.append(m)
            fdata.close()
        except Exception, e:
            print e 
        """ y = lista de clases
            x = lista de oraciones
            lenMin = longitud minima de todas las secuencias"""
        
        return x,y, clases, lenMin, contador 
                    
                
                