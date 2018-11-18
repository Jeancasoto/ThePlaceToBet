import sys
from PyQt4 import QtCore, QtGui, uic

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("ThePlaceToBet.ui", self)
        self.actionPrueba.triggered.connect(self.hola)
        self.actionPrueba2.triggered.connect(self.adios)


    def hola(self):
        print 'Hola'

    def adios(self):
        print 'adios'


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
