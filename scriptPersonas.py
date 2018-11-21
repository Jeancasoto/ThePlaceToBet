num = int(raw_input("Cuantas personas desea crear  :"))

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
                        print 'va por la -->', len(lista_no_IDs)

                        no_ID=lista_areas[randint(0,len(lista_areas)-1)]+"-"+str(randint(1940,2000))+"-"+lista_numeros[randint(0,len(lista_numeros)-1)]+lista_numeros[randint(0,len(lista_numeros)-1)]+lista_numeros[randint(0,len(lista_numeros)-1)]+lista_numeros[randint(0,len(lista_numeros)-1)]+lista_numeros[randint(0,len(lista_numeros)-1)]
                        print str(no_ID)
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
                        print 'va por la -->', len(lista_fechas_nac)

                        no_fecha_nac= str(randint(1,31))+"/"+str(randint(1,12))+"/"+str(randint(1940,2000))
                        print str(no_fecha_nac)
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
                        print 'va por la -->', len(lista_personas)

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
db = server.create('test')

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
                'peso':str(randint(1, 100)/100.00)
                }       
        }
        
        db.save(doc)
        print('Agregado a la base de datos, EXITOSO! --> ', i)

print "script finalizado con exito"

