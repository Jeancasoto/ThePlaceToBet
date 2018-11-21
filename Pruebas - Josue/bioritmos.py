# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bioritmos.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import datetime
import math
import decimal

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

class Ui_MainWindow(object):
    def formulaFisico(self, diasNac):
        fechaAc = datetime.datetime.now().date()
        delta = fechaAc - diasNac
        #print(fechaNa)
        #print(fechaAc)
        #print(delta.days)
        bioFis = 100*math.sin((math.pi*2*delta.days)/23)
        bioFis = round(bioFis,2)
        print(bioFis)

    def calculoFisico(self):
        tempo = self.fecha.date()
        fechaNa = tempo.toPyDate()
        self.formulaFisico(fechaNa)

    def formulaEmocional(self, diasNac):
        fechaAc = datetime.datetime.now().date()
        delta = fechaAc - diasNac
        #print(fechaNa)
        #print(fechaAc)
        #print(delta.days)
        bioEmo = 100*math.sin((math.pi*2*delta.days)/28)
        bioEmo = round(bioEmo,2)
        print(bioEmo)
    
    def calculoEmocional(self):
        tempo = self.fecha.date()
        fechaNa = tempo.toPyDate()
        self.formulaEmocional(fechaNa)
        
    def formulaIntelectual(self,diasNac):
        fechaAc = datetime.datetime.now().date()
        delta = fechaAc - diasNac
        #print(fechaNa)
        #print(fechaAc)
        #print(delta.days)
        bioInt = 100*math.sin((math.pi*2*delta.days)/33)
        bioInt = round(bioInt,2)setEchoMode(QtGui.QLineEdit.Password)
        listaNombre = ["Alfonso","Carlos","Emilio","Antonio","Nicolas","Eric","Erik","Daniel","Fidel","Ferran","Alejandro","Victor","Mariano","Galvan","Fermin","Guillem","Alfredo","Inaki","Lorenzo","Gil","Dario","Nacho","Aaron","Cesar","Feliciano","Marc","Andreu","Benjamin","Jacobo","Alberto","Javier","Javi","Xavier","Xavi","Roberto","Raul","Bruno","Ramon","Gabi","Gaby","Adam","Adan","Anael","Ignacio","Manuel","Hugo","Silvestre","Gaspar","Gustavo","Gregorio","German","Federico","Angel","Ivan","Felipe","Pau","Paulo","Pao","Paolo","Vicente","Gilberto","Ismael","Beltrán","Aitor","Mauro","Jesus","Gaizka"]
        print(bioInt)
    
    def calculoIntelectual(self):
        tempo = self.fecha.date()
        fechaNa = tempo.toPyDate()
        self.formulaIntelectual(fechaNa)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.fecha = QtGui.QDateEdit(self.centralwidget)
        self.fecha.setGeometry(QtCore.QRect(280, 110, 110, 27))
        self.fecha.setObjectName(_fromUtf8("fecha"))
        self.fisico = QtGui.QPushButton(self.centralwidget)
        self.fisico.setGeometry(QtCore.QRect(80, 250, 97, 27))
        self.fisico.setObjectName(_fromUtf8("fisico"))
        self.animico = QtGui.QPushButton(self.centralwidget)
        self.animico.setGeometry(QtCore.QRect(250, 250, 97, 27))
        self.animico.setObjectName(_fromUtf8("animico"))
        self.intelectual = QtGui.QPushButton(self.centralwidget)
        self.intelectual.setGeometry(QtCore.QRect(410, 250, 97, 27))
        self.intelectual.setObjectName(_fromUtf8("intelectual"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.fisico.clicked.connect(self.calculoFisico)
        self.animico.clicked.connect(self.calculoEmocional)
        self.intelectual.clicked.connect(self.calculoIntelectual)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.fecha.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy", None))
        self.fisico.setText(_translate("MainWindow", "fisico", None))
        self.animico.setText(_translate("MainWindow", "emo", None))
        self.intelectual.setText(_translate("MainWindow", "intelec", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

