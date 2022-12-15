import psycopg
import datetime
import json
from psycopg.rows import dict_row

conndata = "dbname=bluesky user=pi password=pi host=88.17.114.199 port=5432"

def AddHabitacion(id: int, hotelid: int, fechaLlegada: datetime, descripcion: str, categoria: str, numCamas: int, tipoCama: str, 
    precioTotal: float, precioBase: float, precioTasas: float, fechaSalida: datetime, policiesid: int):

    with psycopg.connect(conndata) as conn: #hecho
        with conn.cursor() as cur:

            SQL = """INSERT INTO habitacion VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (id) 
            DO UPDATE SET 
                hotelid = excluded.hotelid,
                fechallegada = excluded.fechallegada,
                descripcion = excluded.descripcion,
                categoria = excluded.categoria,
                numcamas = excluded.numcamas,
                tipocama = excluded.tipocama,
                preciototal = excluded.preciototal,
                preciobase = excluded.preciobase,
                preciotasas = excluded.preciotasas
                fechasalida = excluded.fechasalida
                policiesid = excluded.policiesid"""

            data = (id, hotelid, fechaLlegada, descripcion, categoria, numCamas, tipoCama, precioTotal, precioBase, precioTasas, fechaSalida, policiesid)

            try:
                cur.execute(SQL,data)
                conn.commit()

            except Exception as error:
                raise error

def DeleteHabitacion(id: int):
    with psycopg.connect(conndata) as conn:
        with conn.cursor() as cur:

            SQL = "DELETE FROM habitacion WHERE id = %s"
            data = (id,)

            try:
                cur.execute(SQL,data)
                conn.commit()

            except Exception as error:
                raise error

def GetHabitacion(id: str):
    with psycopg.connect(conndata, row_factory=dict_row) as conn:
        with conn.cursor() as cur:

            SQL = "SELECT * FROM habitacion WHERE id = %s"

            data = (id,)

            try:
                cur.execute(SQL,data)

                return json.dumps(cur.fetchall(), indent=4, default=str)

            except Exception as error:
                raise error

def GetHabitacionesHotel(hotelid: str):
    with psycopg.connect(conndata, row_factory=dict_row) as conn:
        with conn.cursor() as cur:

            SQL = "SELECT * FROM habitacion WHERE hotelid = %s"

            data = (hotelid,)

            try:
                cur.execute(SQL,data)

                return json.dumps(cur.fetchall(), indent=4, default=str)

            except Exception as error:
                raise error