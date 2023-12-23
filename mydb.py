import mysql.connector
import logging

#Configura el formato de los mensajes de logging
logging.basicConfig(format='%(message)s',level=logging.INFO)

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)

#Creacion del cursor
cursor_object = database.cursor()
#Creacion de la base de datos
cursor_object.execute("CREATE DATABASE distribuidorahgo_20231220")

#Mensaje de creacion exitosa
logging.info("Base de datos creada :)")
