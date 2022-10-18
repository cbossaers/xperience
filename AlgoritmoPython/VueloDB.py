from csv import excel_tab
from datetime import date, datetime
import json
from json import JSONEncoder
from lib2to3.pgen2.token import GREATEREQUAL
import string
from unicodedata import numeric
import psycopg2

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


def AddVuelo(id: int, fecha_salida: string, fecha_llegada: string, precio: numeric, companyia: string, ciudad_salida: string,
            ciudad_llegada: string, codigo_vuelo: string, precio_total: numeric, precio_base: numeric, tasas_cantidad: numeric):
    try:
        postgres_insert_query = """ INSERT INTO vuelo (id, fecha_salida, fecha_llegada, precio, companyia, ciudad_salida,
            ciudad_llegada, codigo_vuelo, precio_total, precio_base, tasas_cantidad) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (id, fecha_salida, fecha_llegada, precio,
                            companyia, ciudad_salida, ciudad_llegada, codigo_vuelo, precio_total, precio_base, tasas_cantidad)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

    vuelo = {
        "id": id, "fecha_salida": fecha_salida, "fecha_llegada": fecha_llegada, "precio": precio, "compañia": companyia, "ciudad_salida": ciudad_salida, 
        "ciudad_llegada": ciudad_llegada, "codigo_vuelo": codigo_vuelo, "precio_total": precio_total, "precio_base": precio_base, "tasas_cantidad": tasas_cantidad
    }
    return vuelo


def UpdateVuelo(id: int, fecha_salida: string, fecha_llegada: string, precio: numeric, companyia: string, ciudad_salida: string,
            ciudad_llegada: string, codigo_vuelo: string, precio_total: numeric, precio_base: numeric, tasas_cantidad: numeric):
    try:
        sql_update_query = """Update vuelo set fecha_salida = %s, fecha_llegada = %s, precio = %s, companyia = %s, ciudad_salida = %s,
            ciudad_llegada = %s, codigo_vuelo = %s, precio_total = %s, precio_base = %s, tasas_cantidad = %s where id = %s"""
        record_to_insert = (fecha_salida, fecha_llegada, precio, companyia, ciudad_salida, ciudad_llegada, codigo_vuelo,
                            precio_total, precio_base, tasas_cantidad, id)
        cursor.execute(sql_update_query, record_to_insert)
        connection.commit()

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

    vuelo = {
        "id": id, "fecha_salida": fecha_salida, "fecha_llegada": fecha_llegada, "precio": precio, "compañia": companyia, "ciudad_salida": ciudad_salida, 
        "ciudad_llegada": ciudad_llegada, "codigo_vuelo": codigo_vuelo, "precio_total": precio_total, "precio_base": precio_base, "tasas_cantidad": tasas_cantidad
    }
    return vuelo


def DeleteVuelo(id: int):
    try:
        sql_delete_query = """Delete from vuelo where id = %s"""
        cursor.execute(sql_delete_query, id)
        connection.commit()
        
    except Exception as error:
        raise error

    finally: 
        if connection:
            cursor.close()
            connection.close()

    return True
        


def GetVueloById(id: string):
    try:
        postgreSQL_select_Query = "select * from vuelo where id = %s"
        cursor.execute(postgreSQL_select_Query, id)

        columns = ('id', 'fecha_salida', 'fecha_llegada', 'precio', 'compañia', 'ciudad_salida',
                   'ciudad_llegada', 'codigo_vuelo', 'precio_total', 'precio_base', 'tasas_cantidad')
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