# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfazCapasuiListView.ui'
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

class Ui_DialogCapas(object):
    def setupUi(self, DialogCapas):
        DialogCapas.setObjectName(_fromUtf8("DialogCapas"))
        DialogCapas.resize(496, 332)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogCapas.sizePolicy().hasHeightForWidth())
        DialogCapas.setSizePolicy(sizePolicy)
        self.listViewCapas = QtGui.QListView(DialogCapas)
        self.listViewCapas.setGeometry(QtCore.QRect(10, 10, 471, 311))
        self.listViewCapas.setObjectName(_fromUtf8("listViewCapas"))

        self.retranslateUi(DialogCapas)
        QtCore.QMetaObject.connectSlotsByName(DialogCapas)

    def retranslateUi(self, DialogCapas):
        DialogCapas.setWindowTitle(_translate("DialogCapas", "Capas cargadas en la red", None))

