from PREprocess.PreProcess import PreProcess
from Process.Process import Process
import numpy as np
from Interface.IntefaceUser import *
from Interface.InterfaceResult import * 
import PyQt4
import sys
from sympy.functions.elementary import integers
from PyQt4.Qt import QStringList

""" Este modulo esta encargado de tomar los parametros que carga el usuario al sistema, por medio de la interfaz """

class FormularioPrincipal(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogUsuario()
        self.ui.setupUi(self)
        """  Deshabilitar botones posteriores al preproceso  """
        self.ui.pushButtonAddCapa.setEnabled(False)
        self.ui.pushButtonProceso.setEnabled(False)
        self.ui.pushButtonResultados.setEnabled(False)
        #self.ui.pushButtonAddCapa.setEnabled(False)
        #self.ui.pushButtonProceso.setEnabled(False)
        #self.ui.pushButtonProceso_2.setEnabled(False)
        
        self.X_resampled = 0
        self.y_resampled = 0
        self.X_trainSplit = 0
        self.y_trainSplit = 0
        self.X_testSplit = 0
        self.y_testSplit = 0
        self.preproceso = PreProcess()
        self.proceso = Process()
        self.capas = 0
        self.ultimaCapa = 0
        self.predictModel = list()
        self.predictClass = list()
        """ Mostrar Balanceo de dataSetOriginal """
        QtCore.QObject.connect(self.ui.pushButtonViewBalance, QtCore.SIGNAL('clicked()'), self.mostrarBalanceo)
        QtCore.QObject.connect(self.ui.pushButtonPreproceso, QtCore.SIGNAL('clicked()'), self.preProcesarModelo)
        QtCore.QObject.connect(self.ui.pushButtonAddCapa, QtCore.SIGNAL('clicked()'), self.agregarCapa)
        QtCore.QObject.connect(self.ui.pushButtonProceso, QtCore.SIGNAL('clicked()'), self.correrModelo)
    
    def mostrarBalanceo(self):
        x = self.preproceso.ViewBalance()
        FormularioResultado(tipo = 'mostrarBalanceo', parametro = x).exec_()        
    
    def preProcesarModelo(self):
        dataSetPadSequence = self.preproceso.pad_sequences(int(self.ui.lineEditPadSequence.text()))
        self.X_resampled, self.y_resampled = self.preproceso.Sampling(dataSetPadSequence,  self.ui.comboBoxTipoSampling.currentText())
        self.X_trainSplit, self.y_trainSplit, self.X_testSplit, self.y_testSplit = self.preproceso.split(self.X_resampled, self.y_resampled, self.ui.comboBoxTipoSplit.currentText(), float(self.ui.comboBoxTest.currentText()))
        self.ui.pushButtonAddCapa.setEnabled(True)
        self.ui.pushButtonPreproceso.setEnabled(False)
        self.ui.pushButtonViewBalance.setEnabled(False)
        
    def agregarCapa(self):
        """ Acciones para agregar capa a la red"""
        self.capas = self.capas + 1
        parametros = {}
        parametros['activation'] = str(self.ui.comboBoxActivation.currentText())
        parametros['output'] =  int(self.ui.lineEditOutputLayer.text())
        parametros['rate'] = float(self.ui.comboBoxRate.currentText())
        if self.ui.comboBoxTipoCapa.currentText() == 'Embedding':
            parametros['input_length'] = int(self.ui.lineEditPadSequence.text())            
            parametros['input_dim'] = len(self.X_trainSplit[0])
        self.proceso.addLayer(self.ui.comboBoxTipoCapa.currentText(), parametros)
        """ saco la opcion de agregar la capa Embedding """
        if self.capas == 1: 
            self.ui.comboBoxTipoCapa.removeItem(0)
        elif self.capas >= 2: 
            if self.ultimaCapa != 'Dropout':
                self.ui.pushButtonProceso.setEnabled(True)
                
                  
    def correrModelo(self):
        self.proceso.compilerModel()
        if(self.ui.comboBoxTipoSplit.currentText() == 'K-Fold'):
            self.proceso.save('modelo.hdf')
            for i in xrange(0, 10):
                self.proceso.getModel('modelo.hdf')
                print 'Timoteo'
                print i
                self.X_train, self.y_train, self.X_test, self.y_test = self.preproceso.SpltKfold(self.X_trainSplit[i], self.y_trainSplit[i], self.X_testSplit[i], self.y_testSplit[i], self.X_resampled, self.y_resampled)
                print 'Timoteo 1'
                self.y_train, self.y_test = self.preproceso.toCategorical(self.y_train, self.y_test, int(self.ui.lineEditNroClases.text()))
                print 'Timoteo 2'
                print len(self.X_train)
                self.proceso.fitModel(np.array(self.X_train), np.array(self.y_train), int(self.ui.lineEditBatch.text()), int(self.ui.lineEditNB_epoch.text()))
                print 'Timoteo 3'
                self.proceso.evaluateModel(self.X_test, self.y_test, int(self.ui.lineEditBatch.text()))
                print 'Timoteo 4' 
                self.predictModel = self.proceso.predictModelKfold(self.X_test, self.predictModel, i)
                print 'Timoteo 5'
        else:
            self.y_trainSplit, self.y_testSplit = self.preproceso.toCategorical(self.y_trainSplit, self.y_testSplit, int(self.ui.lineEditNroClases.text()))
            self.proceso.fitModel(self.X_trainSplit, self.y_trainSplit, int(self.ui.lineEditBatch.text()), int(self.ui.lineEditNB_epoch.text())) 
            self.proceso.evaluateModel(self.X_testSplit, self.y_testSplit, int(self.ui.lineEditBatch.text()))
            self.predictModel = self.proceso.predictModel(self.X_testSplit)
            self.predictClass = self.proceso.predictClassModel(self.X_testSplit)
              
    def preProcesoTesteo(self):
        """ Los metodos de preproceso funcionan todos """
        dataSetPadSequence = self.preproceso.pad_sequences(int(self.ui.lineEditPadSequence.text()))
        X_resampled, y_resampled = self.preproceso.Sampling(dataSetPadSequence,  self.ui.comboBoxTipoSampling.currentText())
        X_trainSplit, y_trainSplit, X_testSplit, y_testSplit = self.preproceso.split(X_resampled, y_resampled, self.ui.comboBoxTipoSplit.currentText(), float(self.ui.comboBoxTipoSplit_2.currentText()))
        self.proceso.compilerModel()
        predictModel = list()
        predictClass = list()
        if(self.ui.comboBoxTipoSplit.currentText() == 'K-Fold'):
            self.proceso.save('modelo.hdf')
            for i in xrange(0, 10):
                self.proceso.getModel('modelo.hdf')
                X_train, y_train, X_test, y_test = self.preproceso.SpltKfold(X_trainSplit[i], y_trainSplit[i], X_testSplit[i], y_testSplit[i], X_resampled, y_resampled)
                y_train, y_test = self.preproceso.toCategorical(y_train, y_test, int(self.ui.lineEditNroClases.text()))
                self.proceso.fitModel(X_train, y_train, int(self.ui.lineEditBatch.text()), int(self.ui.lineEditNB_epoch.text()))
                self.proceso.evaluateModel(X_test, y_test, int(self.ui.lineEditBatch.text()))
                predictModel = self.proceso.predictModelKfold(X_test, predictModel, i)
                predictClass = self.proceso.predictClassModelKfold(X_test, predictClass, i)
        else:
            y_trainSplit, y_testSplit = self.preproceso.toCategorical(y_trainSplit, y_testSplit, int(self.ui.lineEditNroClases.text()))
            self.proceso.fitModel(np.array(X_trainSplit), np.array(y_trainSplit), int(self.ui.lineEditBatch.text()), int(self.ui.lineEditNB_epoch.text())) 
            self.proceso.evaluateModel(X_testSplit, y_testSplit, int(self.ui.lineEditBatch.text()))
            predictModel = self.proceso.predictModel(X_testSplit)
            predictClass = self.proceso.predictClassModel(X_testSplit)
            
    
    
    def procesarRed(self):
        
        
        split = self.ui.comboBoxTipoSplit.currentText()
        dataSetPadSequence = self.preproceso.pad_sequences(int(self.ui.lineEditPadSequence.text()))
        x_resampled, y_resampled = self.preproceso.Sampling(dataSetPadSequence, self.ui.comboBoxTipoSampling.currentText())
        X_trainSplit, y_trainSplit, X_testSplit, y_testSplit = self.preproceso.split(x_resampled, y_resampled, split, self.ui.comboBoxTipoSplit_2.currentText())
        self.proceso.compilerModel()
        predictModel = list()
        predictClass = list()
        if(split == 'K-Fold'):
            self.proceso.save('modelo.hdf')
            for i in xrange(0, 10):
                
                self.proceso.getModel('modelo.hdf')
                
                X_train, y_train, X_test, y_test = self.preproceso.SpltKfold(X_trainSplit[i], y_trainSplit[i], X_testSplit[i], y_testSplit[i], x_resampled, y_resampled)
                        
                y_train, y_test = self.preproceso.toCategorical(y_train, y_test, self.ui.lineEditNroClases.text())
            
                X_train, y_train, X_test, y_test = self.preproceso.normalize(X_train, y_train, X_test, y_test)
            
                self.proceso.fitModel(X_train, y_train, self.ui.lineEditBatch.text(), self.ui.lineEditNB_epoch.text()) 
            
                self.proceso.evaluateModel(X_test, y_test, self.ui.lineEditBatch.text())
                
                predictModel = self.proceso.predictModelKfold(X_test[0:2], predictModel, i)
                
                predictClass = self.proceso.predictClassModelKfold(X_test, predictClass, i)
        else:
            
            y_trainSplit, y_testSplit = self.preproceso.toCategorical(y_trainSplit, y_testSplit, self.ui.lineEditNroClases.text())
            #y_trainSplit, y_testSplit = preproceso.toCategorical(y_trainSplit, y_testSplit)    
        
            X_train, y_train, X_test, y_test = self.preproceso.normalize(X_trainSplit, y_trainSplit, X_testSplit, y_testSplit)
            
            self.proceso.fitModel(X_train, y_train, self.ui.lineEditBatch.text(), self.ui.lineEditNB_epoch.text()) 
        
            self.proceso.evaluateModel(X_test, y_test, self.ui.lineEditBatch.text())
            
            self.proceso.predictModel(X_test)
        
            self.proceso.predictClassModel(X_test)
        
        
                        
class FormularioResultado(QtGui.QDialog):
    def __init__(self, tipo, parametro = None, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogResultados()
        self.ui.setupUi(self)
        if tipo == 'mostrarBalanceo':
            self.mostrarBalanceo(parametro)
          
            
    def mostrarBalanceo(self, lista):
        model = QtGui.QStringListModel(lista)
        self.ui.listViewResultados.setModel(model)
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = FormularioPrincipal()
    myapp.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   