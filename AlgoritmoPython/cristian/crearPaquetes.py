import json
import datetime
import hotelesDesdeAmadeus as h
import vuelosDesdeAmadeus as v

def CrearPaquete(origen: str, destino: str, fechaIda: datetime, fechaVuelta: datetime):
    habitacion = h.ObtenerHabitacionesDeCiudad(destino, fechaIda, fechaVuelta)
    v.ObtenerVuelos(origen, destino, fechaIda, fechaVuelta)