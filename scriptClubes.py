#num = int(raw_input("Cuantos clubes desea crear  :"))
num =40


from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb
from random import randint 
from random import choice
#from scriptClubes import IDs

#Hace la coneccion local automaticamente 
server = Server()

#Crear una database
#db = server.create('quinelas')

#Referirse a una base de datos ya existente
db = server['test']

contador_global =1

while contador_global <num :
        
        print ("Contador en -->", contador_global)
        lista_equipos =["F.C.Barcelona", "Real Madrid C.F.", "F.C. Bayern Munchen", "Manchester United F.C.","Juventus F.C.","Chelsea F.C.","Club Atletico de Madrid","Paris Saint-Germain F.C.","Borussia Dortmund","Manchester City F.C.","A.C. Milan","Arsenal F.C.","Liverpool F.C.","F.C. Inter de Milan","Valencia C.F.","S.S.C. Napoles","Tottenham Hotspur F.C.","A.S. Roma","F.C. Oporto","S.L. Benfica","Athletic Club","R.C.Deportivo de La Corunia","Schalke 04","Olympique de Lyon","Olympique de Marsella","S.C. Portugal","F.C. Zenit de San Petersburgo","FC Shakhtar Donetsk","Cadiz C.F.","CSKA Moscu","S.C. Braga","Montpellier HSC","FC.. Anzhi Majachkala","F.C. Rubin Kazan","Lille OSC","Abuelos F.C","Limon F.C","Huachipato","Llanfairpwllgwyngyll FC","Robin Hood","Independiente Bigote","Carabobo","Sacachispas","Semen Padang"]

        lista_plantilla = list()

        randal= randint(0,len(lista_equipos)-1)

        def jugadores_disponibles(self):
                #Declaro las dos lista a usar
                lista_jugadores_disp = list()
                #a una lista le asigno el view
                lista_jugadores_disp = db.view('queries/getJugadoresSinEquipo')
                #a esa misma list quiero dejarla solo con el _id
                lista_jugadores_disp = lista_jugadores_disp["key"]

                #Decision que me deja entrar solo en caso de que existan jugadores suficientes 
                if len(lista_jugadores_disp)>15:
                        #un for de 0-15 por los 16 jugadores en total que tiene un equipo
                        for i in range(15):
                                lista_plantilla.append(str(lista_jugadores_disp[i]))
                else:
                        print ('No existen jugadores suficientes')
                
"""
docClub = {
        '_id': idClub,
        'content': {
        'equipos': listaEquipos
        }
}
"""

        def push_clubes_to_database(num):
                for i in range(num):
                #Crear un documento
                doc = {
                        '_id': lista_alfa[i],
                        #'_rev': '1-0000000001',
                        'equipos': []
                }
                db.save(doc)
                print ("Agregado exitoso de club a la base de datos")
            
get_alfanumeric = generar_alfanumerico(num)

ejec = push_clubes_to_database(num)
"""
        def push_clubes_to_database(self):
                #Crear un documento
                doc = {
                        '_id': ,
                        #'_rev': '1-0000000001',
                        'equipos': []
                }
                db.save(doc)
"""
        def push_to_database(self):
                
                #Crear un documento
                doc = {
                        '_id': lista_equipos[randal],
                        #'_rev': '1-0000000001',
                        'content': {
                                'club': str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9)),
                                'integrantes': lista_plantilla
                        }
                }
                db.save(doc)

        def actualizar_jugadores(self):
                for i in range(lista_plantilla):
                        jugador = db.get(i)
                        jugador["content"]["club"] = lista_equipos[randal]
                        db.save(jugador)

        #agregar uno al contador global
        contador_global +=1



print ("script finalizado con exito")

"""

from random import randint

equipos = ['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P']

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
            print "No se ha jugado en otra fecha"
            lista_partidos_totales.append(partido)
            if partido not in lista_partidos:
                print ("No se ha jugado esta jornada")
                lista_partidos.append(partido)
            else:
                print "El partido ya se jugo en esta jornada "
        else:
            print 'El partido ya se jugo en otra fecha aparentemente'
    
    print "Jornada-> ", contador_jornada
    print "Lista partidos:"
    #for j in len(lista_partidos):
    #    print 'Juego:'+j+" "+lista_partidos[j]
    print lista_partidos
    
    contador_jornada+=1

"""