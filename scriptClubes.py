num = int(raw_input("Cuantos clubes desea crear  :"))

from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb
from random import randint 
from random import choice
#from scriptClubes import IDs

lista_clubes =["F.C.Barcelona", "Real Madrid C.F.", "F.C. Bayern Munchen", "Manchester United F.C.","Juventus F.C.","Chelsea F.C.","Club Atletico de Madrid","Paris Saint-Germain F.C.","Borussia Dortmund","Manchester City F.C.","A.C. Milan","Arsenal F.C.","Liverpool F.C.","F.C. Inter de Milan","Valencia C.F.","S.S.C. Napoles","Tottenham Hotspur F.C.","A.S. Roma","F.C. Oporto","S.L. Benfica","Athletic Club","R.C.Deportivo de La Corunia","Schalke 04","Olympique de Lyon","Olympique de Marsella","S.C. Portugal","F.C. Zenit de San Petersburgo","FC Shakhtar Donetsk","Cadiz C.F.","CSKA Moscu","S.C. Braga","Montpellier HSC","FC.. Anzhi Majachkala","F.C. Rubin Kazan","Lille OSC","Abuelos F.C","Limon F.C","Huachipato","Llanfairpwllgwyngyll FC","Robin Hood","Independiente Bigote","Carabobo","Sacachispas","Semen Padang"]

#Hace la coneccion local automaticamente 
server = Server()

#Crear una database
db = server.create('test')

#Referirse a una base de datos ya existente
#db = server['test']

#Crear un documento
for i in range(num):
        
        doc = {
                '_id': lista_clubes[5],
                #'_rev': '1-0000000001',
                'content': {
                        'club': str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9)),
                        'integrantes': ["faltas","agregar","aun"]
                }
        }

db.save(doc)

print "script finalizado con exito"

