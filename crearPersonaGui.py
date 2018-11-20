# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CrearPersona.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#from couchdb.mapping import Document, TextField, IntegerField, Mapping
#from couchdb.mapping import DictField, ViewField, BooleanField, ListField
#from couchdb import Server
#import couchdb

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
        Dialog.resize(589, 432)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 250, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(30, 50, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.fecha_nacimiento = QtGui.QDateEdit(Dialog)
        self.fecha_nacimiento.setGeometry(QtCore.QRect(230, 150, 151, 29))
        self.fecha_nacimiento.setObjectName(_fromUtf8("fecha_nacimiento"))
        self.numero_dentidad = QtGui.QLineEdit(Dialog)
        self.numero_dentidad.setGeometry(QtCore.QRect(230, 100, 171, 29))
        self.numero_dentidad.setObjectName(_fromUtf8("numero_dentidad"))
        self.primer_nombre = QtGui.QLineEdit(Dialog)
        self.primer_nombre.setGeometry(QtCore.QRect(230, 200, 161, 29))
        self.primer_nombre.setObjectName(_fromUtf8("primer_nombre"))
        self.primer_apellido = QtGui.QLineEdit(Dialog)
        self.primer_apellido.setGeometry(QtCore.QRect(230, 250, 161, 29))
        self.primer_apellido.setObjectName(_fromUtf8("primer_apellido"))
        self.combo_box_desempeno = QtGui.QComboBox(Dialog)
        self.combo_box_desempeno.setGeometry(QtCore.QRect(230, 50, 251, 27))
        self.combo_box_desempeno.setEditable(False)
        self.combo_box_desempeno.setModelColumn(0)
        self.combo_box_desempeno.setObjectName(_fromUtf8("combo_box_desempeno"))
        self.combo_box_desempeno.addItem(_fromUtf8(""))
        self.combo_box_desempeno.addItem(_fromUtf8(""))
        self.combo_box_desempeno.addItem(_fromUtf8(""))
        self.boton_cancelar = QtGui.QPushButton(Dialog)
        self.boton_cancelar.setGeometry(QtCore.QRect(380, 370, 85, 27))
        self.boton_cancelar.setObjectName(_fromUtf8("boton_cancelar"))
        self.boton_confirmar = QtGui.QPushButton(Dialog)
        self.boton_confirmar.setGeometry(QtCore.QRect(480, 370, 85, 27))
        self.boton_confirmar.setObjectName(_fromUtf8("boton_confirmar"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 300, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(230, 300, 161, 29))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))


        #Definido
        self.boton_confirmar.clicked.connect(self.recuperarPersona)
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def recuperarPersona(self):
        fechaN = self.fecha_nacimiento.date()
        fechaN = fechaN.toPyDate()
        identidad = self.numero_dentidad.text()
        pNombre = self.primer_nombre.text()
        pApellido = self.primer_apellido.text()
        rol = str(self.combo_box_desempeno.currentText())
        peso = self.doubleSpinBox.value()
        print(fechaN)
        print(identidad)
        print(pNombre)
        print(pApellido)
        print(rol)
        print(peso)

        """serverCDB = Server()
        db = serverCDB['quinelas']

        if ( db[identidad] is None ):
            docPersona = {
                '_id': identidad,
                'content': {
                    'nombre': pNombre,
                    'apellido': pApellido,
                    'fechaN': fechaN.strftime('%m/%d/%Y'),
                    'rol': rol,
                    'peso': peso
                }
            }
            db.save(docPersona)
        else:
            print("Ya existe una persona con ese ID")
        #-----faltaria hacer el insert aqui-----
        """

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Agregar persona", None))
        self.label_2.setText(_translate("Dialog", "Numero de identidad ", None))
        self.label_3.setText(_translate("Dialog", "Fecha de nacimiento ", None))
        self.label_4.setText(_translate("Dialog", "Primer Nombre", None))
        self.label_8.setText(_translate("Dialog", "Primer Apellido", None))
        self.label_10.setText(_translate("Dialog", "Se desempenara como ::", None))
        self.fecha_nacimiento.setDisplayFormat(_translate("Dialog", "dd/mm/yyyy", None))
        self.combo_box_desempeno.setItemText(0, _translate("Dialog", "Arbitro", None))
        self.combo_box_desempeno.setItemText(1, _translate("Dialog", "Jugador", None))
        self.combo_box_desempeno.setItemText(2, _translate("Dialog", "Entrenador", None))
        self.boton_cancelar.setText(_translate("Dialog", "Cancelar", None))
        self.boton_confirmar.setText(_translate("Dialog", "Confirmar", None))
        self.label_11.setText(_translate("Dialog", "Peso", None))

