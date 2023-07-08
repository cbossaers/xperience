from flask import jsonify
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import ast
import json

import DALPaquete

class Paquete(Resource):
    def get(self):
        return {'info': 'GET está actualmente deshabilitado'}, 200  # return data and 200 OK

    def post(self): # hacer
        args = request.json
        x = DALPaquete.GetPaquete(args["id"])
        return x, 200  # return data with 200 OK

    def put(self):
        args = request.json
        DALPaquete.AddPaquete(args["id"],args["id_habitacion"],args["id_vuelo_ida"],args["id_vuelo_vuelta"])
        return 200  # return data with 200 OK

    def delete(self):
        args = request.json
        DALPaquete.DeletePaquete(args["id"])
        return 200  # return data with 200 OK