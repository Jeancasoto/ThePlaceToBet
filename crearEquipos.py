
"""
#num = int(raw_input("Cuantos clubes desea crear  :"))
num =40


from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb
from random import randint 
from random import choice

lista_alfa = list()

def generar_alfanumerico(num):
    lista_abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lista_numeros = ["0","1","2","3","4","5","6","7","8","9"]
    #lista_alfa = list()
    while len(lista_alfa)<num:
        print ('va por la ---- ' + str(len(lista_alfa)))
        encontro = int 
        encontro =0
        for i in range(num):
            cadena = lista_abecedario[randint(0,len(lista_abecedario)-1)] + lista_numeros[randint(0,len(lista_numeros)-1) ] + lista_abecedario[randint(0,len(lista_abecedario)-1)] +  lista_numeros[randint(0,len(lista_numeros)-1) ] + lista_abecedario[randint(0,len(lista_abecedario)-1)] +  lista_numeros[randint(0,len(lista_numeros)-1) ]
            if(len(lista_alfa)==0):
                print ('estaba vacia')
                lista_alfa.append(cadena)
            else:
                #for m in range (len(lista_alfa)):
                if cadena in lista_alfa:
                    encontro +=1
                    #print encontro
                if encontro == 0:
                    lista_alfa.append(cadena)
                    #print 'no encontro'
                    encontro=0
                else:
                   # print 'no hizo ni pija'
                    encontro=0
        print ('va por la ---- ' + str(len(lista_alfa)))
        #print lista_alfa
    #return lista_alfa

#Hace la coneccion local automaticamente 
server = Server()

#Crear una database
#db = server.create('quinelas')

#Referirse a una base de datos ya existente
db = server['quinelas']


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


contador_global =1

while contador_global <num :
        
    print ("Contador en -->" + str(contador_global))
    lista_equipos =["F.C.Barcelona", "Real Madrid C.F.", "F.C. Bayern Munchen", "Manchester United F.C.","Juventus F.C.","Chelsea F.C.","Club Atletico de Madrid","Paris Saint-Germain F.C.","Borussia Dortmund","Manchester City F.C.","A.C. Milan","Arsenal F.C.","Liverpool F.C.","F.C. Inter de Milan","Valencia C.F.","S.S.C. Napoles","Tottenham Hotspur F.C.","A.S. Roma","F.C. Oporto","S.L. Benfica","Athletic Club","R.C.Deportivo de La Corunia","Schalke 04","Olympique de Lyon","Olympique de Marsella","S.C. Portugal","F.C. Zenit de San Petersburgo","FC Shakhtar Donetsk","Cadiz C.F.","CSKA Moscu","S.C. Braga","Montpellier HSC","FC.. Anzhi Majachkala","F.C. Rubin Kazan","Lille OSC","Abuelos F.C","Limon F.C","Huachipato","Llanfairpwllgwyngyll FC","Robin Hood","Independiente Bigote","Carabobo","Sacachispas","Semen Padang"]

    lista_plantilla = list()

    randal= randint(0,len(lista_equipos)-1)

    def jugadores_disponibles(num):
            #Declaro las dos lista a usar
            lista_jugadores_disp = list()
            #a una lista le asigno el view
            lista_jugadores_dispon = db.view('queries/getJugadoresSinEquipo')
            #a esa misma list quiero dejarla solo con el _id
            lista_jugadores_disp = list()
            for jug in lista_jugadores_dispon:
                jug = jug.key
                lista_jugadores_disp.append(jug)

            #Decision que me deja entrar solo en caso de que existan jugadores suficientes 
            #if len(lista_jugadores_disp)>=15:
                #un for de 0-15 por los 16 jugadores en total que tiene un equipo
            for i in range(15):
                    print(str(lista_jugadores_disp[i]))
                    lista_plantilla.append(str(lista_jugadores_disp[i]))
        #else:
            #print ('No existen jugadores suficientes')


    
    def push_to_database(num):
            for i in range(40):
                #randy= randint(0,len(lista_equipos)-1)

                valor = (len(lista_alfa)) - 1
 
                #Crear un documento
                doc = {
                        '_id': lista_equipos[i],
                        #'_rev': '1-0000000001',
                        'content': {
                                'club': lista_alfa[randint(0,valor)],
                                'integrantes': lista_plantilla
                        }
                }
                db.save(doc)

    def actualizar_jugadores(num):
            for jugadorID in lista_plantilla:
                    jugador = db.get(jugadorID)
                    jugador["content"]["club"] = str(lista_equipos[randal])
                    db.save(jugador)

    #agregar uno al contador global
    contador_global +=1

get_jugadores= jugadores_disponibles(num)

agregar_couch = push_to_database(num)

#actualizar_lista =actualizar_jugadores(num)

print ("script finalizado con exito")
"""
#num = int(raw_input("Cuantos clubes desea crear  :"))
num =40

from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb
from random import randint 
from random import choice

lista_alfa = list()

