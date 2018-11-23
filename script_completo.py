#num = int(raw_input("Cuantas personas desea crear  :"))
num = 1000

from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb
from random import randint 
from random import choice

def numeros_de_identidad(num):
        lista_areas = ["0101","0102","0103","0104","0105","0106","0107","0108","0201","0202","0203","0204","0205","0206","0207","0208","0209","0210","0301","0302","0303","0304","0305","0306","0307","0308","0309","0310","0311","0312","0313","0314","0315","0316","0317","0318","0319","0320","0321","0401","0402","0403","0404","0405","0406","0407","0408","0409","0410","0411","0412","0413","0414","0415","0416","0417","0418","0419","0420","0421","0422","0423","0501","0502","0503","0504","0505","0506","0507","0508","0509","0510","0511","0512","0601","0602","0603","0604","0605","0606","0607","0608","0609","0610","0611","0612","0613","0614","0615","0616","0701","0702","0703","0704","0705","0706","0707","0708","0709","0710","0711","0712","0713","0714","0715","0716","0717","0718","0719","0801","0802","0803","0804","0805","0806","0807","0808","0809","0810","0811","0812","0813","0814","0815","0816","0817","0818","0819","0820","0821","0822","0823","0823","0825","0826","0827","0828"]
        lista_numeros =["0","1","2","3","4","5","6","7","8","9"]
        lista_no_IDs = list()

        while len(lista_no_IDs)<num:

                for i in range(num):
                        print ('va por la -->'), len(lista_no_IDs)

                        no_ID=lista_areas[randint(0,len(lista_areas)-1)]+"-"+str(randint(1940,2000))+"-"+lista_numeros[randint(0,len(lista_numeros)-1)]+lista_numeros[randint(0,len(lista_numeros)-1)]+lista_numeros[randint(0,len(lista_numeros)-1)]+lista_numeros[randint(0,len(lista_numeros)-1)]+lista_numeros[randint(0,len(lista_numeros)-1)]
                        print (str(no_ID))
                        if no_ID not in lista_no_IDs:
                                lista_no_IDs.append(no_ID)
                                print('Id agregado exitosamente')
                        else:
                                print('Ya existe ese ID')
        return lista_no_IDs

def fechas_nacimiento(num):
        lista_fechas_nac = list()

        while len(lista_fechas_nac)<num:

            for i in range(num):
                    print ('va por la -->'), len(lista_fechas_nac)

                    no_fecha_nac= str(randint(1,31))+"/"+str(randint(1,12))+"/"+str(randint(1940,2000))
                    print (str(no_fecha_nac))
                    lista_fechas_nac.append(no_fecha_nac)
                    print('fecha agregada exitosamente')
                    
        return lista_fechas_nac

def definir_personas(num):
        lista_personas = list()
        jugadores=0
        entrenadores=0
        arbitros=0
        while len(lista_personas)<num:

                for i in range(num):
                        print ('va por la -->'), len(lista_personas)

                        seleccionar= randint(0,10)
                        if (seleccionar<2):
                                lista_personas.append('Entrenador')
                                entrenadores+=1
                                print ('Se agrego Entrenador')
                                break
                        if (seleccionar>=8):
                                lista_personas.append('Arbitro')
                                print ('Se agrego Arbitro')
                                arbitros+=1
                                break
                        else:
                                lista_personas.append('Jugador')
                                print ('Se agrego Jugador')
                                jugadores+=1
                                break

        
        print('tipos de personas agregadas exitosamente')
        print('Jugadores-->',jugadores)
        print('Entrenadores-->',entrenadores)
        print('Arbitros-->',arbitros)
        print('total-->',jugadores+entrenadores+arbitros)

                     
        return lista_personas

#Lista de los tipos de personas resultantes
tipos_personas =definir_personas(num)
#Lista de numeros de identidad sin repetirse
IDs = numeros_de_identidad(num)
#Lista de fechas de nacimiento
fechas_nac = fechas_nacimiento(num)

listaNombres = ["Alfonso","Carlos","Emilio","Antonio","Nicolas","Eric","Erik","Daniel","Fidel","Ferran","Alejandro","Victor","Mariano","Galvan","Fermin","Guillem","Alfredo","Inaki","Lorenzo","Gil","Dario","Nacho","Aaron","Cesar","Feliciano","Marc","Andreu","Benjamin","Jacobo","Alberto","Javier","Javi","Xavier","Xavi","Roberto","Raul","Bruno","Ramon","Gabi","Gaby","Adam","Adan","Anael","Ignacio","Manuel","Hugo","Silvestre","Gaspar","Gustavo","Gregorio","German","Federico","Angel","Ivan","Felipe","Pau","Paulo","Pao","Paolo","Vicente","Gilberto","Ismael","Beltran","Aitor","Mauro","Jesus","Gaizka"]

