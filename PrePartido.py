# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PrePartido.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(741, 596)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 90, 71, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(550, 90, 41, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tablaJugVis = QtGui.QTableWidget(Dialog)
        self.tablaJugVis.setGeometry(QtCore.QRect(20, 110, 341, 351))
        self.tablaJugVis.setColumnCount(4)
        self.tablaJugVis.setObjectName(_fromUtf8("tablaJugVis"))
        self.tablaJugVis.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaJugVis.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugVis.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugVis.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugVis.setHorizontalHeaderItem(3, item)
        self.tablaJugLocal = QtGui.QTableWidget(Dialog)
        self.tablaJugLocal.setGeometry(QtCore.QRect(385, 110, 341, 351))
        self.tablaJugLocal.setObjectName(_fromUtf8("tablaJugLocal"))
        self.tablaJugLocal.setColumnCount(4)
        self.tablaJugLocal.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaJugLocal.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugLocal.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugLocal.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugLocal.setHorizontalHeaderItem(3, item)
        self.botonAceptar = QtGui.QPushButton(Dialog)
        self.botonAceptar.setGeometry(QtCore.QRect(630, 550, 97, 29))
        self.botonAceptar.setObjectName(_fromUtf8("botonAceptar"))
        self.botonCancelar = QtGui.QPushButton(Dialog)
        self.botonCancelar.setGeometry(QtCore.QRect(510, 550, 97, 29))
        self.botonCancelar.setObjectName(_fromUtf8("botonCancelar"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 480, 141, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 30, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(480, 480, 141, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.labelPromBRVis = QtGui.QLabel(Dialog)
        self.labelPromBRVis.setGeometry(QtCore.QRect(210, 480, 64, 17))
        self.labelPromBRVis.setText(_fromUtf8(""))
        self.labelPromBRVis.setObjectName(_fromUtf8("labelPromBRVis"))
        self.labelPromBRLocal = QtGui.QLabel(Dialog)
        self.labelPromBRLocal.setGeometry(QtCore.QRect(670, 480, 64, 17))
        self.labelPromBRLocal.setText(_fromUtf8(""))
        self.labelPromBRLocal.setObjectName(_fromUtf8("labelPromBRLocal"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Visitante", None))
        self.label_2.setText(_translate("Dialog", "Local", None))
        item = self.tablaJugVis.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nombre", None))
        item = self.tablaJugVis.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Peso", None))
        item = self.tablaJugVis.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Bioritmo", None))
        item = self.tablaJugVis.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Posicion", None))
        item = self.tablaJugLocal.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nombre", None))
        item = self.tablaJugLocal.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Peso", None))
        item = self.tablaJugLocal.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Bioritmo", None))
        item = self.tablaJugLocal.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Posicion", None))
        self.botonAceptar.setText(_translate("Dialog", "Aceptar", None))
        self.botonCancelar.setText(_translate("Dialog", "Cancelar", None))
        self.label_3.setText(_translate("Dialog", "Promedio Bioritmos:", None))
        self.label_4.setText(_translate("Dialog", "Jugadores en el Partido", None))
        self.label_5.setText(_translate("Dialog", "Promedio Bioritmos:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

