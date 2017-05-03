from PREprocess.PreProcess import PreProcess
from Process.Process import Process
from POSTprocess.PostProcess import PostProcess
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
        self.ui.comboBoxReturnSequencesLSTM.setEnabled(False)
        self.ui.comboBoxRate.setEnabled(False)
        self.ui.pushButtonAddMet.setEnabled(False)
        self.ui.pushButtonResultados.setEnabled(False)
        self.X_resampled = 0
        self.y_resampled = 0
        self.X_trainSplit = 0
        self.y_trainSplit = 0
        self.X_testSplit = 0
        self.y_testSplit = 0
        self.preproceso = PreProcess()
        self.proceso = Process()
        self.postproceso = PostProcess()
        self.capas = 0
        self.ultimaCapa = 0
        self.predictModel = list()
        self.predictClass = list()
        self.listaMetricas = list()
        """ Mostrar Balanceo de dataSetOriginal """
        QtCore.QObject.connect(self.ui.pushButtonViewBalance, QtCore.SIGNAL('clicked()'), self.mostrarBalanceo)
        QtCore.QObject.connect(self.ui.pushButtonPreproceso, QtCore.SIGNAL('clicked()'), self.preProcesarModelo)
        QtCore.QObject.connect(self.ui.pushButtonAddCapa, QtCore.SIGNAL('clicked()'), self.agregarCapa)
        QtCore.QObject.connect(self.ui.pushButtonProceso, QtCore.SIGNAL('clicked()'), self.correrModelo)
        QtCore.QObject.connect(self.ui.comboBoxTipoSplit, QtCore.SIGNAL('currentIndexChanged(const QString&)'), self.deshabilitarTest)
        QtCore.QObject.connect(self.ui.comboBoxTipoCapa, QtCore.SIGNAL('currentIndexChanged(const QString&)'), self.deshabilitarReturnSequences)
        QtCore.QObject.connect(self.ui.pushButtonAddMet, QtCore.SIGNAL('clicked()'), self.almacenarMetricas)
        QtCore.QObject.connect(self.ui.pushButtonResultados, QtCore.SIGNAL('clicked()'), self.mostrarMetricas)
    
    def almacenarMetricas(self):
        self.listaMetricas.append(str(self.ui.comboBoxTipoMetrica.currentText()))
    
    def mostrarMetricas(self):
        x = QStringList
        #for i in self.listaMetricas:
            #print i
        if self.ui.comboBoxTipoSplit.currentText() == 'TrainTest':
            #print self.y_test
            #print self.predictClass
            #x = self.postproceso.getMetrics(i, self.y_test, self.predictClass)
            x = self.postproceso.getMetrics(self.ui.comboBoxTipoMetrica.currentText(), self.y_test, self.predictClass)
        else:
            #x = self.postproceso.getMetrics(i, np.array(self.y_test), self.predictClass)
            x = self.postproceso.getMetrics(self.ui.comboBoxTipoMetrica.currentText(), np.array(self.y_test), self.predictClass)
            #x.append(m)
        FormularioResultado(tipo = 'mostrarBalanceo', parametro = x).exec_() 
    
    def mostrarBalanceo(self):
        x = self.preproceso.ViewBalance()
        FormularioResultado(tipo = 'mostrarBalanceo', parametro = x).exec_()        
    
    def deshabilitarTest(self):
        if self.ui.comboBoxTipoSplit.currentText() == 'TrainTest':
            self.ui.comboBoxTest.setEnabled(True)
        else:
            self.ui.comboBoxTest.setEnabled(False)
           
    
    def deshabilitarReturnSequences(self):
        if self.ui.comboBoxTipoCapa.currentText() == 'LSTM':
            self.ui.comboBoxReturnSequencesLSTM.setEnabled(True)
        else:
            self.ui.comboBoxReturnSequencesLSTM.setEnabled(False)
        if self.ui.comboBoxTipoCapa.currentText() == 'Dropout':
            self.ui.comboBoxRate.setEnabled(True)
        else:
            self.ui.comboBoxRate.setEnabled(False)
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
        parametros['return_sequences'] = str(self.ui.comboBoxReturnSequencesLSTM.currentText())
        parametros['input_length'] = int(self.ui.lineEditPadSequence.text())
        parametros['input_dim'] = self.preproceso.lenVocabulary() + 1
        if self.ui.comboBoxTipoCapa.currentText() == 'Embedding':
            parametros['input_length'] = int(self.ui.lineEditPadSequence.text())            
            parametros['input_dim'] = self.preproceso.lenVocabulary() + 1
        self.proceso.addLayer(self.ui.comboBoxTipoCapa.currentText(), parametros)
        """ saco la opcion de agregar la capa Embedding """
        if self.capas == 1: 
            self.ui.comboBoxTipoCapa.removeItem(0)
        elif self.capas >= 2: 
            if self.ultimaCapa != 'Dropout':
                self.ui.pushButtonProceso.setEnabled(True)
                
                  
    def correrModelo(self):
        self.ui.pushButtonAddCapa.setEnabled(False)
        self.ui.pushButtonAddMet.setEnabled(True)
        self.ui.pushButtonResultados.setEnabled(True)
        self.proceso.compilerModel()
        if(self.ui.comboBoxTipoSplit.currentText() == 'K-Fold'):
            self.proceso.save('modelo.hdf')
            for i in xrange(0, 10):
                self.proceso.getModel('modelo.hdf')
                self.X_train, self.y_train, self.X_test, self.y_test = self.preproceso.SpltKfold(self.X_trainSplit[i], self.y_trainSplit[i], self.X_testSplit[i], self.y_testSplit[i], self.X_resampled, self.y_resampled)
                self.y_train, self.y_test = self.preproceso.toCategorical(self.y_train, self.y_test, int(self.ui.lineEditNroClases.text()))
                self.proceso.fitModel(np.array(self.X_train), np.array(self.y_train), int(self.ui.lineEditBatch.text()), int(self.ui.lineEditNB_epoch.text()))
                self.proceso.evaluateModel(np.array(self.X_test), np.array(self.y_test), int(self.ui.lineEditBatch.text()))
                self.predictModel = self.proceso.predictModelKfold(np.array(self.X_test), self.predictModel, i)
                self.predictClass = self.proceso.predictClassModelKfold(np.array(self.X_test), self.predictClass, i)
        else:
            self.y_train, self.y_test = self.preproceso.toCategorical(self.y_trainSplit, self.y_testSplit, int(self.ui.lineEditNroClases.text()))
            self.proceso.fitModel(self.X_trainSplit, np.array(self.y_train), int(self.ui.lineEditBatch.text()), int(self.ui.lineEditNB_epoch.text())) 
            self.proceso.evaluateModel(self.X_testSplit, self.y_test, int(self.ui.lineEditBatch.text()))
            self.predictModel = self.proceso.predictModel(self.X_testSplit)
            self.predictClass = self.proceso.predictClassModel(self.X_testSplit)
        self.ui.pushButtonProceso.setEnabled(False)
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   