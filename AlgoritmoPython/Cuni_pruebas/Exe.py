import datetime
from Funcion import *

ida = datetime.datetime(2022, 11, 14)
vuelta = datetime.datetime.today()
presupuesto = 66
origen = 'AGP'

cargarViajes()
#paquetes(origen,ida,vuelta,presupuesto)

pepe = [0,0,1,2,3,4]
pepe1 = [0,0,1,2,3,5,6]        
pepe = list(set(pepe) | set(pepe1))

print(pepe)
