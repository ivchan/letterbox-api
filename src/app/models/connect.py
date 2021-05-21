from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://admin:password@localhost:27017/letterboxdb?authSource=admin'
}
db = MongoEngine()
db.init_app(app)