listaApellidos = ["Martinez","Lopez","Rodriguez","Hernandez","Flores","Mejia","Garcia","Rivera","Reyes","Pineda","Cruz","Aguilar","Zelaya","Diaz","Sanchez","Castillo","Brarahona","Romero","Castro","Alvarado","Valladares","Velasquez","Gomez","Ramirez","Vasquez","Medina","Soto","Sanchez","Suazo","Varela","Borjas","Zuniga","Ortega","Moncada","Escobar","Estrada","Gonzalez","Ayala","Herrera","Rodas","Rojas","Castro","Roussel","Aparicio","Euceda","Cano","Carcamo","Galdamez","Sandoval","Martinez","Guevara","Pinto","Risso","Padgett","Matamoros","Mendoza","Lainez","Rivas","Obando","Dos Santos","Potter","Izaguirre","Altamirano","Azize","Deras","Timm","Goretzka"]

#Hace la coneccion local automaticamente 
server = Server()

#Crear una database
db = server.create('theplacetobet')

#Referirse a una base de datos ya existente
#db = server['theplacetobet']

#Crear un documento

for i in range(num):

        doc = {
        '_id': IDs[i],
        #'_rev': '1-0000000001',
        'content': {
                'nombre': listaNombres[randint(0,len(listaNombres)-1)],
                'apellido': listaApellidos[randint(0,len(listaApellidos)-1)],
                'fechaN': fechas_nac[i],
                'rol': tipos_personas[i],
                'peso':str(randint(1, 100)/100.00),
                'equipo':'N/A'
                }       
        }
        
        db.save(doc)
        print('Agregado a la base de datos, EXITOSO! --> ', i)

print ("script finalizado con exito")
print ("#####----PERSONAS CREADAS CON EXITO----######")

############### COMENZANDO A CREAR LOS CLUBES #################
num2= 25
lista_alfa = list()

def generar_alfanumerico(num2):
    lista_abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lista_numeros = ["0","1","2","3","4","5","6","7","8","9"]
    #lista_alfa = list()
    while len(lista_alfa)<num2:
        print ('va por la ---- ', len(lista_alfa))
        encontro = int 
        encontro =0
        for i in range(num2):
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

##### CREANDO CLUBES #######
def push_clubes_to_database(num2):
        for i in range(num2):
            #Crear un documento
            doc = {
                '_id': lista_alfa[i],
                #'_rev': '1-0000000001',
                'equipos': []
            }
            db.save(doc)
            print ("Agregado exitoso de club a la base de datos")
             
get_alfanumeric = generar_alfanumerico(num2)

ejec = push_clubes_to_database(num2)

print ("script finalizado con exito")
print ("#####----CLUBES CREADOS CON EXITO----######")

num3=40

contador_global =0



