from flask import Flask
from app.models.connect import db
from app.models.user import User
from app.models.issuer import Issuer

app = Flask(__name__)

if __name__ == '__main__':
    u2 = User()
    u2.name = "Administrator"
    u2.status = "active"
    u2.login_id = "admin"
    u2.save();
    app.run(host='0.0.0.0', port=5000)
