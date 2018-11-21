import sys
from PyQt4 import QtCore, QtGui, uic
from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb

class Ui_MainWindow(QtGui.QMainWindow):
    
    listaJugadores = []
    jugadoresAgregados = []

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("mainWtabs.ui", self)
        self.boton_confirmar.clicked.connect(self.recuperarPersona)
        #Accion para el boton del administrador que habilita tabs 
        self.boton_login.clicked.connect(self.autenticar)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.recuperarJugadores.clicked.connect(self.listarJugadores)
        self.boton_agregar__jug_equipo.clicked.connect(self.transferirJugadores)
    
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

        if identidad not in db:
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

    def listarJugadores(self):
        serverCDB = Server()
        db = serverCDB['quinelas']

        lists = db.view('queries/getJugadores')
        self.lista_jugadores_disp.clear()
        self.lista_jugadores_ag.clear()
        temporal = []
        for item in lists:
            docTemp = item.value
            print(docTemp['content']['nombre'])
            temporal.append(docTemp['_id'])
            jNombre = docTemp['content']['nombre']
            jApellido = docTemp['content']['apellido']
            #jFecha = docTemp['content']['fechaN']
            #jRol = docTemp['content']['rol']
            jPeso = docTemp['content']['peso']
            listRow = jNombre+" "+jApellido+"-"+str(jPeso)
            self.lista_jugadores_disp.addItem(listRow)
        global listaJugadores
        listaJugadores = temporal
            
    def insertarEquipo(self):
        print("INSERTAR EQUIPO")
        nEquipo = self.texto_nom_equipo.text()
        nClub = "N/A"
        nJugadores = []

    def transferirJugadores(self):
        temporal = []
        #for JugadorSelec in self.lista_jugadores_disp.selectedItems():
        tempo = self.lista_jugadores_disp.currentItem()
        value = tempo.text()
        value = value.split("-")
        temporal.append(value[0])
        print(value[0])
        self.lista_jugadores_disp.takeItem(tempo)
        self.lista_jugadores_ag.addItem(tempo)
        
        #jugadoresAgregados.append(self.lista_jugadores_disp.currentRow())
        global jugadoresAgregados
        jugadoresAgregados = temporal
        for i in range(0, len(temporal)):
            print(temporal[i])         
        #print(self.lista_jugadores_disp.currentRow())            
        
    def actualizarEquiposClub(self):
        self.listaEquiposSel.clear()
        self.listaEquiposDisp.clear()

        serverCDB = Server()
        db = serverCDB['quinelas']

        equiposSinClub = db.view('queries/getEquiposSinClub')

        for equipo in equiposSinClub:
            equipo = equipo.value
            row = equipo["content"]["nombreEquipo"]
            print(row)
            self.listaEquiposDisp.addItem(row)

    def agregarListaEquipo(self):
        for EquipoSelec in self.listaEquiposDisp.selectedItems():
            self.listaEquiposDisp.takeItem(self.listaEquiposDisp.row(EquipoSelec))
            self.listaEquiposSel.addItem(EquipoSelec)

    def quitarListaEquipo(self):
        for EquipoSelec in self.listaEquiposSel.selectedItems():
            self.listaEquiposSel.takeItem(self.listaEquiposSel.row(EquipoSelec))
            self.listaEquiposDisp.addItem(EquipoSelec)

    def crearClub(self):
        print("CREAR CLUB")
        nombreClub = self.textNomClub.text()

        listaEquipos = []
        for EquipoSelec in self.listaEquiposSel.selectedItems():
            listaEquipos.append(EquipoSelec)

        serverCDB = Server()
        db = serverCDB['quinelas']

        if nombreClub not in db:
            docClub = {
                '_id': nombreClub,
                'content': {
                    'nombreClub': nombreClub,
                    'equipos': listaEquipos
                }
            }
            db.save(docClub)
            self.listaEquiposSel.clear()
            self.listaEquiposDisp.clear()
        else:
            print("El nombre de club ya existe")
            self.listaEquiposSel.clear()
            self.listaEquiposDisp.clear()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
