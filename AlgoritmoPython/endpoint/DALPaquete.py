import psycopg
import datetime
import json
from psycopg.rows import dict_row

#temporalmente está aquí para no tener que escribirlo cada vez
conndata = "dbname=bluesky user=pi password=pi host=88.17.114.199 port=5432"

def AddPaquete(id: int, id_habitacion: int, id_vuelo_ida: int, id_vuelo_vuelta: int):

    with psycopg.connect(conndata) as conn:
        with conn.cursor() as cur:

            SQL = """INSERT INTO paquete VALUES (%s,%s,%s,%s) 
            ON CONFLICT (id) 
            DO UPDATE SET 
                id_habitacion = excluded.id_habitacion,
                id_vuelo_ida = excluded.id_vuelo_ida,
                id_vuelo_vuelta = excluded.id_vuelo_vuelta"""

            data = (id, id_habitacion, id_vuelo_ida, id_vuelo_vuelta)

            try:
                cur.execute(SQL,data)
                conn.commit()

            except Exception as error:
                raise error

def DeletePaquete(id: int):
    with psycopg.connect(conndata) as conn:
        with conn.cursor() as cur:

            SQL = "DELETE FROM paquete WHERE id = %s"
            data = (id,)

            try:
                cur.execute(SQL,data)
                conn.commit()

            except Exception as error:
                raise error

def GetPaquete(id: str):
    with psycopg.connect(conndata, row_factory=dict_row) as conn:
        with conn.cursor() as cur:

            SQL = "SELECT * FROM paquete WHERE id = %s"

            data = (id,)

            try:
                cur.execute(SQL,data)

                return json.dumps(cur.fetchall(), indent=4, default=str)

            except Exception as error:
                raise error