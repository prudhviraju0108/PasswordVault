from flask import Flask, render_template,request
import mysql.connector
import yaml
from flask_mysqldb import MySQL


app = Flask(__name__)

db = yaml.load(open("db.yaml"))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        user_name = userdetails['user_name']
        password = userdetails['password']
        cursor = mysql.connecton.cursor
        cursor.execute("INSERT into details(name,user_name,password) VALUES(%s, %s, %s)",(name,user_name,password))
        mysql.connection.commit
        cursor.close()
        return "success"
    return render_template('index.html')


app.run()