from crypt import methods
import pymysql
from requests import post
from app import app
from db import mysql
from flask import Flask, jsonify, render_template, request

@app.route('/', methods=[GET, POST]) 
def persons():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM persons")

    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200

    return resp


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')