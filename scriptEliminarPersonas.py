from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb
from random import randint 
from random import choice

server = Server()

db = server["quinelas"]

Personas = db.view("queries/getPersonas")

for persona in Personas:
    persona = persona.value
    db.delete(persona)
    print("Elimino: " + persona["_id"] + " - " + persona["content"]["nombre"])