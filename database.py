from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb

server = Server()

db = server.create("Prueba")

print("Base de datos creada exitosamente")