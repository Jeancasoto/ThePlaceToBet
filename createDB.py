from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb

#Hace la coneccion local automaticamente 
server = Server()

#Crear una database
db = server.create('theplacetobet')

print ('Programa finalizado con exito')

"""
msg = QMessageBox()
msg.setIcon(QMessageBox.Information)
msg.setText("Base de datos creada con exito")
"""