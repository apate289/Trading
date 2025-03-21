from flaskext.mysql import MySQL
from flask import Flask
import MySQLdb

app = Flask(__name__)

#msql = MySQL()
#app.config['MYSQL_HOST'] = "localhost"
#app.config['MYSQL_DATABASE_USER'] = "Ankit"
#app.config['MYSQL_DATABASE_PASSWORD'] = "Ankit@134"
#app.config['MYSQL_DATABASE_DB'] = "productdb" #"client_stocks"

#msql.init_app(app)

db=MySQLdb.connect(host="localhost",user="Ankit",
                  password="Ankit@134",database="productdb")