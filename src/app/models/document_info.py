import datetime

from app.models.connect import db


class DocumentInfo(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    issuer = db.Column(db.String(200), nullable=True)
    subject = db.Column(db.String(200), nullable=True)
    ref_no = db.Column(db.String(100), unique=True, nullable=True)
    status = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, nullable=True)
    last_update_time = db.Column(db.DateTime, nullable=True)

    def __init__(self):
        self.id = ''
        self.issuer = ''
        self.subject = ''
        self.ref_no = ''
        self.status = ''
