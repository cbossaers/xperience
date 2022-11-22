from csv import excel_tab
from datetime import date, datetime
import json
from json import JSONEncoder
from lib2to3.pgen2.token import GREATEREQUAL
import string
from unicodedata import numeric
import psycopg2
from psycopg2.extras import RealDictCursor
from decimal import *


def GetHotelById(id: string):   #¡¡¡¡¡cambiar tipos decimal a float en BD para que funcione!!!!!
    try:
        connection = psycopg2.connect(user="pi",
                                  password="pi",
                                  host="88.17.26.37",
                                  port="5432",
                                  database="bluesky")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from hotel where id = %s"
        cursor.execute(postgreSQL_select_Query, id)

        columns = ('id', 'tipo', 'chain_code', 'id_amadeus', 'dupe_id', 'nombre',
                   'num_estrellas', 'codigo_ciudad', 'latitud', 'longitud')
        results = {}

        for hotel in cursor.fetchall():
            results[hotel[0]] = dict()
            for i in range(len(hotel)):
                results[hotel[0]][columns[i]] = hotel[i]
            
        return results

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

print(GetHotelById("1"))