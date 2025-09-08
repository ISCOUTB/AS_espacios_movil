import mysql.connector

def get_connection():

    return mysql.connector.connect(host="localhost", user="root", password="Bul@salas_06", database="Espacios_db")