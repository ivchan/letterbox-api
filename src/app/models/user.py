from app.models.connect import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=True)
    status = db.Column(db.String(10), nullable=False)
    user_role = db.Column(db.String(10), nullable=False)
    login_id = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self):
        self.id = ''
        self.name = ''
        self.email = ''
        self.status = ''
        self.user_role = ''
        self.login_id = ''
