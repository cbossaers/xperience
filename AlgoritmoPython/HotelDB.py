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

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)

def GetHotelById(id: string):
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
        results = []

        for hotel in cursor.fetchall():
            results.append(dict(zip(columns, hotel)))

        return json.dumps(results, cls=DecimalEncoder)

    except Exception as error:
        raise error

    finally:
        if connection:
            cursor.close()
            connection.close()

print(GetHotelById("1"))