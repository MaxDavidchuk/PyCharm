from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd9249af539f2b86d61f250a9945033b6'
app.config['MONGO_URI'] = 'mongodb+srv://admin123:Admin_123@cluster1.nufw3xc.mongodb.net/db1?retryWrites=true&w=majority'
mongo = PyMongo(app)
