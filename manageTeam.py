# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manageTeam.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb

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
        Dialog.resize(688, 506)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 251, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(320, 50, 251, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.listView = QtGui.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(30, 190, 256, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(360, 190, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(370, 160, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 400, 85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 470, 121, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 470, 121, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.recuperarJugadores = QtGui.QPushButton(Dialog)
        self.recuperarJugadores.setGeometry(QtCore.QRect(70, 400, 181, 29))
        self.recuperarJugadores.setObjectName(_fromUtf8("recuperarJugadores"))

        #definido
        self.recuperarJugadores.clicked.connect(self.recuperarEquipo)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Nombre de la institucion deportiva", None))
        self.label_3.setText(_translate("Dialog", "Jugadores que forman parte ", None))
        self.label_4.setText(_translate("Dialog", "Agregar jugadores", None))
        self.pushButton.setText(_translate("Dialog", "Agregar", None))
        self.pushButton_2.setText(_translate("Dialog", "Aceptar", None))
        self.pushButton_3.setText(_translate("Dialog", "Cancelar", None))
        self.recuperarJugadores.setText(_translate("Dialog", "Recuperar Jugadores", None))

    

    def recuperarEquipo(self):
        serverCDB = Server()
        db = serverCDB['quinelas']

        lists = db.view('queries/getJugadores')
        self.listWidget.clear()
        for item in lists:
            docTemp = item.value
            print(docTemp['content']['nombre'])
            jNombre = docTemp['content']['nombre']
            jApellido = docTemp['content']['apellido']
            jFecha = docTemp['content']['fechaN']
            jRol = docTemp['content']['rol']
            jPeso = docTemp['content']['peso']
            listRow = jNombre+" "+jApellido+" - "+str(jPeso)
            self.listWidget.addItem(listRow)

        #for item in db.view('queries/getJugadores'):
        #    print(item.key._id)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

