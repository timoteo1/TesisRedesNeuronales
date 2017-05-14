# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfazInforme.ui'
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

class Ui_DialogInforme(object):
    def setupUi(self, DialogInforme):
        DialogInforme.setObjectName(_fromUtf8("DialogInforme"))
        DialogInforme.resize(496, 332)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogInforme.sizePolicy().hasHeightForWidth())
        DialogInforme.setSizePolicy(sizePolicy)
        self.scrollArea = QtGui.QScrollArea(DialogInforme)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 471, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollContents = QtGui.QWidget()
        self.scrollContents.setGeometry(QtCore.QRect(0, 0, 469, 309))
        self.scrollContents.setMinimumSize(QtCore.QSize(399, 0))
        self.scrollContents.setObjectName(_fromUtf8("scrollContents"))
        self.labelMensaje = QtGui.QLabel(self.scrollContents)
        self.labelMensaje.setGeometry(QtCore.QRect(0, 0, 471, 311))
        self.labelMensaje.setText(_fromUtf8(""))
        self.labelMensaje.setObjectName(_fromUtf8("labelMensaje"))
        self.scrollArea.setWidget(self.scrollContents)

        self.retranslateUi(DialogInforme)
        QtCore.QMetaObject.connectSlotsByName(DialogInforme)

    def retranslateUi(self, DialogInforme):
        DialogInforme.setWindowTitle(_translate("DialogInforme", "Informacion", None))

