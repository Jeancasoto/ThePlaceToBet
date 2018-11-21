# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CrearClub.ui'
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
        Dialog.resize(713, 557)
        self.listaEquiposDisp = QtGui.QListView(Dialog)
        self.listaEquiposDisp.setGeometry(QtCore.QRect(30, 130, 271, 361))
        self.listaEquiposDisp.setObjectName(_fromUtf8("listaEquiposDisp"))
        self.listaEquiposSel = QtGui.QListView(Dialog)
        self.listaEquiposSel.setGeometry(QtCore.QRect(410, 130, 271, 361))
        self.listaEquiposSel.setObjectName(_fromUtf8("listaEquiposSel"))
        self.textNomClub = QtGui.QLineEdit(Dialog)
        self.textNomClub.setGeometry(QtCore.QRect(100, 50, 511, 29))
        self.textNomClub.setObjectName(_fromUtf8("textNomClub"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 61, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 241, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 141, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(470, 110, 151, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.botonAgregarEquipo = QtGui.QPushButton(Dialog)
        self.botonAgregarEquipo.setGeometry(QtCore.QRect(310, 260, 91, 29))
        self.botonAgregarEquipo.setObjectName(_fromUtf8("botonAgregarEquipo"))
        self.botonEliminarEquipo = QtGui.QPushButton(Dialog)
        self.botonEliminarEquipo.setGeometry(QtCore.QRect(310, 310, 91, 29))
        self.botonEliminarEquipo.setObjectName(_fromUtf8("botonEliminarEquipo"))
        self.botonAceptar = QtGui.QPushButton(Dialog)
        self.botonAceptar.setGeometry(QtCore.QRect(570, 510, 97, 29))
        self.botonAceptar.setObjectName(_fromUtf8("botonAceptar"))
        self.botonCancelar = QtGui.QPushButton(Dialog)
        self.botonCancelar.setGeometry(QtCore.QRect(440, 510, 97, 29))
        self.botonCancelar.setObjectName(_fromUtf8("botonCancelar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Nombre:", None))
        self.label_2.setText(_translate("Dialog", "Nuevo Club Deportivo", None))
        self.label_3.setText(_translate("Dialog", "Equipos Disponibles", None))
        self.label_4.setText(_translate("Dialog", "Equipos Seleccionados", None))
        self.botonAgregarEquipo.setText(_translate("Dialog", "Agegar ->", None))
        self.botonEliminarEquipo.setText(_translate("Dialog", "<-Eliminar", None))
        self.botonAceptar.setText(_translate("Dialog", "Aceptar", None))
        self.botonCancelar.setText(_translate("Dialog", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

