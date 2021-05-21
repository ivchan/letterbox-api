from datetime import datetime

from app.models.connect import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.now())
    last_update_time = db.Column(db.DateTime, onupdate=datetime.now(), default=datetime.now())
    status = db.Column(db.String(10), nullable=False)

    def __init__(self):
        self.id = ""
        self.name = ""
        self.status = ""
