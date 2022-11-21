import string
from unicodedata import numeric
import psycopg2
from decimal import *

def AddVuelo(id: int, fecha_salida: string, fecha_llegada: string, precio: numeric, companyia: string, ciudad_salida: string,
            ciudad_llegada: string, codigo_vuelo: string, precio_total: numeric, precio_base: numeric, tasas_cantidad: numeric):
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.114.199",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
        postgres_insert_query = " INSERT INTO vuelo VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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
        "id": id, "fecha_salida": fecha_salida, "fecha_llegada": fecha_llegada, "precio": precio, "companyia": companyia, "ciudad_salida": ciudad_salida, 
        "ciudad_llegada": ciudad_llegada, "codigo_vuelo": codigo_vuelo, "precio_total": precio_total, "precio_base": precio_base, "tasas_cantidad": tasas_cantidad
    }
    return vuelo


def UpdateVuelo(id: int, fecha_salida: string, fecha_llegada: string, precio: numeric, companyia: string, ciudad_salida: string,
            ciudad_llegada: string, codigo_vuelo: string, precio_total: numeric, precio_base: numeric, tasas_cantidad: numeric):
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.114.199",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
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
        "id": id, "fecha_salida": fecha_salida, "fecha_llegada": fecha_llegada, "precio": precio, "companyia": companyia, "ciudad_salida": ciudad_salida, 
        "ciudad_llegada": ciudad_llegada, "codigo_vuelo": codigo_vuelo, "precio_total": precio_total, "precio_base": precio_base, "tasas_cantidad": tasas_cantidad
    }
    return vuelo


def DeleteVuelo(id: int):
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.114.199",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
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
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.114.199",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from vuelo where id = %s"
        cursor.execute(postgreSQL_select_Query, id)

        columns = ('id', 'fecha_salida', 'fecha_llegada', 'precio', 'companyia', 'ciudad_salida',
                   'ciudad_llegada', 'codigo_vuelo', 'precio_total', 'precio_base', 'tasas_cantidad')
        results = []

        for vuelo in cursor.fetchall():
            aux = dict()

            for i in range(len(vuelo)):
                aux[columns[i]] = vuelo[i]

            results.append(aux)
            
        return results 

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

def GetVueloByOriDest(Origen: string, Destino: string):
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.114.199",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from vuelo where ciudad_salida = %s and ciudad_llegada = %s"
        cursor.execute(postgreSQL_select_Query, (Origen, Destino))

        columns = ('id', 'fecha_salida', 'fecha_llegada', 'precio', 'companyia', 'ciudad_salida',
                   'ciudad_llegada', 'codigo_vuelo', 'precio_total', 'precio_base', 'tasas_cantidad')
        results = []

        for vuelo in cursor.fetchall():
            aux = dict()

            for i in range(len(vuelo)):
                aux[columns[i]] = vuelo[i]

            results.append(aux)
            
        return results 

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

def GetVueloByOriFecha(origen: string, fechaSalida: string, fechaLlegada: string):
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.114.199",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from vuelo where ciudad_salida = %s and fecha_salida = %s and fecha_llegada = %s"
        cursor.execute(postgreSQL_select_Query, (origen, fechaSalida, fechaLlegada))

        columns = ('id', 'fecha_salida', 'fecha_llegada', 'precio', 'companyia', 'ciudad_salida',
                   'ciudad_llegada', 'codigo_vuelo', 'precio_total', 'precio_base', 'tasas_cantidad')

        results = []

        for vuelo in cursor.fetchall():
            aux = dict()

            for i in range(len(vuelo)):
                aux[columns[i]] = vuelo[i]

            results.append(aux)
            
        return results 

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

def GetVueloByFechaPrecio(fechaSalida: string, fechaLLegada: string, importe: string):
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.114.199",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from vuelo where fecha_salida = %s and fecha_llegada = %s and precio_total <= %s"
        cursor.execute(postgreSQL_select_Query, (fechaSalida, fechaLLegada, importe))

        columns = ('id', 'fecha_salida', 'fecha_llegada', 'precio', 'companyia', 'ciudad_salida',
                'ciudad_llegada', 'codigo_vuelo', 'precio_total', 'precio_base', 'tasas_cantidad')
 
        results = []

        for vuelo in cursor.fetchall():
            aux = dict()

            for i in range(len(vuelo)):
                aux[columns[i]] = vuelo[i]

            results.append(aux)
            
        return results 

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

# print(GetVueloByOriDest("prueba1", "prueba2"))
#print(GetVueloByOriFecha("prueba1", "2022-03-01", "2022-03-01"))
#x = GetVueloByFechaPrecio('2022-03-01','2022-03-01',100)
#print(x)
#filename = "./AlgoritmoPython/endpoint/data.json"
#with open(filename, "w") as outfile:
#    json.dump(x, outfile, indent=4)
