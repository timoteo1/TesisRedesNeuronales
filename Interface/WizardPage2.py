# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WPruebaUser2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WizardPage2(object):
    def setupUi(self, WizardPage2):
        WizardPage2.setObjectName(_fromUtf8("WizardPage2"))
        WizardPage2.resize(480, 308)
        self.labelReturnSequences = QtGui.QLabel(WizardPage2)
        self.labelReturnSequences.setGeometry(QtCore.QRect(10, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelReturnSequences.setFont(font)
        self.labelReturnSequences.setObjectName(_fromUtf8("labelReturnSequences"))
        self.comboBoxRate = QtGui.QComboBox(WizardPage2)
        self.comboBoxRate.setGeometry(QtCore.QRect(380, 80, 71, 22))
        self.comboBoxRate.setObjectName(_fromUtf8("comboBoxRate"))
        self.comboBoxRate.addItem(_fromUtf8(""))
        self.comboBoxRate.addItem(_fromUtf8(""))
        self.comboBoxRate.addItem(_fromUtf8(""))
        self.comboBoxRate.addItem(_fromUtf8(""))
        self.comboBoxRate.addItem(_fromUtf8(""))
        self.comboBoxRate.addItem(_fromUtf8(""))
        self.comboBoxRate.addItem(_fromUtf8(""))
        self.comboBoxRate.addItem(_fromUtf8(""))
        self.comboBoxRate.addItem(_fromUtf8(""))
        self.comboBoxActivation = QtGui.QComboBox(WizardPage2)
        self.comboBoxActivation.setGeometry(QtCore.QRect(140, 120, 151, 22))
        self.comboBoxActivation.setObjectName(_fromUtf8("comboBoxActivation"))
        self.comboBoxActivation.addItem(_fromUtf8(""))
        self.comboBoxActivation.addItem(_fromUtf8(""))
        self.comboBoxActivation.addItem(_fromUtf8(""))
        self.comboBoxActivation.addItem(_fromUtf8(""))
        self.comboBoxActivation.addItem(_fromUtf8(""))
        self.comboBoxActivation.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(WizardPage2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.labelActivation = QtGui.QLabel(WizardPage2)
        self.labelActivation.setGeometry(QtCore.QRect(10, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelActivation.setFont(font)
        self.labelActivation.setObjectName(_fromUtf8("labelActivation"))
        self.labelRate = QtGui.QLabel(WizardPage2)
        self.labelRate.setGeometry(QtCore.QRect(330, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.labelRate.setFont(font)
        self.labelRate.setObjectName(_fromUtf8("labelRate"))
        self.labelOutputLayer = QtGui.QLabel(WizardPage2)
        self.labelOutputLayer.setGeometry(QtCore.QRect(10, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelOutputLayer.setFont(font)
        self.labelOutputLayer.setObjectName(_fromUtf8("labelOutputLayer"))
        self.pushButtonAddCapa = QtGui.QPushButton(WizardPage2)
        self.pushButtonAddCapa.setGeometry(QtCore.QRect(320, 230, 131, 23))
        self.pushButtonAddCapa.setObjectName(_fromUtf8("pushButtonAddCapa"))
        self.labelTipoCapa = QtGui.QLabel(WizardPage2)
        self.labelTipoCapa.setGeometry(QtCore.QRect(10, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelTipoCapa.setFont(font)
        self.labelTipoCapa.setObjectName(_fromUtf8("labelTipoCapa"))
        self.comboBoxReturnSequencesLSTM = QtGui.QComboBox(WizardPage2)
        self.comboBoxReturnSequencesLSTM.setGeometry(QtCore.QRect(140, 200, 71, 22))
        self.comboBoxReturnSequencesLSTM.setObjectName(_fromUtf8("comboBoxReturnSequencesLSTM"))
        self.comboBoxReturnSequencesLSTM.addItem(_fromUtf8(""))
        self.comboBoxReturnSequencesLSTM.addItem(_fromUtf8(""))
        self.lineEditOutputLayer = QtGui.QLineEdit(WizardPage2)
        self.lineEditOutputLayer.setGeometry(QtCore.QRect(140, 160, 61, 21))
        self.lineEditOutputLayer.setObjectName(_fromUtf8("lineEditOutputLayer"))
        self.comboBoxTipoCapa = QtGui.QComboBox(WizardPage2)
        self.comboBoxTipoCapa.setGeometry(QtCore.QRect(140, 80, 151, 22))
        self.comboBoxTipoCapa.setObjectName(_fromUtf8("comboBoxTipoCapa"))
        self.comboBoxTipoCapa.addItem(_fromUtf8(""))
        self.comboBoxTipoCapa.addItem(_fromUtf8(""))
        self.comboBoxTipoCapa.addItem(_fromUtf8(""))
        self.comboBoxTipoCapa.addItem(_fromUtf8(""))
        self.pushButtonNext_2 = QtGui.QPushButton(WizardPage2)
        self.pushButtonNext_2.setGeometry(QtCore.QRect(320, 270, 131, 23))
        self.pushButtonNext_2.setObjectName(_fromUtf8("pushButtonNext_2"))
        self.pushButtonArchivo = QtGui.QPushButton(WizardPage2)
        self.pushButtonArchivo.setGeometry(QtCore.QRect(90, 250, 161, 23))
        self.pushButtonArchivo.setObjectName(_fromUtf8("pushButtonArchivo"))
        self.pushButtonVerRed = QtGui.QPushButton(WizardPage2)
        self.pushButtonVerRed.setGeometry(QtCore.QRect(320, 30, 131, 21))
        self.pushButtonVerRed.setObjectName(_fromUtf8("pushButtonVerRed"))

        self.retranslateUi(WizardPage2)
        QtCore.QMetaObject.connectSlotsByName(WizardPage2)

    def retranslateUi(self, WizardPage2):
        WizardPage2.setWindowTitle(_translate("WizardPage2", "WizardPage", None))
        self.labelReturnSequences.setText(_translate("WizardPage2", "Return Sequences", None))
        self.comboBoxRate.setItemText(0, _translate("WizardPage2", "0.1", None))
        self.comboBoxRate.setItemText(1, _translate("WizardPage2", "0.2", None))
        self.comboBoxRate.setItemText(2, _translate("WizardPage2", "0.3", None))
        self.comboBoxRate.setItemText(3, _translate("WizardPage2", "0.4", None))
        self.comboBoxRate.setItemText(4, _translate("WizardPage2", "0.5", None))
        self.comboBoxRate.setItemText(5, _translate("WizardPage2", "0.6", None))
        self.comboBoxRate.setItemText(6, _translate("WizardPage2", "0.7", None))
        self.comboBoxRate.setItemText(7, _translate("WizardPage2", "0.8", None))
        self.comboBoxRate.setItemText(8, _translate("WizardPage2", "0.9", None))
        self.comboBoxActivation.setItemText(0, _translate("WizardPage2", "softmax", None))
        self.comboBoxActivation.setItemText(1, _translate("WizardPage2", "softplus", None))
        self.comboBoxActivation.setItemText(2, _translate("WizardPage2", "tanh", None))
        self.comboBoxActivation.setItemText(3, _translate("WizardPage2", "sigmoid", None))
        self.comboBoxActivation.setItemText(4, _translate("WizardPage2", "linear", None))
        self.comboBoxActivation.setItemText(5, _translate("WizardPage2", "relu", None))
        self.label_2.setText(_translate("WizardPage2", "PostProceso (crear Red)", None))
        self.labelActivation.setText(_translate("WizardPage2", "Activation", None))
        self.labelRate.setText(_translate("WizardPage2", "Rate", None))
        self.labelOutputLayer.setText(_translate("WizardPage2", "Output", None))
        self.pushButtonAddCapa.setText(_translate("WizardPage2", "Agregar Capa", None))
        self.labelTipoCapa.setText(_translate("WizardPage2", "Tipo Capa", None))
        self.comboBoxReturnSequencesLSTM.setItemText(0, _translate("WizardPage2", "True", None))
        self.comboBoxReturnSequencesLSTM.setItemText(1, _translate("WizardPage2", "False", None))
        self.lineEditOutputLayer.setText(_translate("WizardPage2", "10", None))
        self.comboBoxTipoCapa.setItemText(0, _translate("WizardPage2", "Embedding", None))
        self.comboBoxTipoCapa.setItemText(1, _translate("WizardPage2", "Dense", None))
        self.comboBoxTipoCapa.setItemText(2, _translate("WizardPage2", "Dropout", None))
        self.comboBoxTipoCapa.setItemText(3, _translate("WizardPage2", "LSTM", None))
        self.pushButtonNext_2.setText(_translate("WizardPage2", "Next", None))
        self.pushButtonArchivo.setText(_translate("WizardPage2", "Generar Archivo de Salida", None))
        self.pushButtonVerRed.setText(_translate("WizardPage2", "Ver capas", None))

