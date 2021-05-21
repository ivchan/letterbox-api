import uuid
from flask import Flask
from app.models.connect import db
from app.models.user import User
from app.models.issuer import Issuer

app = Flask(__name__)

if __name__ == '__main__':
    db.create_all()
    # key = uuid.uuid4()
    # u = User()
    # u.id = key
    # u.name = "my name"
    # u.status = "active"
    # db.session.add(u)
    # db.session.commit()
    #exit()
    app.run(host='0.0.0.0', port=5000)
