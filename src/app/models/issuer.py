import datetime
from flask_mongoengine import MongoEngine
from app.models.connect import db


class Issuer(db.Document):
    name = db.StringField()
    create_time = db.DateTimeField()
    last_update_time = db.DateTimeField()
    status = db.StringField()

    def __init__(self):
        self.id = ""
        self.name = ""
        self.status = ""