def generar_alfanumerico(num):
    lista_abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lista_numeros = ["0","1","2","3","4","5","6","7","8","9"]
    #lista_alfa = list()
    while len(lista_alfa)<num:
        print ('va por la ---- '+ str(len(lista_alfa)))
        encontro = int 
        encontro =0
        for i in range(num):
            cadena = lista_abecedario[randint(0,len(lista_abecedario)-1)] + lista_numeros[randint(0,len(lista_numeros)-1) ] + lista_abecedario[randint(0,len(lista_abecedario)-1)] +  lista_numeros[randint(0,len(lista_numeros)-1) ] + lista_abecedario[randint(0,len(lista_abecedario)-1)] +  lista_numeros[randint(0,len(lista_numeros)-1) ]
            if(len(lista_alfa)==0):
                print ('estaba vacia')
                lista_alfa.append(cadena)
            else:
                #for m in range (len(lista_alfa)):
                if cadena in lista_alfa:
                    encontro +=1
                    #print encontro
                if encontro == 0:
                    lista_alfa.append(cadena)
                    #print 'no encontro'
                    encontro=0
                else:
                   # print 'no hizo ni pija'
                    encontro=0
        print ('va por la ---- '+ str(len(lista_alfa)))
        #print lista_alfa
    #return lista_alfa

#Hace la coneccion local automaticamente 
server = Server()

#Crear una database
#db = server.create('quinelas')

#Referirse a una base de datos ya existente
db = server['quinelas']


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


contador_global =1

while contador_global <num :
        
    print ("Contador en -->"+ str(contador_global))
    lista_equipos =["F.C.Barcelona", "Real Madrid C.F.", "F.C. Bayern Munchen", "Manchester United F.C.","Juventus F.C.","Chelsea F.C.","Club Atletico de Madrid","Paris Saint-Germain F.C.","Borussia Dortmund","Manchester City F.C.","A.C. Milan","Arsenal F.C.","Liverpool F.C.","F.C. Inter de Milan","Valencia C.F.","S.S.C. Napoles","Tottenham Hotspur F.C.","A.S. Roma","F.C. Oporto","S.L. Benfica","Athletic Club","R.C.Deportivo de La Corunia","Schalke 04","Olympique de Lyon","Olympique de Marsella","S.C. Portugal","F.C. Zenit de San Petersburgo","FC Shakhtar Donetsk","Cadiz C.F.","CSKA Moscu","S.C. Braga","Montpellier HSC","FC.. Anzhi Majachkala","F.C. Rubin Kazan","Lille OSC","Abuelos F.C","Limon F.C","Huachipato","Llanfairpwllgwyngyll FC","Robin Hood","Independiente Bigote","Carabobo","Sacachispas","Semen Padang"]

    lista_plantilla = list()

    randal= randint(0,len(lista_equipos)-1)

    def jugadores_disponibles(num):
            #Declaro las dos lista a usar
            lista_jugadores_disp = list()
            #a una lista le asigno el view
            lista_jugadores_dispon = db.view('queries/getJugadoresSinEquipo')
            #a esa misma list quiero dejarla solo con el _id
            lista_jugadores_disp = list()
            for jug in lista_jugadores_dispon:
                jug = jug.key
                lista_jugadores_disp.append(jug)

            #Decision que me deja entrar solo en caso de que existan jugadores suficientes 
            #if len(lista_jugadores_disp)>=15:
                #un for de 0-15 por los 16 jugadores en total que tiene un equipo
            for i in range(15):
                    print(str(lista_jugadores_disp[i]))
                    lista_plantilla.append(str(lista_jugadores_disp[i]))
        #else:
            #print ('No existen jugadores suficientes')


    
    def push_to_database(num):
            for i in range(40):
                #randy= randint(0,len(lista_equipos)-1)
 
                #Crear un documento
                doc = {
                        '_id': lista_equipos[i],
                        #'_rev': '1-0000000001',
                        'content': {
                                'club': lista_alfa[randint(0,len(lista_alfa)-1)],
                                'integrantes': lista_plantilla
                        }
                }
                db.save(doc)

    def actualizar_clubes(num):
            #for que recorre todos los clubes creados
            for i in range(len(lista_alfa)-1):
                #declarar una nueva lista
                new_team_list = list()
                club = db.get(lista_alfa[i])
                #for que recorre todos los equipos creados
                for j in range(len(lista_equipos)): 
                    #obtener cual es el id del equipo en este momento
                    equipo = db.get(lista_equipos[i])
                    #obtener cual es el club al que pertenece el equipo en este momento
                    member_of = equipo["content"]["club"]
                    #decision para poder agregar a la lista
                    if (member_of == club):
                        #agregar a la nueva lista el id del equipo
                        new_team_list.append(str(equipo))
                    else:
                        print (str(equipo)+'No es miembro del club'+ str(club))
            if len(new_team_list) is not 0:
                club["content"]["equipos"] = str(new_team_list) 
                db.save(club)
            else:
                print ('No se encontraron equipos miembros del club'+ str(club))

    #agregar uno al contador global
    contador_global +=1

get_jugadores= jugadores_disponibles(num)

agregar_couch = push_to_database(num)

#actualizar_lista =actualizar_jugadores(num)

update_clubes = actualizar_clubes(num)

print ("script finalizado con exito")