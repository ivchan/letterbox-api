import json

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models.connect import db
from app.models.user import User
from app.models.issuer import Issuer
from app.models.attachment import Attachment
from app.models.document_info import DocumentInfo

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:P@ssw0rd@localhost:3306/letterboxdb"
migrate = Migrate(app, db)
db.init_app(app)


# @app.route('/issuers')
# def get_issuers():
#     issuers = Issuer.objects()
#     return make_response(json.dumps(issuers), 200)
#
# @app.route('/issuers/<id>')
# def get_one_issuer(id: str):
#     issuer = Issuer.objects.first_or_404(id=id)
#     return issuer.to_dict(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
