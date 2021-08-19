import mysql.connector as connector

def connection(host='localhost', user='root', passwd='', database=None):
    connection = connector.connect(host=host, user=user, passwd=passwd, database=database)
    if connection:
        return [True, connection]
    else:
        return [False, 0]