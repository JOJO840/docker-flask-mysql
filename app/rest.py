import pymysql
from app import app
from db import mysql
from flask import Flask, jsonify, request

@app.route('/persons', methods=['GET'])
def persons():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    request.method == 'GET'

    cursor.execute("SELECT * FROM persons")
    conn.commit()

    rows = cursor.fetchall()        
    resp = jsonify(rows)
    resp.status_code = 200

    return resp

@app.route('/persons/POST', methods=['POST'])
def persons_post():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    request.method == 'POST'

    cursor.execute("INSERT INTO persons (id, name, email, phone, adress) values (3, Petter, Earth2 ) ")
    conn.commit()

    rows = cursor.fetchall()        
    resp = jsonify(rows)
    resp.status_code = 200

    return resp


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')