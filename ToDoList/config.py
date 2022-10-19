from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e7756c504ff5c2310add47019cefeb00'
app.config['MONGO_URI'] = 'mongodb+srv://dp_maxim:Pass11word@cluster0.j4hvnsy.mongodb.net/db1?retryWrites=true&w=majority'
mongo = PyMongo(app)
