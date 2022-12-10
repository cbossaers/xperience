import psycopg
import datetime
import json
from psycopg.rows import dict_row

#temporalmente está aquí para no tener que escribirlo cada vez
conndata = "dbname=bluesky user=pi password=pi host=88.17.114.199 port=5432"

def AddVuelo(codigo: str, origen: str, destino: str, fechaSalida: datetime, fechaLlegada: datetime, companyia: str, 
    precio: float, preciototal: float, preciobase: float, preciotasas: float):

        with psycopg.connect(conndata) as conn:
            with conn.cursor() as cur:

                SQL = "INSERT INTO vuelo2 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (codigo,fecha_salida,precio) DO NOTHING"

                data = (codigo, origen, destino, fechaSalida, fechaLlegada, companyia, precio, preciototal, preciobase, preciotasas)

                try:
                    cur.execute(SQL,data)
                    conn.commit()

                except Exception as error:
                    raise error

def UpdateVuelo(codigo: str, fechaSalida: datetime, fechaLlegada: datetime):
    with psycopg.connect(conndata) as conn:
            with conn.cursor() as cur:

                SQL = "UPDATE vuelo2 SET fechasalida = %s, fechaLlegada = %s WHERE codigo = %s, fechasalida = %s"

                data = (fechaSalida, fechaLlegada, codigo, fechaSalida)

                try:
                    cur.execute(SQL,data)
                    conn.commit()

                except Exception as error:
                    raise error

def DeleteVuelo(codigo: str, fechaSalida: datetime):
    with psycopg.connect(conndata) as conn:
        with conn.cursor() as cur:

            SQL = "DELETE FROM vuelo2 WHERE codigo = %s AND fechasalida = %s"
            data = (codigo, fechaSalida,)

            try:
                cur.execute(SQL,data)
                conn.commit()

            except Exception as error:
                raise error
        
def GetVueloByOriDest(origen: str, destino: str):
    with psycopg.connect(conndata, row_factory=dict_row) as conn:
            with conn.cursor() as cur:

                SQL = "SELECT * FROM vuelo2 WHERE origen = %s AND destino = %s"

                data = (origen, destino)

                try:
                    cur.execute(SQL,data)

                    return json.dumps(cur.fetchall(), indent=4, default=str)

                except Exception as error:
                    raise error

def GetVueloByOriFecha(origen: str, fechaSalida: datetime, fechaLlegada: datetime):
    with psycopg.connect(conndata, row_factory=dict_row) as conn:
            with conn.cursor() as cur:

                SQL = "SELECT * FROM vuelo2 WHERE origen = %s AND (fechasalida BETWEEN %s AND %s)"

                data = (origen, fechaSalida, fechaLlegada)

                try:
                    cur.execute(SQL,data)

                    return json.dumps(cur.fetchall(), indent=4, default=str)

                except Exception as error:
                    raise error

def GetVueloByFechaPrecio(fechaSalida: datetime, fechaLlegada: datetime, importe: float):
    with psycopg.connect(conndata, row_factory=dict_row) as conn:
            with conn.cursor() as cur:

                SQL = "SELECT * FROM vuelo2 WHERE (fechasalida BETWEEN %s AND %s) AND preciototal <= %s"

                data = (fechaSalida, fechaLlegada, importe)

                try:
                    cur.execute(SQL,data)

                    return json.dumps(cur.fetchall(), indent=4, default=str)

                except Exception as error:
                    raise error

# print(GetVueloByOriDest("prueba1", "prueba2"))
#print(GetVueloByOriFecha("prueba1", "2022-03-01", "2022-03-01"))
#x = GetVueloByFechaPrecio(datetime.datetime(2022,11,29),datetime.datetime(2022,11,30),300)
#print(x)
#filename = "./AlgoritmoPython/endpoint/data.json"
#with open(filename, "w") as outfile:
#    json.dump(x, outfile, indent=4)
#AddVuelo('FR24567',datetime.datetime(2022,11,29,11,7), datetime.datetime(2022,11,29,18,0),184.4,'Ryanair','Valencia','Oslo',156.85,100,20)
