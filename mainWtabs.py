# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWtabs.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Log_in_admin = QtGui.QTabWidget(self.centralwidget)
        self.Log_in_admin.setGeometry(QtCore.QRect(20, 30, 771, 501))
        self.Log_in_admin.setDocumentMode(False)
        self.Log_in_admin.setTabsClosable(False)
        self.Log_in_admin.setObjectName(_fromUtf8("Log_in_admin"))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.Log_in_admin.addTab(self.widget, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.Log_in_admin.addTab(self.tab_5, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.Log_in_admin.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Log_in_admin.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Log_in_admin.setTabText(self.Log_in_admin.indexOf(self.widget), _translate("MainWindow", "Administrador", None))
        self.Log_in_admin.setTabText(self.Log_in_admin.indexOf(self.tab_5), _translate("MainWindow", "Crear persona", None))
        self.Log_in_admin.setTabText(self.Log_in_admin.indexOf(self.tab_2), _translate("MainWindow", "Crear equipo", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

