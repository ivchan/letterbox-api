import datetime

from app.models.connect import db


class Attachment(db.Model):
    __tablename__ = 'attachments'
    id = db.Column(db.String(36), nullable=False, primary_key=True)
    file_type = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(36), nullable=False)
    storage_file_name = db.Column(db.String(100), nullable=False)
    uploaded_file_name = db.Column(db.String(100), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable=True)
    upload_by = db.Column(db.String(20), nullable=True)

    def __init__(self):
        self.file_type = ''
        self.location = ''
        self.storage_file_name = ''
        self.uploaded_file_name = ''
        self.upload_time = datetime.datetime.utcnow()
        self.upload_by = ''

