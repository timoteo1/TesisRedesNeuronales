# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WPruebaUser3.ui'
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

class Ui_WizardPage3(object):
    def setupUi(self, WizardPage3):
        WizardPage3.setObjectName(_fromUtf8("WizardPage3"))
        WizardPage3.resize(478, 323)
        self.label_4 = QtGui.QLabel(WizardPage3)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.labelnNB_epoch_2 = QtGui.QLabel(WizardPage3)
        self.labelnNB_epoch_2.setGeometry(QtCore.QRect(20, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelnNB_epoch_2.setFont(font)
        self.labelnNB_epoch_2.setObjectName(_fromUtf8("labelnNB_epoch_2"))
        self.label_3 = QtGui.QLabel(WizardPage3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 401, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditNB_epoch = QtGui.QLineEdit(WizardPage3)
        self.lineEditNB_epoch.setGeometry(QtCore.QRect(140, 230, 61, 21))
        self.lineEditNB_epoch.setObjectName(_fromUtf8("lineEditNB_epoch"))
        self.labelCompilerLoss = QtGui.QLabel(WizardPage3)
        self.labelCompilerLoss.setGeometry(QtCore.QRect(20, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelCompilerLoss.setFont(font)
        self.labelCompilerLoss.setObjectName(_fromUtf8("labelCompilerLoss"))
        self.labelCompilerOptimizer = QtGui.QLabel(WizardPage3)
        self.labelCompilerOptimizer.setGeometry(QtCore.QRect(20, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelCompilerOptimizer.setFont(font)
        self.labelCompilerOptimizer.setObjectName(_fromUtf8("labelCompilerOptimizer"))
        self.lineEditBatch = QtGui.QLineEdit(WizardPage3)
        self.lineEditBatch.setGeometry(QtCore.QRect(140, 260, 61, 21))
        self.lineEditBatch.setObjectName(_fromUtf8("lineEditBatch"))
        self.label_5 = QtGui.QLabel(WizardPage3)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBoxCompilerOptimizer = QtGui.QComboBox(WizardPage3)
        self.comboBoxCompilerOptimizer.setGeometry(QtCore.QRect(140, 80, 151, 22))
        self.comboBoxCompilerOptimizer.setObjectName(_fromUtf8("comboBoxCompilerOptimizer"))
        self.comboBoxCompilerOptimizer.addItem(_fromUtf8(""))
        self.comboBoxCompilerOptimizer.addItem(_fromUtf8(""))
        self.comboBoxCompilerOptimizer.addItem(_fromUtf8(""))
        self.comboBoxCompilerOptimizer.addItem(_fromUtf8(""))
        self.labelnNB_epoch = QtGui.QLabel(WizardPage3)
        self.labelnNB_epoch.setGeometry(QtCore.QRect(20, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelnNB_epoch.setFont(font)
        self.labelnNB_epoch.setObjectName(_fromUtf8("labelnNB_epoch"))
        self.pushButtonProceso = QtGui.QPushButton(WizardPage3)
        self.pushButtonProceso.setGeometry(QtCore.QRect(330, 270, 131, 23))
        self.pushButtonProceso.setObjectName(_fromUtf8("pushButtonProceso"))
        self.labelCompilerLoss_2 = QtGui.QLabel(WizardPage3)
        self.labelCompilerLoss_2.setGeometry(QtCore.QRect(20, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(9)
        self.labelCompilerLoss_2.setFont(font)
        self.labelCompilerLoss_2.setObjectName(_fromUtf8("labelCompilerLoss_2"))
        self.comboBoxCompilerLoss = QtGui.QComboBox(WizardPage3)
        self.comboBoxCompilerLoss.setGeometry(QtCore.QRect(140, 120, 151, 22))
        self.comboBoxCompilerLoss.setObjectName(_fromUtf8("comboBoxCompilerLoss"))
        self.comboBoxCompilerLoss.addItem(_fromUtf8(""))
        self.comboBoxCompilerLoss.addItem(_fromUtf8(""))
        self.comboBoxCompilerLoss.addItem(_fromUtf8(""))
        self.comboBoxCompilerLoss.addItem(_fromUtf8(""))
        self.comboBoxCompilerLoss.addItem(_fromUtf8(""))
        self.comboBoxCompilerMetrics = QtGui.QComboBox(WizardPage3)
        self.comboBoxCompilerMetrics.setGeometry(QtCore.QRect(140, 160, 151, 22))
        self.comboBoxCompilerMetrics.setObjectName(_fromUtf8("comboBoxCompilerMetrics"))
        self.comboBoxCompilerMetrics.addItem(_fromUtf8(""))
        self.comboBoxCompilerMetrics.addItem(_fromUtf8(""))
        self.comboBoxCompilerMetrics.addItem(_fromUtf8(""))

        self.retranslateUi(WizardPage3)
        QtCore.QMetaObject.connectSlotsByName(WizardPage3)

    def retranslateUi(self, WizardPage3):
        WizardPage3.setWindowTitle(_translate("WizardPage3", "WizardPage", None))
        self.label_4.setText(_translate("WizardPage3", "Entrenamiento Red", None))
        self.labelnNB_epoch_2.setText(_translate("WizardPage3", "batch_size", None))
        self.label_3.setText(_translate("WizardPage3", "PostProceso (Compilación - Entrenamiento Red)", None))
        self.lineEditNB_epoch.setText(_translate("WizardPage3", "10", None))
        self.labelCompilerLoss.setText(_translate("WizardPage3", "loss", None))
        self.labelCompilerOptimizer.setText(_translate("WizardPage3", "Optimizer", None))
        self.lineEditBatch.setText(_translate("WizardPage3", "10", None))
        self.label_5.setText(_translate("WizardPage3", "Compilación Red", None))
        self.comboBoxCompilerOptimizer.setItemText(0, _translate("WizardPage3", "rmsprop", None))
        self.comboBoxCompilerOptimizer.setItemText(1, _translate("WizardPage3", "adagrad", None))
        self.comboBoxCompilerOptimizer.setItemText(2, _translate("WizardPage3", "adadelta", None))
        self.comboBoxCompilerOptimizer.setItemText(3, _translate("WizardPage3", "adam", None))
        self.labelnNB_epoch.setText(_translate("WizardPage3", "nb_epoch", None))
        self.pushButtonProceso.setText(_translate("WizardPage3", "Procesar", None))
        self.labelCompilerLoss_2.setText(_translate("WizardPage3", "metrics", None))
        self.comboBoxCompilerLoss.setItemText(0, _translate("WizardPage3", "categorical_crossentropy", None))
        self.comboBoxCompilerLoss.setItemText(1, _translate("WizardPage3", "poisson", None))
        self.comboBoxCompilerLoss.setItemText(2, _translate("WizardPage3", "binary_crossentropy", None))
        self.comboBoxCompilerLoss.setItemText(3, _translate("WizardPage3", "mean_squared_error", None))
        self.comboBoxCompilerLoss.setItemText(4, _translate("WizardPage3", "mean_absolute_error", None))
        self.comboBoxCompilerMetrics.setItemText(0, _translate("WizardPage3", "categorical_accuracy", None))
        self.comboBoxCompilerMetrics.setItemText(1, _translate("WizardPage3", "binary_accuracy", None))
        self.comboBoxCompilerMetrics.setItemText(2, _translate("WizardPage3", "sparse_categorical_accuracy", None))

