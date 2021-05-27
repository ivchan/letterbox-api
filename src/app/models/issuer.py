from app.models.connect import db


class Issuer(db.Model):
    __tablename__ = 'issuers'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self):
        self.id = ''
        self.name = ''
