import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'econdata'

TABLES = {}
TABLES['key_words'] = ("CREATE TABLE keywords (keyword VARCHAR(100), possible_inputs VARCHAR(500), PRIMARY KEY(keyword)) ENGINE=InnoDB")

cnx = mysql.connector.connect(user = 'oliver', password = 'olianett', port = '8889',  host = '127.0.0.1', database = DB_NAME)
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
                "CREATE DATABASE {} DEAFULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.items():
    try:
        print("CREATING table {}: ".format(name), end = '')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("table already exists")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
