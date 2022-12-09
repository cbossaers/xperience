from datetime import date
import psycopg
import json
from psycopg.rows import dict_row

#temporalmente está aquí para no tener que escribirlo cada vez
conndata = "dbname=bluesky user=pi password=pi host=88.17.114.199 port=5432"

def AddUsuario(correo: str, contr: str, nombre: str, apellidos: str, telefono: int = None, 
    fechaNacimiento: date = None, dni: str = None, dirPost: str = None, dirFac: str = None):

    with psycopg.connect(conndata) as conn:
        with conn.cursor() as cur:

            SQL = """INSERT INTO usuario VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) 
            ON CONFLICT (correo) 
            DO UPDATE SET 
                contrasenya = excluded.contrasenya,
                nombre = excluded.nombre,
                apellidos = excluded.apellidos,
                telefono = excluded.telefono,
                fechaNacimiento = excluded.fechaNacimiento,
                dni = excluded.dni,
                direccionPostal = excluded.direccionPostal,
                direccionFacturacion = excluded.direccionFacturacion"""

            data = (correo, contr, nombre, apellidos, telefono, fechaNacimiento, dni, dirPost, dirFac)

            try:
                cur.execute(SQL,data)
                conn.commit()

            except Exception as error:
                raise error

def DeleteUsuario(correo: str):
    with psycopg.connect(conndata) as conn:
        with conn.cursor() as cur:

            SQL = "DELETE FROM usuario WHERE correo = %s"
            data = (correo,)

            try:
                cur.execute(SQL,data)
                conn.commit()

            except Exception as error:
                raise error
        
def GetUsuario(correo: str):
    with psycopg.connect(conndata, row_factory=dict_row) as conn:
        with conn.cursor() as cur:

            SQL = "SELECT * FROM usuario WHERE correo = %s"

            data = (correo,)

            try:
                cur.execute(SQL,data)

                return json.dumps(cur.fetchall(), indent=4, default=str)

            except Exception as error:
                raise error


#AddUsuario('CORREO5', 'lalalala','Manolo','Ayuso Cervera')
#DeleteUsuario("CORREO5")
#print(GetUsuario('CORREO3'))