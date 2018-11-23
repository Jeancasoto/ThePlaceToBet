import sys
from random import randint
from PyQt4 import QtCore, QtGui, uic
from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb
import datetime
#from datetime import datetime
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
        #Llamar metodo para salir del sistema
        self.boton_salir.clicked.connect(self.salir)
        #Cargar los equipos al combobox y agentes libres en Modificar
        self.cargar_cbEquipos.clicked.connect(self.cargarComboModificar)
        #Cargar la plantilla del equipo seleccionado en el combo Modificar
        self.comboBox_7.currentIndexChanged.connect(self.cargarPlantillasModificar)
        #Agregar jugadores agentes libres a Equipo seleccionado
        self.pushButton_3.clicked.connect(self.agregarAgenteLibre)
        #Despedir jugador y volverlo agente libre
        self.pushButton_2.clicked.connect(self.despedirJugador)
        #Cargar equipos a la lista de crear temporada
        self.cargarEquiposTemp.clicked.connect(self.cargarEquiposTemporada)
        #Agregar equipos a la temporada nueva
        self.botonAgregarEquipo_2.clicked.connect(self.agregarEquiposTemporada)
        #Crear temporada
        self.botonCrearTemp.clicked.connect(self.crearTemporada)
        #Actualizar combobox temporadas
        self.botonTemporadas.clicked.connect(self.cargarComboTemporadas)
        #Completar los datos de jornada en Jugar
        self.comboBox.currentIndexChanged.connect(self.cargarComboJornada)
        #Completar los datos de enfrentamiento en Jugar
        self.comboBox_2.currentIndexChanged.connect(self.cargarComboEnfrentamiento)
        #Cargar los datos de arbitros, coaches y jugadores
        self.botonPartidos.clicked.connect(self.cargarDatosPartido)
        #Cargar todo para visualizar :v
        self.combo_consulta.currentIndexChanged.connect(self.listarTODO)
        #Calcular el pronostico del resultado
        self.pushButton.clicked.connect(self.simulacionPartido)
        #Comandos para simular un group button :v
        self.radioButton.toggled.connect(self.radio_isSelected)
        self.radioButton_2.toggled.connect(self.radio_isSelected)
        self.radioButton_3.toggled.connect(self.radio_isSelected)

    #Metodo al accionar el boton de exit
    def salir(self):
        sys.exit()
        print ('Salir del sistema exitoso')
    
    def autenticar(self):
        input_username = str(self.username.text())
        input_password = str(self.password.text())
        if input_username == "admin":
            print ('Username encontrado')
            if  input_password == 'admin':
                print ('Password encontrado')
                self.verObjetos.setTabEnabled(1, True)
                self.verObjetos.setTabEnabled(2, True)
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
                    'peso': peso,
                    'equipo': "N/A"
                }
            }
            db.save(docPersona)
        else:
            print("Ya existe una persona con ese ID")
        #-----faltaria hacer el insert aqui-----

    def listarJugadores(self):
        serverCDB = Server()
        db = serverCDB['quinelas']

        lists = db.view('queries/getJugadoresSinEquipo')
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
        global jugadoresAgregados
        nJugadores = jugadoresAgregados
        print("*******************")
        for i in range(0,len(nJugadores)):
            print(nJugadores[i])
        print("********************")
        
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

            for id in nJugadores:
                jugador = db.get(id)
                jugador["content"]["equipo"] = nEquipo
                db.save(jugador)

            print("Agregado exitosamente!")
        else:
            print("Ya existe un equipo con ese ID")
        self.lista_jugadores_disp.clear()
        self.lista_jugadores_ag.clear()
        jugadoresAgregados = []

    def transferirJugadores(self):
        global jugadoresAgregados
        temporal = jugadoresAgregados
        for JugadorSelec in self.lista_jugadores_disp.selectedItems():
            #tempo = self.lista_jugadores_disp.currentItem()
            value = JugadorSelec.text()
            value = value.split("-")
            idSuazo = value[0]+"-"+value[1]+"-"+value[2]
            temporal.append(idSuazo)
            print(idSuazo)    
            self.lista_jugadores_disp.takeItem(self.lista_jugadores_disp.row(JugadorSelec))
            self.lista_jugadores_ag.addItem(JugadorSelec)
        #jugadoresAgregados.append(self.lista_jugadores_disp.currentRow())
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
        """
        equiposSinClub = db.view('queries/getEquiposSinClub')

        for equipo in equiposSinClub:
            equipo = equipo.value
            row = equipo["_id"]
            if row.split("-")[0] == "2017"
                print(row)
                self.listaEquiposDisp.addItem(row)"""

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
        #Ejemplo de como modificar
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

    #Metodo para calcular el bioritmo promedio para un equipo
    def calcularBioritmos(self, jKey):

        #Este metodo calcula el bioritmo para un EQUIPO
        #Calcula el bioritmo para cada jugador individual, los suma y saca la media ponderada
        #Luego, saca la media de los 3 bioritmos (fis, emo, int)

        print("CALCULAR BIORITMOS")
        serverCDB = Server()
        db = serverCDB['quinelas']
        docJ = db[jKey]
        pesoAct = float(docJ["content"]["peso"])
        print("pesoAct: "+str(pesoAct))
        nacJ = docJ["content"]["fechaN"]
        fechaN = datetime.datetime.strptime(nacJ, '%d/%m/%Y')
        fechaAct = datetime.date.today().strftime("%d/%m/%Y")
        fechaAct = datetime.datetime.strptime(fechaAct, '%d/%m/%Y')
        delta = fechaAct - fechaN
        #fisico = (100*math.sin((math.pi*2*delta.days)/23))*pesoAct
        acumFisico = (100*math.sin((math.pi*2*delta.days)/23))*pesoAct
        print("acumFisico: "+str(acumFisico))
        #emocional = (100*math.sin((math.pi*2*delta.days)/28))*pesoAct
        acumEmo = (100*math.sin((math.pi*2*delta.days)/28))*pesoAct
        print("acumEmo: "+str(acumEmo))
        #intelectual = (100*math.sin((math.pi*2*delta.days)/33))*pesoAct
        acumIntel = (100*math.sin((math.pi*2*delta.days)/33))*pesoAct
        print("acumIntel: "+str(acumIntel))
        mediaP = (acumFisico+acumEmo+acumIntel)/(3*pesoAct)
        print("mediaP: "+str(mediaP))
        return mediaP

    #Metodo que agrega los equipos al combobox en modificar
    def cargarComboModificar(self):
        #Limpiar las listas
        self.listWidget_2.clear()
        #Agregar los equipos al combobox
        self.comboBox_7.clear()
        serverCDB = Server()
        db = serverCDB['quinelas']
        equipos = db.view('queries/getEquipos')
        listaTemporal = []
        for equipo in equipos:
            equipo = equipo.value
            cbItem = equipo["_id"]
            listaTemporal.append(cbItem)
        self.comboBox_7.addItems(listaTemporal)
        self.cargarAgentesLibre()
        
    #Metodo que carga los jugadores Agentes Libre
    def cargarAgentesLibre(self):
        self.listWidget_2.clear()
        serverCDB = Server()
        db = serverCDB['quinelas']
        jugadores = db.view('queries/getJugadoresSinEquipo')
        for jugador in jugadores:
            docTemp = jugador.value
            listRow = docTemp["_id"]+"-"+docTemp["content"]["nombre"]+"-"+docTemp["content"]["apellido"]+"-"+str(docTemp["content"]["peso"])
            self.listWidget_2.addItem(listRow)  
    
    #Metodo que carga los jugadores del equipo seleccionado del cb en Modificar
    def cargarPlantillasModificar(self):
        self.listWidget.clear()
        print("PLANTILLAS EQUIPOS")
        serverCDB = Server()
        db = serverCDB['quinelas']
        #Agregar los jugadores del equipo seleccionado cb
        equipoKey = str(self.comboBox_7.currentText())
        equipo = db[equipoKey]
        jugadores = equipo["content"]["integrantes"]
        for jugador in jugadores:
            actual = db[jugador]
            listRow = actual["_id"]+"-"+actual["content"]["nombre"]+"-"+actual["content"]["apellido"]+"-"+str(actual["content"]["peso"])
            self.listWidget.addItem(listRow)

    #Metodo que agrega al equipo un jugador agente libre
    def agregarAgenteLibre(self):
        if(len(self.listWidget_2.selectedItems())>0):
            listaNuevos = []
            serverCDB = Server()
            db = serverCDB['quinelas']
            for jugador in self.listWidget_2.selectedItems():
                value = jugador.text()
                value = value.split("-")
                idJ = value[0]+"-"+value[1]+"-"+value[2]
                listaNuevos.append(idJ)
                docJugador = db[idJ]
                docJugador["content"]["equipo"] = str(self.comboBox_7.currentText())
                db.save(docJugador)       
                self.listWidget_2.takeItem(self.listWidget_2.row(jugador))
            equipoKey = str(self.comboBox_7.currentText())
            equipo = db[equipoKey]
            plantillaAct = equipo["content"]["integrantes"]
            plantillaAct = plantillaAct + listaNuevos
            equipo["content"]["integrantes"] = plantillaAct
            db.save(equipo)
            self.cargarPlantillasModificar()
        else:
            print("ERROR! Debe elegir un elemento de la lista Agente Libre")

    #Metodo que despide a un jugador del equipo en Modificar
    def despedirJugador(self):
        if(len(self.listWidget.selectedItems()) > 0):
            serverCDB = Server()
            db = serverCDB['quinelas']
            equipo = db[str(self.comboBox_7.currentText())]
            plantillaAct = equipo["content"]["integrantes"]
            for jugador in self.listWidget.selectedItems():
                value = jugador.text()
                value = value.split("-")
                idJ = value[0]+"-"+value[1]+"-"+value[2]
                plantillaAct.remove(idJ)
                docJ = db[idJ]
                docJ["content"]["equipo"]="N/A"
                db.save(docJ)
                self.listWidget.takeItem(self.listWidget.row(jugador))
            equipo["content"]["integrantes"] = plantillaAct
            db.save(equipo)
            self.cargarAgentesLibre()
        else:
            print("ERROR! Debe elegir un elemento de la lista Plantilla")
        
    def cargarEquiposTemporada(self):
        self.equiposDisp.clear()
        self.equiposPart.clear()
        serverCDB = Server()
        db = serverCDB['quinelas']
        equipos = db.view('queries/getEquipos')
        listaTemporal = []
        for equipo in equipos:
            equipo = equipo.value
            IDEquipo = equipo["_id"]
            listaTemporal.append(IDEquipo)
            self.equiposDisp.addItem(IDEquipo)

    def agregarEquiposTemporada(self):
        for EquipoSelec in self.equiposDisp.selectedItems():
            self.equiposDisp.takeItem(self.equiposDisp.row(EquipoSelec))
            self.equiposPart.addItem(EquipoSelec)

    def crearTemporada(self):
        serverCDB = Server()
        db = serverCDB['quinelas']

        if len(self.texIntTemporada.text()) > 0:
            anoTemp = self.texIntTemporada.text()
            equipos = [] 
            for index in range(self.equiposPart.count()): 
                equipos.append(str(self.equiposPart.item(index).text()))

            for id_equipo in equipos:
                equipo = db.get(id_equipo)
                #saca el club del equipo
                club = db.get(equipo["content"]["club"])
                if club == "N/A":
                    print("ERROR! Equipo sin Club")
                    return

            docTemp = {
                "_id": anoTemp,
                "content":{
                    "equipos": equipos
                }
            }

            db.save(docTemp)
            
            contador_jornada =1

            #existe una lista de los enfrentamientos ya disputados donde no pueden disputarse mas de 1 vez por temporada
            #def enfrentamientos(self):  
            lista_partidos_totales =[]
            #cada jornada tiene 14 partidos (n-1)
            jornada =contador_jornada
            #existen equipos locales y visitantes 
            for i in range(len(equipos)):
                lista_partidos = []
                while len(lista_partidos) <14:
                    ran1=randint(0,len(equipos)-1)
                    ran2=randint(0,len(equipos)-1)
                    partido = equipos[ran1]+"-"+equipos[ran2]
                    if partido not in lista_partidos_totales:
                        print ("No se ha jugado en otra fecha")
                        lista_partidos_totales.append(partido)
                        if partido not in lista_partidos:
                            print ("No se ha jugado esta jornada")
                            lista_partidos.append(partido)
                        else:
                            print ("El partido ya se jugo en esta jornada ")
                    else:
                        print ('El partido ya se jugo en otra fecha aparentemente')
                
                print ("Jornada-> " + str(contador_jornada))
                print ("Lista partidos:")
                #for j in len(lista_partidos):
                #    print 'Juego:'+j+" "+lista_partidos[j]
                print (lista_partidos)

                #Escoger Jugadores
                for encuentro in lista_partidos:
                    #Validacion por si dos equipos del mismo club se enfrentan
                    listaJugadoresUsados = []

                    #----------Local-------------

                    id_equipo = encuentro.split("-")[0]
                    print(id_equipo)
                    equipo = db.get(id_equipo)
                    #saca el club del equipo
                    club = db.get(equipo["content"]["club"])
                    print(equipo["content"]["club"])

                    jugadores_temp = []

                    #saca los equipos del club
                    for equipoClub in club["content"]["equipos"]:
                        equipoClub = db.get(equipoClub)
                        #saca los integrantes de los equipos
                        for jugadorClub in equipoClub["content"]["integrantes"]:
                            #y lo agrega
                            jugadores_temp.append(jugadorClub)

                    #agrega los tutulares random
                    jugadores_Titulares = []
                    for i in range(11):
                        jugRan = randint(0, len(jugadores_temp)-1)
                        jugadores_Titulares.append(jugadores_temp[jugRan])
                        listaJugadoresUsados.append(jugadores_temp[jugRan])
                        jugadores_temp.pop(jugRan)

                    #agrega los suplentes random
                    jugadores_Suplentes = []
                    for i in range(5):
                        jugRan = randint(0, len(jugadores_temp)-1)
                        jugadores_Suplentes.append(jugadores_temp[jugRan])
                        listaJugadoresUsados.append(jugadores_temp[jugRan])
                        jugadores_temp.pop(jugRan)

                    tecnicoE = db.view("queries/getEntrenador")
                    #tecnicoE = tecnicoE[randint(0,len(tecnicoE))]
                    tecnicoEs = []
                    for tec in tecnicoE:
                        tec = tec.key
                        tecnicoEs.append(tec)

                    foo = randint(0, len(tecnicoEs) - 1)
                    print(tecnicoEs[foo])
                    vari = tecnicoEs[foo]

                    #Crea el doc con toda la info necesaria
                    docLocal = {
                        "nombre": equipo["_id"],
                        "jugadores_titulares": jugadores_Titulares,
                        "jugadores_suplentes": jugadores_Suplentes,
                        "entrenador": vari
                    }

                    #----------Visita---------

                    id_equipo = encuentro.split("-")[1]
                    equipo = db.get(id_equipo)
                    #saca el club del equipo
                    club = db.get(equipo["content"]["club"])

                    jugadores_temp = []

                    #saca los equipos del club
                    for equipoClub in club["content"]["equipos"]:
                        equipoClub = db.get(equipoClub)
                        #saca los integrantes de los equipos
                        for jugadorClub in equipoClub["content"]["integrantes"]:
                            #y lo agrega

                            #con la condicion extra
                            if jugadorClub not in listaJugadoresUsados:
                                jugadores_temp.append(jugadorClub)

                    #agrega los tutulares random
                    jugadores_Titulares = []
                    for i in range(11):
                        jugRan = randint(0, len(jugadores_temp)-1)
                        jugadores_Titulares.append(jugadores_temp[jugRan])
                        listaJugadoresUsados.append(jugadores_temp[jugRan])
                        jugadores_temp.pop(jugRan)

                    #agrega los suplentes random
                    jugadores_Suplentes = []
                    for i in range(5):
                        jugRan = randint(0, len(jugadores_temp)-1)
                        jugadores_Suplentes.append(jugadores_temp[jugRan])
                        listaJugadoresUsados.append(jugadores_temp[jugRan])
                        jugadores_temp.pop(jugRan)

                    tecnicoE = db.view("queries/getEntrenador")
                    #tecnicoE = tecnicoE[randint(0,len(tecnicoE))]
                    tecnicoEs = []
                    for tec in tecnicoE:
                        tec = tec.key
                        tecnicoEs.append(tec)

                    foo = randint(0, len(tecnicoEs) - 1)
                    print(tecnicoEs[foo])
                    vari = tecnicoEs[foo]

                    #Crea el doc con toda la info necesaria
                    docVisita = {
                        "nombre": equipo["_id"],
                        "jugadores_titulares": jugadores_Titulares,
                        "jugadores_suplentes": jugadores_Suplentes,
                        "entrenador": vari
                    }

                    arbitros = []
                    listaArbitrosV = db.view("queries/getArbitros")
                    listaArbitros = []
                    for arb in listaArbitrosV:
                        listaArbitros.append(arb.key)

                    for i in range(4):
                        posArbitro = randint(0, len(listaArbitros) - 1)
                        arbitros.append(listaArbitros[posArbitro])
                        listaArbitros.pop(posArbitro)

                    #FINALMENTE EL DOC DE PARTIDO

                    docPartido = {
                        "_id": str(anoTemp) + "-" + str(contador_jornada) + "-" + encuentro.split("-")[0] + "-" + encuentro.split("-")[1],
                        "content":{
                            "jornada": contador_jornada,
                            "local": docLocal,
                            "visita": docVisita,
                            "arbitros": arbitros,
                            "score_local": "N/A",
                            "score_visita": "N/A"

                        }
                    }
                    db.save(docPartido)

                contador_jornada+=1

    """#Metodo para cargar los yrs de las temporadas en el combo en Jugar"""
    def cargarComboTemporadas(self):
        self.comboBox.clear()
        serverCDB = Server()
        db = serverCDB['quinelas']
        temporadas = db.view('queries/getPartidas')
        listaYrs = []
        for temporada in temporadas:
            docTemp = temporada.value
            idT = docTemp["_id"]
            listaTempo = idT.split("-")
            idT = listaTempo[0]
            if idT not in listaYrs:
                listaYrs.append(idT)
        self.comboBox.addItems(listaYrs)

    #Metodo para llenar cb de Jornada
    def cargarComboJornada(self):
        #print("HOLAAAAAAAAAAA")
        self.comboBox_2.clear()
        serverCDB = Server()
        db = serverCDB["quinelas"]
        temporadas = db.view("queries/getPartidas")
        itemActual = str(self.comboBox.currentText())
        listaJornadas = []
        for temporada in temporadas:
            docTemp = temporada.value
            idT = docTemp["_id"]
            listaTempo = idT.split("-")
            idT = listaTempo[0]
            #print(idT)
            #print(itemActual)
            if itemActual == idT:
                #print("*******")
                #print(listaTempo[1])
                if listaTempo[1] not in listaJornadas:
                    listaJornadas.append(listaTempo[1])
        listHols = []
        for i in range (0,len(listaJornadas)):
            x = int(listaJornadas[i])
            listHols.append(x)
        listHols.sort()
        listaJornadas.clear()
        for i in range (0,len(listHols)):
            x = str(listHols[i])
            listaJornadas.append(x)
        self.comboBox_2.addItems(listaJornadas)

    #Metodo para cargar los enfrentamientos en el combobox
    def cargarComboEnfrentamiento(self):
        self.comboBox_3.clear()
        serverCDB = Server()
        db = serverCDB["quinelas"]
        temporadas = db.view("queries/getPartidas")
        jornadaActual = str(self.comboBox_2.currentText())
        temporadaActual = str(self.comboBox.currentText())
        listaEnfrentamientos = []
        for temporada in temporadas:
            docTemp = temporada.value
            idT = docTemp["_id"]
            listaTempo = idT.split("-")
            idT = listaTempo[0]
            idJ = listaTempo[1]
            if jornadaActual == idJ and temporadaActual == idT:
                enfren = listaTempo[2]+"-"+listaTempo[3]
                if enfren not in listaEnfrentamientos:
                    listaEnfrentamientos.append(enfren)
        self.comboBox_3.addItems(listaEnfrentamientos)

    #Metodo para cargar los arbitros, coaches, jugadores
    def cargarDatosPartido(self):
        idT = str(self.comboBox.currentText())
        idJ = str(self.comboBox_2.currentText())
        idE = str(self.comboBox_3.currentText())
        myKey = idT+"-"+idJ+"-"+idE
        print(myKey)
        serverCDB = Server()
        db = serverCDB["quinelas"]
        temporadas = db.view("queries/getPartidas")
        myDoc = db[myKey]

        #Recuperar los datos del local
        localDoc = myDoc["content"]["local"]
        jugadores = localDoc["jugadores_titulares"]
        for i in range(0, len(jugadores)):
            jugadorDoc = db[jugadores[i]]
            nombre = jugadorDoc["content"]["nombre"]+" "+jugadorDoc["content"]["apellido"]
            self.tableWidget_3.setItem(i , 0, QtGui.QTableWidgetItem(nombre))
        for i in range(0,len(jugadores)):
            docJ = db[jugadores[i]]
            media = self.calcularBioritmos(docJ["_id"])
            media = round(media,2)
            #print(media)                                          
            self.tableWidget_3.setItem(i , 1, QtGui.QTableWidgetItem(str(media)))
        #Entrenador local
        entrenador = localDoc["entrenador"]
        entrenador = db[entrenador]
        nombreA = entrenador["content"]["nombre"]+" "+entrenador["content"]["apellido"]
        self.tableWidget_2.setItem(0, 0, QtGui.QTableWidgetItem(nombreA))

        #Recuperar los datos del visitante
        visitDoc = myDoc["content"]["visita"]
        jugadores = visitDoc["jugadores_titulares"]
        for i in range(0, len(jugadores)):
            jugadorDoc = db[jugadores[i]]
            nombre = jugadorDoc["content"]["nombre"]+" "+jugadorDoc["content"]["apellido"]
            self.tableWidget_4.setItem(i , 0, QtGui.QTableWidgetItem(nombre))
        for i in range(0,len(jugadores)):
            docJ = db[jugadores[i]]
            media = self.calcularBioritmos(docJ["_id"])
            media = round(media,2)
            #print(media)
            self.tableWidget_4.setItem(i , 1, QtGui.QTableWidgetItem(str(media)))
        #Entrenador visita
        entrenador = visitDoc["entrenador"]
        entrenador = db[entrenador]
        nombreA = entrenador["content"]["nombre"]+" "+entrenador["content"]["apellido"]
        self.tableWidget_2.setItem(1, 0, QtGui.QTableWidgetItem(nombreA))

        #Arbitros
        arbitros = myDoc["content"]["arbitros"]
        for arbitro in arbitros:
            pArbitro = db[arbitro]
            nombreAr = pArbitro["content"]["nombre"]+" "+pArbitro["content"]["apellido"]
            self.tableWidget.setItem(arbitros.index(arbitro), 0, QtGui.QTableWidgetItem(nombreAr))

    def listarTODO(self):
        self.list_con_datos.clear()

        serverCDB = Server()
        db = serverCDB["quinelas"]

        #Toma la seleccion actual
        objAct = self.combo_consulta.currentIndex()

        print(objAct)

        if objAct == 0:
            #Listar Personas
            personasDB = db.view("queries/getPersonas")
            for persona in personasDB:
                persona = persona.value
                IDPersona = persona["_id"]
                persona = db.get(IDPersona)
                nombreP = persona["content"]["nombre"]
                apellidoP = persona["content"]["apellido"]
                fechaP = persona["content"]["fechaN"]
                pesoP = persona["content"]["peso"]
                self.list_con_datos.addItem("ID: " + IDPersona + " - Nombre: " + nombreP + " " + apellidoP + " - Fecha Nacimiento: " + fechaP + " - Peso: " + pesoP)
        elif objAct == 1:
            #Listar Jugadores
            personasDB = db.view("queries/getJugadores")
            for persona in personasDB:
                persona = persona.value
                IDPersona = persona["_id"]
                persona = db.get(IDPersona)
                nombreP = persona["content"]["nombre"]
                apellidoP = persona["content"]["apellido"]
                fechaP = persona["content"]["fechaN"]
                pesoP = persona["content"]["peso"]
                self.list_con_datos.addItem("ID: " + IDPersona + " - Nombre: " + nombreP + " " + apellidoP + " - Fecha Nacimiento: " + fechaP + " - Peso: " + pesoP)
        elif objAct == 2:
            #Listar Entrenadores
            personasDB = db.view("queries/getEntrenador")
            for persona in personasDB:
                persona = persona.value
                IDPersona = persona["_id"]
                persona = db.get(IDPersona)
                nombreP = persona["content"]["nombre"]
                apellidoP = persona["content"]["apellido"]
                fechaP = persona["content"]["fechaN"]
                pesoP = persona["content"]["peso"]
                self.list_con_datos.addItem("ID: " + IDPersona + " - Nombre: " + nombreP + " " + apellidoP + " - Fecha Nacimiento: " + fechaP + " - Peso: " + pesoP)
            pass
        elif objAct == 3:
            #Listar Arbitros
            personasDB = db.view("queries/getArbitros")
            for persona in personasDB:
                persona = persona.value
                IDPersona = persona["_id"]
                persona = db.get(IDPersona)
                nombreP = persona["content"]["nombre"]
                apellidoP = persona["content"]["apellido"]
                fechaP = persona["content"]["fechaN"]
                pesoP = persona["content"]["peso"]
                self.list_con_datos.addItem("ID: " + IDPersona + " - Nombre: " + nombreP + " " + apellidoP + " - Fecha Nacimiento: " + fechaP + " - Peso: " + pesoP)
            pass
        elif objAct == 4:
            #Listar Equipos
            equiposDB = db.view("queries/getEquipos")
            for equipo in equiposDB:
                equipo = equipo.value
                IDEquipo = equipo["_id"]
                equipo = db.get(IDEquipo)
                clubE = equipo["content"]["club"]
                self.list_con_datos.addItem("Nombre: " + IDEquipo + " - Club: " + clubE + " - Integrantes: ")
                for integrante in equipo["content"]["integrantes"]:
                    self.list_con_datos.addItem("--- ID: " + integrante)
            pass
        elif objAct == 5:
            #Listar Clubes
            pass
        elif objAct == 6:
            #Listar Jornadas
            pass
        elif objAct == 7:
            #Listar Partidos
            pass

    def simulacionPartido(self):
        acumLocal = 0
        acumVisita = 0
        for i in range(0,10):
            item1 = self.tableWidget_3.itemAt(i, 1)
            item2 = self.tableWidget_4.itemAt(i, 1)
            acumLocal += float(item1.text())
            acumVisita += float(item2.text())
        mediaLocal = acumLocal/11
        mediaVisita = acumVisita/11
        golesLocal = int(round(mediaLocal/5))
        print("Local: "+golesLocal)
        golesVisita = int(round(mediaVisita/5))
        print("Visita: "+golesVisita)
        self.label_54.setText(str(golesLocal))
        self.label_56.setText(str(golesVisita))
        apuesta = float(self.labelMoney.getText())
        if (golesLocal > golesVisita and self.radioButton.isChecked()) or (golesLocal < golesVisita and self.radioButton_3.isChecked()) or (golesLocal == golesVisita and self.radioButton_2.isChecked()):
            apuesta*= 1.5
            self.labelMoney.setText(str(apuesta))
        elif (golesLocal < golesVisita and self.radioButton.isChecked()) or (golesLocal > golesVisita and self.radioButton_3.isChecked()) or (golesLocal != golesVisita and self.radioButton_3.isChecked()):
            apuesta*= 0.75
            self.labelMoney.setText(str(apuesta))
        else:
            self.labelMoney.setText(str(apuesta))

    def radio_isSelected(self):
        if self.radioButton.isChecked():
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(False)
        elif self.radioButton_2.isChecked():
            self.radioButton.setChecked(False)
            self.radioButton_3.setChecked(False)
        elif self.radioButton_3.isChecked():
            self.radioButton_2.setChecked(False)
            self.radioButton.setChecked(False)

    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())