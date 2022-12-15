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
        args = request.json
        DALVuelo.AddVuelo(args["codigo"],args["origen"],args["destino"],args["fechaSalida"],args["fechaLlegada"],args["companyia"],args["precio"],args["preciototal"],args["preciobase"],args["preciotasas"])
        return 200  # return data with 200 OK

    def patch(self):
        args = request.json
        DALVuelo.UpdateVuelo(args["codigo"],args["fechaSalida"],args["fechaLlegada"])
        return 200  # return data with 200 OK   

    def delete(self):
        args = request.json
        DALVuelo.DeleteVuelo(args["codigo"],args["fechaSalida"])
        return 200  # return data with 200 OK