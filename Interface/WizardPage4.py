# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WPruebaUser4.ui'
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

class Ui_WizardPage4(object):
    def setupUi(self, WizardPage4):
        WizardPage4.setObjectName(_fromUtf8("WizardPage4"))
        WizardPage4.resize(480, 198)
        self.pushButtonResultados = QtGui.QPushButton(WizardPage4)
        self.pushButtonResultados.setGeometry(QtCore.QRect(330, 60, 131, 23))
        self.pushButtonResultados.setObjectName(_fromUtf8("pushButtonResultados"))
        self.label_6 = QtGui.QLabel(WizardPage4)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBoxTipoMetrica = QtGui.QComboBox(WizardPage4)
        self.comboBoxTipoMetrica.setGeometry(QtCore.QRect(140, 60, 151, 22))
        self.comboBoxTipoMetrica.setObjectName(_fromUtf8("comboBoxTipoMetrica"))
        self.comboBoxTipoMetrica.addItem(_fromUtf8(""))
        self.comboBoxTipoMetrica.addItem(_fromUtf8(""))
        self.comboBoxTipoMetrica.addItem(_fromUtf8(""))
        self.comboBoxTipoMetrica.addItem(_fromUtf8(""))
        self.comboBoxTipoMetrica.addItem(_fromUtf8(""))
        self.labelTipoMetrica = QtGui.QLabel(WizardPage4)
        self.labelTipoMetrica.setGeometry(QtCore.QRect(20, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelTipoMetrica.setFont(font)
        self.labelTipoMetrica.setObjectName(_fromUtf8("labelTipoMetrica"))

        self.retranslateUi(WizardPage4)
        QtCore.QMetaObject.connectSlotsByName(WizardPage4)

    def retranslateUi(self, WizardPage4):
        WizardPage4.setWindowTitle(_translate("WizardPage4", "WizardPage", None))
        self.pushButtonResultados.setText(_translate("WizardPage4", "Mostrar Metricas", None))
        self.label_6.setText(_translate("WizardPage4", "PostProceso", None))
        self.comboBoxTipoMetrica.setItemText(0, _translate("WizardPage4", "Precision Score", None))
        self.comboBoxTipoMetrica.setItemText(1, _translate("WizardPage4", "Recall_score", None))
        self.comboBoxTipoMetrica.setItemText(2, _translate("WizardPage4", "zero_one_loss", None))
        self.comboBoxTipoMetrica.setItemText(3, _translate("WizardPage4", "accuracy_score", None))
        self.comboBoxTipoMetrica.setItemText(4, _translate("WizardPage4", "confusion_matrix", None))
        self.labelTipoMetrica.setText(_translate("WizardPage4", "Tipo Metrica", None))

