from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)

app.config['SECRET_KEY'] = '12345'
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['MYSQL_DATABASE_HOST'] ='maxim45.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] ='maxim45'
app.config['MYSQL_DATABASE_PASSWORD'] ='Pass11word'
app.config['MYSQL_DATABASE_DB'] ='maxim45$library_db'

mysql = MySQL()
mysql.init_app(app)