while contador_global <num3 :
    
    #print ('contador del while en---> '+ contador_global)

    print ("Contador en -->", str(contador_global))
    lista_equipos =["F.C.Barcelona", "Real Madrid C.F.", "F.C. Bayern Munchen", "Manchester United F.C.","Juventus F.C.","Chelsea F.C.","Club Atletico de Madrid","Paris Saint-Germain F.C.","Borussia Dortmund","Manchester City F.C.","A.C. Milan","Arsenal F.C.","Liverpool F.C.","F.C. Inter de Milan","Valencia C.F.","S.S.C. Napoles","Tottenham Hotspur F.C.","A.S. Roma","F.C. Oporto","S.L. Benfica","Athletic Club","R.C.Deportivo de La Corunia","Schalke 04","Olympique de Lyon","Olympique de Marsella","S.C. Portugal","F.C. Zenit de San Petersburgo","FC Shakhtar Donetsk","Cadiz C.F.","CSKA Moscu","S.C. Braga","Montpellier HSC","FC.. Anzhi Majachkala","F.C. Rubin Kazan","Lille OSC","Abuelos F.C","Limon F.C","Huachipato","Llanfairpwllgwyngyll FC","Robin Hood","Independiente Bigote","Carabobo","Sacachispas","Semen Padang"]

    lista_jugadores_disp = list()

    lista_plantilla = list()

    randal= randint(0,len(lista_equipos)-1)

    def jugadores_disponibles(num3):
        for i in range(len(IDs)-1):
            ppp = IDs[i]
            print ('sacando----'+str(ppp))
            selected_id = db[ppp]
            print ('selected id: '+selected_id['_id'])
            equipo_pertenece = selected_id['content']['equipo']
            print ('equipo pertenece: '+equipo_pertenece)
            if equipo_pertenece == 'N/A':
                print('Encontro N/A')
                lista_jugadores_disp.append(selected_id['_id'])
                print('Hizo apend')
            else:
                print ('Tiene equipo ya')

        print ('jugadores sin equipo '+ str(len(lista_jugadores_disp)) )

    def plantilla_para_equipo(num3):
        for i in range(16):
            lista_plantilla.append(lista_jugadores_disp[i])

        print ('lista de 16 jugadores creada con exito')

    
    def push_to_database(num3):
        #for i in range(40):
            #randy= randint(0,len(lista_equipos)-1)

        #Crear un documento
        doc = {
            '_id': lista_equipos[contador_global],
            #'_rev': '1-0000000001',
            'content': {
                'club': lista_alfa[randint(0,len(lista_alfa)-1)],
                'integrantes': lista_plantilla
            }
        }
        db.save(doc)

        print ('Agrego exitosamente el equipo'+ lista_equipos[contador_global])

    def actualizar_jugadores(num3):
        for i in range(len(lista_plantilla)-1):
            #ppp = IDs[i]
            #print ('sacando----'+str(ppp))
            selected_id = db[lista_plantilla[i]]
            #print ('selected id: '+selected_id['_id'])
            selected_id['content']['equipo'] = str(lista_equipos[contador_global])
            db.save(selected_id)
            #print ('equipo pertenece: '+equipo_pertenece)
            #if equipo_pertenece == 'N/A':
            #    print('Encontro N/A')
            #    lista_jugadores_disp.append(selected_id['_id'])
            #    print('Hizo apend')
            #else:
            #    print 'Tiene equipo ya'

        #print ('jugadores sin equipo '+ str(len(lista_jugadores_disp)) )
        print ('Jugadores deben tener ya los equipos asignados')



    sacar_jugadores_disp = jugadores_disponibles(num3)

    sacar_plantilla = plantilla_para_equipo(num3)

    agregar_equipo = push_to_database(num3)

    update_players= actualizar_jugadores(num3)

    contador_global+=1 

print ("script finalizado con exito")
print ("#####----EQUIPOS CREADOS CON EXITO----######")


def actualizar_clubes(num2):

    for i in range(len(lista_alfa)-1):
        nomina_equipos = []
        #ppp = IDs[i]
        #print ('sacando----'+str(ppp))
        selected_id = db[lista_alfa[i]]
        print ('selected id: '+ selected_id['_id'])
        for j in range(num2):
            new_selected_id = db[lista_equipos[j]]
            print ('new selected id: '+ new_selected_id['_id'])
            perteneciente = new_selected_id['content']['club']
            print ('perteneciente: '+ perteneciente)
            if perteneciente == selected_id['_id'] :
                print ('Se encontro coincidencia')
                if perteneciente not in nomina_equipos:
                    nomina_equipos.append(new_selected_id['_id'])
                    print ('Se hizo append')
                else:
                    print ('ya existia')
            else:
                print ('No se encontro coincidencia')
        
        if len(nomina_equipos)>0:
            selected_id['equipos'] = nomina_equipos
            db.save(selected_id)   
        else:
            print ('No hubieron cambios')
        print ('se debio guardar: '+ str(len(nomina_equipos)) + 'para el club' + selected_id['_id'] )

        #print ('selected id: '+selected_id['_id'])
        #####selected_id['content']['equipos'] = str(lista_equipos[contador_global])
        #####db.save(selected_id)
        #print ('equipo pertenece: '+equipo_pertenece)
        #if equipo_pertenece == 'N/A':
        #    print('Encontro N/A')
        #    lista_jugadores_disp.append(selected_id['_id'])
        #    print('Hizo apend')
        #else:
        #    print 'Tiene equipo ya'

    #print ('jugadores sin equipo '+ str(len(lista_jugadores_disp)) )
    print ('Clubes deben tener ya los equipos correspondientes')

update_clubes = actualizar_clubes(num2)

print ("script finalizado con exito")
print ("#####----CLUBES ACTUALIZADOS CON EXITO----######")
print ('###########################################')
print ('###########################################')
print ("#########-FIN EXITOSO DEL SCRIPT-##########")
print ('###########################################')
print ('###########################################')
