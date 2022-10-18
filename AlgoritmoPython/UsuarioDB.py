from csv import excel_tab
from datetime import date, datetime
import json
from json import JSONEncoder
from lib2to3.pgen2.token import GREATEREQUAL
import string
import psycopg2
from psycopg2.extras import RealDictCursor

# Conexión a la BDD (importar desde fichero externo?)
try:
    connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.121.110",
                                  port="5432",
                                  database="bluesky")
    cursor = connection.cursor(cursor_factory = RealDictCursor)
except Exception as error:
    raise error


def AddUsuario(id: int, nombre: string, apellidos: string, correo: string, telefono: string, fechaNac: string,
               dni: string, dirPost: string, dirFac: string, contra: string):
    try:
        postgres_insert_query = """ INSERT INTO usuario (id, nombre, apellidos, correo, telefono, fecha_nacimiento,
            dni, direccion_postal, direccion_facturacion, contrasenya) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (id, nombre, apellidos, correo,
                            telefono, fechaNac, dni, dirPost, dirFac, contra)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

    usuario = {
        "id":id, "nombre":nombre, "apellidos":apellidos, "correo": correo, "telefono": telefono, "fechaNacimiento": fechaNac, 
        "dni": dni, "direccionPostal": dirPost, "direccionFacturacion": dirFac, "contraseña": contra
    }
    return usuario


def UpdateUsuario(id: int, nombre: string, apellidos: string, correo: string, telefono: string, fechaNac: string,
                  dni: string, dirPost: string, dirFac: string, contra: string):
    try:
        sql_update_query = """Update usuario set nombre = %s, apellidos = %s, correo = %s, telefono = %s, fecha_nacimiento = %s,
            dni = %s, direccion_postal = %s, direccion_facturacion = %s, contrasenya = %s where id = %s"""
        record_to_insert = (nombre, apellidos, correo, telefono,
                            fechaNac, dni, dirPost, dirFac, contra, id)
        cursor.execute(sql_update_query, record_to_insert)
        connection.commit()

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

    usuario = {
        "id":id, "nombre":nombre, "apellidos":apellidos, "correo": correo, "telefono": telefono, "fechaNacimiento": fechaNac, 
        "dni": dni, "direccionPostal": dirPost, "direccionFacturacion": dirFac, "contraseña": contra
    }
    return usuario


def DeleteUsuario(id: int):
    try:
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
        postgreSQL_select_Query = "select * from usuario where correo = {s}".format(s = correo)
        cursor.execute(postgreSQL_select_Query)

        columns = ('id', 'nombre', 'apellidos', 'correo', 'telefono',
                   'fecha_nacimiento', 'dni', 'direccion_postal', 'direccion_facturacion', 'contrasenya')
        results = []
        
        for usuario in cursor.fetchall():
            results.append(dict(zip(columns, usuario)))

        return json.dumps(results)

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

def GetUsuarioById(id: string):
    try:
        postgreSQL_select_Query = "select * from usuario where id = %s"
        cursor.execute(postgreSQL_select_Query, id)

        columns = ('id', 'nombre', 'apellidos', 'correo', 'telefono',
                   'fecha_nacimiento', 'dni', 'direccion_postal', 'direccion_facturacion', 'contrasenya')
        results = []

        for usuario in cursor.fetchall():
            results.append(dict(zip(columns, usuario)))

        return json.dumps(results)

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

#except (Exception, psycopg2.Error) as error:
#        print("Error while fetching data from PostgreSQL", error)
print(GetUsuarioByCorreo("'prueba'"))