import datetime
from flask_mongoengine import MongoEngine
from app.models.connect import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    status = db.StringField()
    user_role = db.StringField()
    login_id = db.StringField()

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "user_role": self.user_role,
            "login_id": self.login_id
        }
