import json
import numbers
from sqlite3 import Date
import string
from csv import excel_tab
from datetime import date, datetime
from json import JSONEncoder
from lib2to3.pgen2.token import GREATEREQUAL

import psycopg2
from psycopg2.extras import RealDictCursor


def AddUsuario(correo: string, contr: string, nombre: string, apellidos: string, telefono: numbers, fechaNacimiento: Date, dni: string, dirPost: string, dirFac: string):
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.114.199",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
        postgres_insert_query = """INSERT INTO usuario VALUES (%s,%s,%s,%s) ON CONFLICT (correo) DO UPDATE 
            SET contrasenya= %s, nombre = %s, apellidos = %s, telefono = %s, fechaNacimiento = %s, dni = %s, direccionpostal = %s, direccionfacturacion = %s;"""
        record_to_insert = (correo, contr, nombre, apellidos, contr, nombre, apellidos, telefono, fechaNacimiento, dni, dirPost, dirFac)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

        
    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

def DeleteUsuario(id: int):
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.26.37",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
        sql_delete_query = """Delete from usuario where id = %s"""
        cursor.execute(sql_delete_query, id)
        connection.commit()
        
    except Exception as error:
        raise error

    finally: 
        if connection:
            cursor.close()
            connection.close()

    return True
        
def GetUsuarioByCorreo(correo: string):
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.26.37",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from usuario where correo = {s}".format(s = correo)
        cursor.execute(postgreSQL_select_Query)

        columns = ('id', 'nombre', 'apellidos', 'correo', 'telefono',
                   'fecha_nacimiento', 'dni', 'direccion_postal', 'direccion_facturacion', 'contrasenya')
        results = {}

        for usuario in cursor.fetchall():
            results[usuario[0]] = dict()
            for i in range(len(usuario)):
                results[usuario[0]][columns[i]] = usuario[i]
            
        return results

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

#except (Exception, psycopg2.Error) as error:
#        print("Error while fetching data from PostgreSQL", error)
print(AddUsuario('CORREO2', 'abc123','César','Ayuso Cervera', 2,'30/05/2001', None, None, None))