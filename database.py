import sqlite3
from sqlite3 import Error

def create_connection():

    conn = None
    try:
        conn = sqlite3.connect('attendance.db')
    except Error as e:
        print(e)
    return conn
