from app.models.connect import db


class Issuer(db.Document):
    name = db.StringField()

    def to_json(self):
        return {
            "name": self.name
        }