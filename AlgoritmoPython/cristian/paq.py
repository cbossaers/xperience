from flask import jsonify
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import ast
import json
import datetime

import crearPaquetes as c

class Paq(Resource):
    def get(self):
        return {'info': 'GET está actualmente deshabilitado'}, 200  # return data and 200 OK

    def post(self):
        args = request.json
        x = c.GenerarPaquetes(args["origen"], args["fechaIda"], args["fechaVuelta"], args["presupuesto"])
        return x, 200  # return data with 200 OK