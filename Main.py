from PREprocess.PreProcess import PreProcess
from Process.Process import Process
from POSTprocess.PostProcess import PostProcess
import numpy as np
from Atributo import *
#from Interface.IntefaceUser import *
from Interface.WizardPage1 import *
from Interface.WizardPage2 import *
from Interface.WizardPage3 import *
from Interface.WizardPage4 import *
from Interface.InterfaceResult import * 
import PyQt4
import sys
from sympy.functions.elementary import integers
from PyQt4.Qt import QStringList
from psutil._psutil_windows import proc_cmdline

""" Este modulo esta encargado de tomar los parametros que carga el usuario al sistema, por medio de la interfaz """


      
class FormularioPagina1(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_WizardPage()
        self.ui.setupUi(self) 
        
        self.ui.pushButtonViewBalance.setEnabled(False)
        self.ui.pushButtonPreproceso.setEnabled(False)
        
        
        self.preproceso = PreProcess()
        self.longitud = 0
    
        
        QtCore.QObject.connect(self.ui.pushButtonConfirmarFormato, QtCore.SIGNAL('clicked()'), self.definirFormato)
        QtCore.QObject.connect(self.ui.pushButtonViewBalance, QtCore.SIGNAL('clicked()'), self.mostrarBalanceo)
        QtCore.QObject.connect(self.ui.pushButtonPreproceso, QtCore.SIGNAL('clicked()'), self.preProcesarModelo)
        QtCore.QObject.connect(self.ui.comboBoxTipoSplit, QtCore.SIGNAL('currentIndexChanged(const QString&)'), self.deshabilitarTest)
    
    def deshabilitarTest(self):
        if self.ui.comboBoxTipoSplit.currentText() == 'TrainTest':
            self.ui.comboBoxTest.setEnabled(True)
        else:
            self.ui.comboBoxTest.setEnabled(False)
     
    def definirFormato(self):
        self.ui.pushButtonConfirmarFormato.setEnabled(False)
        formato = self.ui.comboBoxFormatoDataSet.currentText()
        self.preproceso.Constructor(formato)
        self.preproceso.verPruebaBorrarDespues()
        self.ui.pushButtonPreproceso.setEnabled(True)
        self.ui.pushButtonViewBalance.setEnabled(True)
        """  Seteo longitud Maxima de PadSequence """
        self.ui.labelMaxLongitud.setText('La longitud maxima es: ' + str(self.preproceso.lenMinSequence()))

    
    def mostrarBalanceo(self):
        x = self.preproceso.ViewBalance()
        FormularioResultado(tipo = 'mostrarBalanceo', parametro = x).exec_()
        
    def preProcesarModelo(self):
        self.ui.pushButtonPreproceso.setEnabled(False)
        self.ui.pushButtonViewBalance.setEnabled(False)
        dataSetPadSequence = self.preproceso.pad_sequences(int(self.ui.lineEditPadSequence.text()))
        self.X_resampled, self.y_resampled = self.preproceso.Sampling(dataSetPadSequence,  self.ui.comboBoxTipoSampling.currentText())
        self.X_trainSplit, self.y_trainSplit, self.X_testSplit, self.y_testSplit = self.preproceso.split(self.X_resampled, self.y_resampled, self.ui.comboBoxTipoSplit.currentText(), float(self.ui.comboBoxTest.currentText()))
        
        self.atributo = Atributo(self.X_resampled, self.y_resampled, self.X_trainSplit, self.y_trainSplit, self.X_testSplit, self.y_testSplit, self.ui.comboBoxTipoSplit.currentText())
        self.atributo.setCantClases(self.preproceso.getCant_clases())
        print self.preproceso.getCant_clases()
        """ Aca debo llamar a la ventana 2"""
        
        self.atributo.setPad_sequences(int(self.ui.lineEditPadSequence.text()))
        
        self.close()
        formularioPagina2(self.preproceso, self.atributo).exec_()
        
        
        
        #self.ui.pushButtonAddCapa.setEnabled(True)
        
class formularioPagina2(QtGui.QDialog):
    def __init__(self, prep, atr, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_WizardPage2()
        self.ui.setupUi(self) 
        
        self.preproceso = prep
        self.atributo = atr
        self.proceso = Process()
        self.capas = 0
        self.ui.pushButtonNext.setEnabled(False)
        self.ui.comboBoxRate.setEnabled(False)
        self.ui.comboBoxActivation.setEnabled(False)
        self.ui.comboBoxReturnSequencesLSTM.setEnabled(False)
        
        QtCore.QObject.connect(self.ui.comboBoxTipoCapa, QtCore.SIGNAL('currentIndexChanged(const QString&)'), self.deshabilitarReturnSequences)
        QtCore.QObject.connect(self.ui.pushButtonAddCapa, QtCore.SIGNAL('clicked()'), self.agregarCapa)
        QtCore.QObject.connect(self.ui.pushButtonNext, QtCore.SIGNAL('clicked()'), self.siguienteEtapa)
        
    def deshabilitarReturnSequences(self):
        if self.ui.comboBoxTipoCapa.currentText() == 'LSTM':
            self.ui.comboBoxReturnSequencesLSTM.setEnabled(True)
        else:
            self.ui.comboBoxReturnSequencesLSTM.setEnabled(False)
        if self.ui.comboBoxTipoCapa.currentText() == 'Dropout':
            self.ui.comboBoxRate.setEnabled(True)
        else:
            self.ui.comboBoxRate.setEnabled(False)
        if self.ui.comboBoxTipoCapa.currentText() == 'Dense':
            self.ui.comboBoxActivation.setEnabled(True)
        else:
            self.ui.comboBoxActivation.setEnabled(False)
        
        
    def agregarCapa(self):
        """ Acciones para agregar capa a la red"""
        
        self.capas = self.capas + 1
        parametros = {}
        parametros['activation'] = str(self.ui.comboBoxActivation.currentText())
        parametros['output'] =  int(self.ui.lineEditOutputLayer.text())
        parametros['rate'] = float(self.ui.comboBoxRate.currentText())
        parametros['return_sequences'] = str(self.ui.comboBoxReturnSequencesLSTM.currentText())
        #parametros['input_length'] = int(self.ui.lineEditPadSequence.text())
        #parametros['input_dim'] = self.preproceso.lenVocabulary() + 1
        if self.ui.comboBoxTipoCapa.currentText() == 'Embedding':
            parametros['input_length'] = self.atributo.getPad_sequences()            
            parametros['input_dim'] = self.preproceso.lenVocabulary() + 1
        self.proceso.addLayer(self.ui.comboBoxTipoCapa.currentText(), parametros)
        """ saco la opcion de agregar la capa Embedding """
        if self.capas == 1: 
            self.ui.comboBoxTipoCapa.removeItem(0)
            """ Habilito el boton Proceso, solo si tengo dos o mas capas y la ultima capa no es de tipo Dropout """
        elif self.capas >= 2: 
            if self.ui.comboBoxTipoCapa.currentText() != 'Dropout':
                self.ui.pushButtonNext.setEnabled(True)
            else:
                self.ui.pushButtonNext.setEnabled(False)
    
    def siguienteEtapa(self):
        self.close()
        formularioPagina3(self.preproceso, self.proceso, self.atributo).exec_()
        
        
class formularioPagina3(QtGui.QDialog):
    def __init__(self, prep, proc, atr, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_WizardPage3()
        self.ui.setupUi(self)
            
        self.preproceso = prep
        self.proceso = proc
        self.atributo = atr
            
        QtCore.QObject.connect(self.ui.pushButtonProceso, QtCore.SIGNAL('clicked()'), self.procesarModelo)
        
    def procesarModelo(self):
        self.X_trainSplit = self.atributo.getX_trainSplit()
        self.y_trainSplit = self.atributo.gety_trainSplit()
        self.X_testSplit = self.atributo.getX_testSplit()
        self.y_testSplit = self.atributo.gety_testSplit()
        self.X_resampled = self.atributo.getX_resampled()
        self.y_resampled = self.atributo.getY_resampled()
        self.proceso.compilerModel(str(self.ui.comboBoxCompilerOptimizer.currentText()), str(self.ui.comboBoxCompilerLoss.currentText()), str(self.ui.comboBoxCompilerMetrics.currentText()))
        if(self.atributo.get_TipoSplit() == 'K-Fold'):
            self.proceso.save('modelo.hdf')
            self.predictModel = list()
            self.predictClass = list()
            for i in xrange(0, 10):
                self.proceso.getModel('modelo.hdf')
                self.X_train, self.y_train, self.X_test, self.y_test = self.preproceso.SpltKfold(self.X_trainSplit[i], self.y_trainSplit[i], self.X_testSplit[i], self.y_testSplit[i], self.X_resampled, self.y_resampled)
                self.y_train, self.y_test = self.preproceso.toCategorical(self.y_train, self.y_test, self.atributo.getCantClases())
                self.proceso.fitModel(np.array(self.X_train), np.array(self.y_train), int(self.ui.lineEditBatch.text()), int(self.ui.lineEditNB_epoch.text()))
                self.proceso.evaluateModel(np.array(self.X_test), self.y_test, int(self.ui.lineEditBatch.text()))
                self.predictModel = self.proceso.predictModelKfold(np.array(self.X_test), self.predictModel, i)
                self.predictClass = self.proceso.predictClassModelKfold(np.array(self.X_test), self.predictClass, i)
                print 'K-fold'
        else:
            self.y_train, self.y_test = self.preproceso.toCategorical(self.y_trainSplit, self.y_testSplit, self.atributo.getCantClases())
            self.proceso.fitModel(self.X_trainSplit, np.array(self.y_train), int(self.ui.lineEditBatch.text()), int(self.ui.lineEditNB_epoch.text())) 
            self.proceso.evaluateModel(self.X_testSplit, self.y_test, int(self.ui.lineEditBatch.text()))
            self.predictModel = self.proceso.predictModel(self.X_testSplit)
            self.predictClass = self.proceso.predictClassModel(self.X_testSplit)
        self.atributo.setPredictClass(self.predictClass)
        self.atributo.setY_test(self.y_test)
        self.close()
        formularioPagina4(self.atributo).exec_()

class formularioPagina4(QtGui.QDialog):
    def __init__(self, atr, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_WizardPage4()
        self.ui.setupUi(self)
        
        self.atributo = atr
        self.postproceso = PostProcess()
        QtCore.QObject.connect(self.ui.pushButtonResultados, QtCore.SIGNAL('clicked()'), self.mostrarMetricas)
        
    def mostrarMetricas(self):
        x = QStringList
        #for i in self.listaMetricas:
            #print i
            
        self.y_test = self.atributo.getY_test()
        self.predictClass = self.atributo.getPredictClass()
        #if self.ui.comboBoxTipoSplit.currentText() == 'TrainTest':
        if self.atributo.get_TipoSplit() == 'TrainTest':
            #print self.y_test
            #print self.predictClass
            #x = self.postproceso.getMetrics(i, self.y_test, self.predictClass)
            x = self.postproceso.getMetrics(self.ui.comboBoxTipoMetrica.currentText(), self.y_test, self.predictClass)
        else:
            #x = self.postproceso.getMetrics(i, np.array(self.y_test), self.predictClass)
            x = self.postproceso.getMetrics(self.ui.comboBoxTipoMetrica.currentText(), np.array(self.y_test), self.predictClass)
            #x.append(m)
        self.close()
        FormularioResultado(tipo = 'mostrarBalanceo', parametro = x).exec_()
         
        
""" -----------------/////////////////////////////////------------------------------------/////////////////////////////////////--------------- """

class FormularioPrincipal(QtGui.QDialog):
    
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        #self.ui = Ui_Wizard()
        self.ui.setupUi(self)        
        
        self.preproceso = PreProcess()
        self.proceso = Process()
        self.postproceso = PostProcess()
       
        """  Deshabilitar botones posteriores setear Formato  """
        self.ui.pushButtonViewBalance.setEnabled(False)
        self.ui.pushButtonPreproceso.setEnabled(False)
        self.ui.pushButtonAddCapa.setEnabled(False)
        self.ui.pushButtonProceso.setEnabled(False)
        self.ui.pushButtonResultados.setEnabled(False)
        self.ui.comboBoxReturnSequencesLSTM.setEnabled(False)
        self.ui.comboBoxRate.setEnabled(False)
        self.ui.comboBoxActivation.setEnabled(False)
        #self.ui.pushButtonAddMet.setEnabled(False)
        self.ui.pushButtonResultados.setEnabled(False)
        self.X_resampled = 0
        self.y_resampled = 0
        self.X_trainSplit = 0
        self.y_trainSplit = 0
        self.X_testSplit = 0
        self.y_testSplit = 0
        
        self.capas = 0
        self.ultimaCapa = 0
        self.predictModel = list()
        self.predictClass = list()
        #self.listaMetricas = list()
        """ Mostrar Balanceo de dataSetOriginal """
        QtCore.QObject.connect(self.ui.pushButtonConfirmarFormato, QtCore.SIGNAL('clicked()'), self.definirFormato)
        QtCore.QObject.connect(self.ui.pushButtonViewBalance, QtCore.SIGNAL('clicked()'), self.mostrarBalanceo)
        QtCore.QObject.connect(self.ui.pushButtonPreproceso, QtCore.SIGNAL('clicked()'), self.preProcesarModelo)
        QtCore.QObject.connect(self.ui.pushButtonAddCapa, QtCore.SIGNAL('clicked()'), self.agregarCapa)
        QtCore.QObject.connect(self.ui.pushButtonProceso, QtCore.SIGNAL('clicked()'), self.correrModelo)
        QtCore.QObject.connect(self.ui.comboBoxTipoSplit, QtCore.SIGNAL('currentIndexChanged(const QString&)'), self.deshabilitarTest)
        QtCore.QObject.connect(self.ui.comboBoxTipoCapa, QtCore.SIGNAL('currentIndexChanged(const QString&)'), self.deshabilitarReturnSequences)
        #QtCore.QObject.connect(self.ui.pushButtonAddMet, QtCore.SIGNAL('clicked()'), self.almacenarMetricas)
        QtCore.QObject.connect(self.ui.pushButtonResultados, QtCore.SIGNAL('clicked()'), self.mostrarMetricas)
    
    """
    def almacenarMetricas(self):
        self.listaMetricas.append(str(self.ui.comboBoxTipoMetrica.currentText()))
    """
    
    def definirFormato(self):
        self.ui.pushButtonConfirmarFormato.setEnabled(False)
        formato = self.ui.comboBoxFormatoDataSet.currentText()
        self.preproceso.Constructor(formato)
        self.preproceso.verPruebaBorrarDespues()
        self.ui.pushButtonPreproceso.setEnabled(True)
        self.ui.pushButtonViewBalance.setEnabled(True)
        """  Seteo longitu Maxima de PadSequence """
        self.ui.labelMaxLongitud.setText('La longitud maxima es: ' + str(self.preproceso.lenMinSequence()))
        
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
        if self.ui.comboBoxTipoCapa.currentText() == 'Dense':
            self.ui.comboBoxActivation.setEnabled(True)
        else:
            self.ui.comboBoxActivation.setEnabled(False)
                  
    def preProcesarModelo(self):
        self.ui.pushButtonPreproceso.setEnabled(False)
        self.ui.pushButtonViewBalance.setEnabled(False)
        dataSetPadSequence = self.preproceso.pad_sequences(int(self.ui.lineEditPadSequence.text()))
        self.X_resampled, self.y_resampled = self.preproceso.Sampling(dataSetPadSequence,  self.ui.comboBoxTipoSampling.currentText())
        self.X_trainSplit, self.y_trainSplit, self.X_testSplit, self.y_testSplit = self.preproceso.split(self.X_resampled, self.y_resampled, self.ui.comboBoxTipoSplit.currentText(), float(self.ui.comboBoxTest.currentText()))
        self.ui.pushButtonAddCapa.setEnabled(True)
        
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
            """ Habilito el boton Proceso, solo si tengo dos o mas capas y la ultima capa no es de tipo Dropout """
        elif self.capas >= 2: 
            if self.ui.comboBoxTipoCapa.currentText() != 'Dropout':
                self.ui.pushButtonProceso.setEnabled(True)
            else:
                self.ui.pushButtonProceso.setEnabled(False)
               
                  
    def correrModelo(self):
        self.ui.pushButtonAddCapa.setEnabled(False)
        #self.ui.pushButtonAddMet.setEnabled(True)
        self.ui.pushButtonResultados.setEnabled(True)
        self.proceso.compilerModel()
        if(self.ui.comboBoxTipoSplit.currentText() == 'K-Fold'):
            self.proceso.save('modelo.hdf')
            for i in xrange(0, 10):
                self.proceso.getModel('modelo.hdf')
                self.X_train, self.y_train, self.X_test, self.y_test = self.preproceso.SpltKfold(self.X_trainSplit[i], self.y_trainSplit[i], self.X_testSplit[i], self.y_testSplit[i], self.X_resampled, self.y_resampled)
                self.y_train = self.preproceso.normalize(self.y_train)
                self.y_test = self.preproceso.normalize(self.y_test)
                self.y_train, self.y_test = self.preproceso.toCategorical(self.y_train, self.y_test, int(self.ui.lineEditNroClases.text()))
                self.proceso.fitModel(np.array(self.X_train), np.array(self.y_train), int(self.ui.lineEditBatch.text()), int(self.ui.lineEditNB_epoch.text()))
                self.proceso.evaluateModel(np.array(self.X_test), np.array(self.y_test), int(self.ui.lineEditBatch.text()))
                self.predictModel = self.proceso.predictModelKfold(np.array(self.X_test), self.predictModel, i)
                self.predictClass = self.proceso.predictClassModelKfold(np.array(self.X_test), self.predictClass, i)
        else:
            #self.y_trainSplit = self.preproceso.normalize(self.y_trainSplit)
            #self.y_testSplit = self.preproceso.normalize(self.y_testSplit)
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
    
    myapp = FormularioPagina1()
    myapp.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   