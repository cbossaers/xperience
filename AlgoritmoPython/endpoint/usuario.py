from flask import jsonify
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import ast
import json

import DALUsuario

class Usuario(Resource):
    def get(self):# hacer
        return {'info': 'GET está actualmente deshabilitado'}, 200  # return data and 200 OK

    def post(self):
        args = request.json
        x = DALUsuario.GetUsuario(args["correo"])
        return x, 200  # return data with 200 OK

    def put(self):
        args = request.json
        DALUsuario.AddUsuario(args["correo"],args["contr"],args["nombre"],args["apellidos"],args["telefono"],args["fechaNacimiento"],args["dni"],args["dirPost"],args["dirFac"])
        return 200  # return data with 200 OK

    def delete(self):
        args = request.json
        DALUsuario.DeleteUsuario(args["correo"])
        return 200  # return data with 200 OK