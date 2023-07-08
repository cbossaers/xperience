import json
import os
import statistics
import ApiConnection

      
# Serializing json
def getListaHotelesEstrellas(cityCode):

	listaHoteles = ApiConnection.getHotelByCity(cityCode)
	listaRating = []
	lista = []
	for element in listaHoteles:
		lista.append(element)
		if len(lista) == 3:
			listaRating.append(ApiConnection.getHotelRating(lista))
			lista = []
	if len(lista) >= 1:
		listaRating.append(ApiConnection.getHotelRating(lista))
		lista = []
	for element in listaRating:
		if element["overallRating"] >= 90:
			lista.append([element["hotelId"],5, element["sentiments"]])
		elif element["overallRating"] >= 75:
			lista.append([element["hotelId"],4, element["sentiments"]])
		elif element["overallRating"] >= 50:
			lista.append([element["hotelId"],3, element["sentiments"]])
		else:
			lista.append([element["hotelId"],2, element["sentiments"]])
		
	return lista

print(getListaHotelesEstrellas("PAR"))
	# listaHotelesMayor50.
	# for element in lista:
