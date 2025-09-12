from flask import Flask, request
import mysql.connector
from mysql.connector import Error




app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)