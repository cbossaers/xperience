# from asyncore import write
# import asyncio
from datetime import date, datetime
# import imp
import json
from json import JSONEncoder
from lib2to3.pgen2.token import GREATEREQUAL
import string
import psycopg2
import psycopg2.extensions as ext

# Conexión a la BDD (importar desde fichero externo?)
try:
    connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.121.110",
                                  port="5432",
                                  database="bluesky")
    cursor = connection.cursor()
except Exception as error:
    raise error


def AddUsuario(id: int, nombre: string, apellidos: string, correo: string, telefono: string, fechaNac: string,
               dni: string, dirPost: string, dirFac: string, contra: string):

    postgres_insert_query = """ INSERT INTO usuario (id, nombre, apellidos, correo, telefono, fecha_nacimiento,
        dni, direccion_postal, direccion_facturacion, contrasenya) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (id, nombre, apellidos, correo,
                        telefono, fechaNac, dni, dirPost, dirFac, contra)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()

    # Cerrar conexión (a implementar en fichero externo)
    cursor.close()
    connection.close()
    return CrearJson(id, nombre, apellidos, correo, telefono, fechaNac, dni, dirPost, dirFac, contra)


def UpdateUsuario(id: int, nombre: string, apellidos: string, correo: string, telefono: string, fechaNac: string,
                  dni: string, dirPost: string, dirFac: string, contra: string):

    sql_update_query = """Update usuario set nombre = %s, apellidos = %s, correo = %s, telefono = %s, fecha_nacimiento = %s,
        dni = %s, direccion_postal = %s, direccion_facturacion = %s, contrasenya = %s where id = %s"""
    record_to_insert = (nombre, apellidos, correo, telefono,
                        fechaNac, dni, dirPost, dirFac, contra, id)
    cursor.execute(sql_update_query, record_to_insert)

    connection.commit()

    # Cerrar conexión (a implementar en fichero externo)
    cursor.close()
    connection.close()
    return CrearJson(id, nombre, apellidos, correo, telefono, fechaNac, dni, dirPost, dirFac, contra)


def DeleteUsuario(id: int, nombre: string, apellidos: string, correo: string, telefono: string, fechaNac: string,
                  dni: string, dirPost: string, dirFac: string, contra: string):

    sql_delete_query = """Delete from usuario where id = %s"""
    cursor.execute(sql_delete_query, id)

    connection.commit()

    # Cerrar conexión (a implementar en fichero externo)
    cursor.close()
    connection.close()
    return CrearJson(id, nombre, apellidos, correo, telefono, fechaNac, dni, dirPost, dirFac, contra)


def GetUsuario(id: string):
    try:
        postgreSQL_select_Query = "select * from usuario where id = %s"
        cursor.execute(postgreSQL_select_Query, id)

        # usuario = cursor.fetchall()
        columns = ('id', 'nombre', 'apellidos', 'correo', 'telefono',
                   'fecha_nacimiento', 'dni', 'direccion_postal', 'direccion_facturacion', 'contrasenya')
        results = []

        for usuario in cursor.fetchall():
            results.append(dict(zip(columns, usuario)))

        return json.dumps(results)

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# Método para crear un Json de Return con los datos del Usuario


def CrearJson(id: int, nombre: string, apellidos: string, correo: string, telefono: string, fechaNac: string,
              dni: string, dirPost: string, dirFac: string, contra: string):

    value = {
        "id": id,
        "nombre": nombre,
        "apellidos": apellidos,
        "correo": correo,
        "telefono": telefono,
        "fecha_nacimiento": fechaNac,
        "dni": dni,
        "direccion_postal": dirPost,
        "direccion_facturacion": dirFac,
        "contrasenya": contra
    }
    return value


class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime)):
            return obj.isoformat()


print(GetUsuario("1"))
