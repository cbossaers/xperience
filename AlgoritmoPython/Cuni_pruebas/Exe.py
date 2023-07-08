import datetime
from Funciones import *

airp = ['MAD', 'BCN', 'AGP', 'ALC', 'SVQ', 'VLC']

ida = datetime.datetime(2022, 11, 14)
vuelta = datetime.datetime.today()
presupuesto = 66
origen = 'AGP'

VuelosFiltados(airp, DestinosList(30), "airportOrigins", "ida")
VuelosFiltados(DestinosList(30), airp, "airportDestinations", "vuelta")
#Paquetes(origen,ida,vuelta,presupuesto)