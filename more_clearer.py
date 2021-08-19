import mysql.connector as connector

def connection():
    config = {
        "user": "root",
        "password": "",
        "host": "localhost",
        "database": 'apis'
    }
    try:
        c = connector.connect(**config)
        return [True, c]
    except:
        return [False, 0]