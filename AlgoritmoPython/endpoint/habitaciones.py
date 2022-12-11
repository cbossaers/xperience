from flask import jsonify
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import ast
import json

import DALHabitacion

class Habitaciones(Resource):
    def get(self):
        return {'info': 'GET está actualmente deshabilitado'}, 200  # return data and 200 OK

    def post(self): # hacer
        args = request.json
        x = DALHabitacion.GetHabitacion(args["id"])
        return x, 200  # return data with 200 OK

    def getFromHotel(self):
        args = request.json
        x = DALHabitacion.GetHabitacionesHotel(args["hotelid"])
        return x, 200  # return data with 200 OK   

    def put(self):
        args = request.json
        DALHabitacion.AddHabitacion(args["id"],args["hotelid"],args["fechaLlegada"],args["descripcion"],args["categoria"],args["numCamas"],args["tipoCama"],args["precioTotal"],args["precioBase"],args["precioTasas"],args["fechaSalida"],args["policiesid"])
        return 200  # return data with 200 OK

    def delete(self):
        args = request.json
        DALHabitacion.DeleteHabitacion(args["id"])
        return 200  # return data with 200 OK