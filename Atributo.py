'''
Created on 29 mar. 2017

@author: Timoteo
'''

class Atributo(object):
   

    def __init__(self, atributo, valor):
        self.atributo = atributo
        self.valor = valor
        
    def getAtributo(self):
        return self.atributo
    
    def getValor(self):
        return self.valor