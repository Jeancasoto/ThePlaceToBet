import sys
from PyQt4 import QtCore, QtGui, uic
from crearPersonaGui import Ui_Dialog

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("ThePlaceToBet.ui", self)
        #Llamar metodo para salir del sistema
        self.menu_exit.triggered.connect(self.menu_salir)
        #Llamar metodo para exec dialog crear persona
        self.menu_crear_persona.triggered.connect(self.exec_crear_persona)

    #Metodo que manda a llamar el dialog
    def login(self):
        #self.nd = NewDialog(self)
        #self.nd.show()
        print 'alv perro'
    #Metodo al accionar el boton de exit
    def menu_salir(self):
        sys.exit()
        print 'Salir del sistema exitoso'
    #Metodo para exec gui crear persona 
    def exec_crear_persona(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        print 'Debe exec el dialog de crear persona'
    
    
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
