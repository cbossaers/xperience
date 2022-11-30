from flask import jsonify
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import ast
import json
import DALVuelo

class Vuelo(Resource):
    def get(self):
        return {'info': 'GET está actualmente deshabilitado'}, 200  # return data and 200 OK

    def post(self):
        args = request.json
        x = DALVuelo.GetVueloByFechaPrecio(args["fechaSalida"], args["fechaLlegada"], args["precio"])
        return x, 200  # return data with 200 OK

    def put(self):
        return True

    def delete(self):
        return True