import sys
from random import randint
from PyQt4 import QtCore, QtGui, uic
from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb
import datetime
import math
import decimal

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
        self.boton_equipo_aceptar.clicked.connect(self.insertarEquipo)
        self.botonAgregarEquipo.clicked.connect(self.agregarListaEquipo)
        self.botonEliminarEquipo.clicked.connect(self.quitarListaEquipo)
        self.botonActualizarEqui.clicked.connect(self.actualizarEquiposClub)
        self.botonAceptar.clicked.connect(self.crearClub)

    
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
            jId = docTemp["_id"]
            jNombre = docTemp['content']['nombre']
            jApellido = docTemp['content']['apellido']
            #jFecha = docTemp['content']['fechaN']
            #jRol = docTemp['content']['rol']
            jPeso = docTemp['content']['peso']
            listRow = jId+"-"+jNombre+" "+jApellido+"-"+str(jPeso)
            self.lista_jugadores_disp.addItem(listRow)
        global listaJugadores
        listaJugadores = temporal
        global jugadoresAgregados
        jugadoresAgregados = []
            
    def insertarEquipo(self):
        print("INSERTAR EQUIPO")
        nEquipo = self.texto_nom_equipo.text()
        print(nEquipo)
        nClub = "N/A"
        nJugadores = jugadoresAgregados
        
        serverCDB = Server()
        db = serverCDB['quinelas']
        
        if nEquipo not in db:
            print("entro aqui perro")
            docEquipo = {
                '_id': nEquipo,
                'content': {
                    'club': nClub,
                    'integrantes': nJugadores
                }
            }
            db.save(docEquipo)
            print("Agregado exitosamente!")
        else:
            print("Ya existe un equipo con ese ID")
        


    def transferirJugadores(self):
        temporal = []
        for JugadorSelec in self.lista_jugadores_disp.selectedItems():
            #tempo = self.lista_jugadores_disp.currentItem()
            value = JugadorSelec.text()
            value = value.split("-")
            temporal.append(value[0])
            print(value[0])    
            self.lista_jugadores_disp.takeItem(self.lista_jugadores_disp.row(JugadorSelec))
            self.lista_jugadores_ag.addItem(JugadorSelec)
        #jugadoresAgregados.append(self.lista_jugadores_disp.currentRow())
        global jugadoresAgregados
        jugadoresAgregados = temporal
        #for i in range(0, len(temporal)):
        #    print(temporal[i])         
        #print(self.lista_jugadores_disp.currentRow())            
        
    def actualizarEquiposClub(self):
        self.listaEquiposSel.clear()
        self.listaEquiposDisp.clear()

        serverCDB = Server()
        db = serverCDB['quinelas']

        equiposSinClub = db.view('queries/getEquiposSinClub')

        for equipo in equiposSinClub:
            equipo = equipo.value
            row = equipo["_id"]
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

        serverCDB = Server()
        db = serverCDB['quinelas']

        idClub = "1" + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))

        listaEquipos = []
        cont = 0

        items = [] 
        for index in range(self.listaEquiposSel.count()): 
            items.append(str(self.listaEquiposSel.item(index).text()))

        for EquipoSelec in items:
            #EquipoSelec = str(self.listaEquiposSel.item(cont))
            listaEquipos.append(EquipoSelec)
            docEquipo = db.get(EquipoSelec)
            docEquipo["content"]["club"] = idClub
            print(docEquipo)
            db.save(docEquipo)
            cont += 1

        docClub = {
            '_id': idClub,
            'content': {
                'equipos': listaEquipos
            }
        }
        db.save(docClub)

        self.listaEquiposSel.clear()
        self.listaEquiposDisp.clear()

    def calcularBioritmos(self, equipoSelec):

        #Este metodo calcula el bioritmo para un EQUIPO
        #Calcula el bioritmo para cada jugador individual, los suma y saca la media ponderada
        #Luego, saca la media de los 3 bioritmos (fis, emo, int)

        """
        A partir de aqui, necesito saber los equipos y sus jugadores para calcular su bioritmo
        """
        print("CALCULAR BIORITMOS")

        serverCDB = Server()
        db = serverCDB['quinelas']
        acumPesos = 0
        acumFisico = 0
        acumEmo = 0
        acumIntel = 0
        if(equipoSelec in db):
            doc = db[equipoSelec]
            listaJ = []
            #listaJ = doc["content"]["integrantes"]
            for i in range(0,10):
                elementoI = listaJ[i]
                doc1 = db[elementoI]
                fechaNac = doc1["content"]["fechaN"]
                fechaNac = fechaNac.toPyDate()
                fechaAct = datetime.datetime.now().date()
                delta = fechaAct - fechaNac
                pesoAct = doc1["content"]["peso"]
                acumPesos += pesoAct
                #fisico = (100*math.sin((math.pi*2*delta.days)/23))*pesoAct
                acumFisico += (100*math.sin((math.pi*2*delta.days)/23))*pesoAct
                #emocional = (100*math.sin((math.pi*2*delta.days)/28))*pesoAct
                acumEmo += (100*math.sin((math.pi*2*delta.days)/28))*pesoAct
                #intelectual = (100*math.sin((math.pi*2*delta.days)/33))*pesoAct
                acumIntel += (100*math.sin((math.pi*2*delta.days)/33))*pesoAct
            mediaF = acumFisico/acumPesos
            mediaE = acumEmo/acumPesos
            mediaI = acumIntel/acumPesos
            mediaT = (mediaF+mediaE+mediaI)/3                       
        else:
            print("Ese equipo no existe o no tiene jugadores")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
