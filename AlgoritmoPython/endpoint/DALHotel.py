import psycopg
import datetime
import json
from psycopg.rows import dict_row

conndata = "dbname=bluesky user=pi password=pi host=88.17.114.199 port=5432"

def AddHotel(id: int, tipo: str, chaincode: str, amadeusid: int, dupeid: str, nombre: str, estrellas: int, ciudad: str, latitud: float, longitud: float):

    with psycopg.connect(conndata) as conn:
        with conn.cursor() as cur:

            SQL = """INSERT INTO hotel VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
            ON CONFLICT (id) 
            DO UPDATE SET 
                tipo = excluded.tipo,
                chaincode = excluded.chaincode,
                amadeusid = excluded.amadeusid,
                dupeid = excluded.dupeid,
                nombre = excluded.nombre,
                estrellas = excluded.estrellas,
                ciudad = excluded.ciudad,
                latitud = excluded.latitud,
                longitud = excluded.longitud"""

            data = (id, tipo, chaincode, amadeusid, dupeid, nombre, estrellas, ciudad, latitud, longitud)

            try:
                cur.execute(SQL,data)
                conn.commit()

            except Exception as error:
                raise error

def DeleteHotel(id: int):
    with psycopg.connect(conndata) as conn:
        with conn.cursor() as cur:

            SQL = "DELETE FROM hotel WHERE id = %s"
            data = (id,)

            try:
                cur.execute(SQL,data)
                conn.commit()

            except Exception as error:
                raise error

def GetHotel(id: str):
    with psycopg.connect(conndata, row_factory=dict_row) as conn:
        with conn.cursor() as cur:

            SQL = "SELECT * FROM hotel WHERE id = %s"

            data = (id,)

            try:
                cur.execute(SQL,data)

                return json.dumps(cur.fetchall(), indent=4, default=str)

            except Exception as error:
                raise error