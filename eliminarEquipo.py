from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb

server = Server()

db = server["quinelas"]

Personas = db.view("queries/getEquipos")

for persona in Personas:
    persona = persona.value
    db.delete(persona)
    print("Elimino: " + persona["_id"])