import sys
from PyQt4 import QtCore, QtGui, uic
from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("mainWtabs.ui", self)
        self.boton_confirmar.clicked.connect(self.recuperarPersona)
        #Accion para el boton del administrador que habilita tabs 
        self.boton_login.clicked.connect(self.autenticar)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
    
    def autenticar(self):
        input_username = str(self.username.text())
        input_password = str(self.password.text())
        if input_username == "admin":
            print ('Username encontrado')
            if  input_password == 'admin':
                print ('Password encontrado')
                self.Log_in_admin.setTabEnabled(1, True)
                self.Log_in_admin.setTabEnabled(2, True)
            else:
                print ('Password no encontrada')
        else:
            print ('Username no encontrado')

    def recuperarPersona(self):
        print ('Entro al metodo')
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

        serverCDB = Server()
        db = serverCDB['quinelas']

        if ( identidad not in db ):
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

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
