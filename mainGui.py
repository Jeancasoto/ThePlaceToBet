# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ThePlaceToBet.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(806, 630)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 1300, 866))
        self.label.setAutoFillBackground(False)
        self.label.setText(_fromUtf8(""))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../Pictures/15418809-insignes-de-célèbres-clubs-de-football-anglais.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.contenedor_der = QtGui.QWidget(self.centralwidget)
        self.contenedor_der.setEnabled(True)
        self.contenedor_der.setGeometry(QtCore.QRect(240, 0, 581, 591))
        self.contenedor_der.setMouseTracking(False)
        self.contenedor_der.setAutoFillBackground(False)
        self.contenedor_der.setObjectName(_fromUtf8("contenedor_der"))
        self.contenedor_izq = QtGui.QWidget(self.centralwidget)
        self.contenedor_izq.setGeometry(QtCore.QRect(0, 0, 221, 591))
        self.contenedor_izq.setAutoFillBackground(False)
        self.contenedor_izq.setObjectName(_fromUtf8("contenedor_izq"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuUser = QtGui.QMenu(self.menubar)
        self.menuUser.setSeparatorsCollapsible(False)
        self.menuUser.setObjectName(_fromUtf8("menuUser"))
        self.menuAdministrador = QtGui.QMenu(self.menuUser)
        self.menuAdministrador.setObjectName(_fromUtf8("menuAdministrador"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCrear_Persona = QtGui.QAction(MainWindow)
        self.actionCrear_Persona.setObjectName(_fromUtf8("actionCrear_Persona"))
        self.actionCrear_Equipo = QtGui.QAction(MainWindow)
        self.actionCrear_Equipo.setObjectName(_fromUtf8("actionCrear_Equipo"))
        self.actionManage_Team = QtGui.QAction(MainWindow)
        self.actionManage_Team.setObjectName(_fromUtf8("actionManage_Team"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPrueba = QtGui.QAction(MainWindow)
        self.actionPrueba.setObjectName(_fromUtf8("actionPrueba"))
        self.menuAdministrador.addAction(self.actionCrear_Persona)
        self.menuUser.addAction(self.menuAdministrador.menuAction())
        self.menuUser.addAction(self.actionManage_Team)
        self.menuUser.addAction(self.actionExit)
        self.menuUser.addAction(self.actionPrueba)
        self.menubar.addAction(self.menuUser.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "The Place to Bet", None))
        self.menuUser.setTitle(_translate("MainWindow", "Opciones", None))
        self.menuAdministrador.setTitle(_translate("MainWindow", "Administrador", None))
        self.actionCrear_Persona.setText(_translate("MainWindow", "Crear Persona ", None))
        self.actionCrear_Equipo.setText(_translate("MainWindow", "Crear Equipo", None))
        self.actionManage_Team.setText(_translate("MainWindow", "Manage Team", None))
        self.actionExit.setText(_translate("MainWindow", "Salir", None))
        self.actionPrueba.setText(_translate("MainWindow", "prueba", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

