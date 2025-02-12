from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)

msql = MySQL()
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_DATABASE_USER'] = "admin"
app.config['MYSQL_DATABASE_PASSWORD'] = "YES"
app.config['MYSQL_DATABASE_DB'] = "client_stocks"

msql.init_app(app)