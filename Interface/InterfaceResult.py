# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfazResultados.ui'
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

class Ui_DialogResultados(object):
    def setupUi(self, DialogResultados):
        DialogResultados.setObjectName(_fromUtf8("DialogResultados"))
        DialogResultados.resize(391, 261)
        self.listViewResultados = QtGui.QListView(DialogResultados)
        self.listViewResultados.setGeometry(QtCore.QRect(10, 10, 371, 241))
        self.listViewResultados.setObjectName(_fromUtf8("listViewResultados"))

        self.retranslateUi(DialogResultados)
        QtCore.QMetaObject.connectSlotsByName(DialogResultados)

    def retranslateUi(self, DialogResultados):
        DialogResultados.setWindowTitle(_translate("DialogResultados", "Resultados", None))

