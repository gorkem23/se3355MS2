import pymysql

from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="new"
)

@app.route('/')
def index():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
