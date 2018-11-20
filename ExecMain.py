import sys
from PyQt4 import QtCore, QtGui, uic

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("ThePlaceToBet.ui", self)
        #Llamar a la ventana que muestra un login para el admin
        self.menu_exit.triggered.connect(self.menu_salir)
    #Metodo que manda a llamar el dialog
    def login(self):
        #self.nd = NewDialog(self)
        #self.nd.show()
        print 'alv perro'
    def menu_salir(self):
        QCoreApplication.exit(0)
        print 'deberia'
    
#class Plugin:
#    def __init__(self, iface):
#        self.dlg.button.connect(self.open_new_dialog)


#Creacion del Dialog admin     
#class Login_as_admin(QtGui.QWidget):
#    def __init__(self, parent):
#        super(NewDialog, self).__init__(parent) 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
