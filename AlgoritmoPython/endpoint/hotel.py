from flask import jsonify
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import ast
import json
import DALHotel

class Hotel(Resource):
    def get(self):
        data = pd.read_csv('Hotel.csv')  # read local CSV
        return {'data': data.to_dict()}, 200  # return data dict and 200 OK
    
    def post(self):
        args = request.json
        x = DALHotel.GetHotel(args["id"])
        return x, 200  # return data with 200 OK
    
    def patch(self):
        return True

    def put(self):
        args = request.json
        DALHotel.AddHotel(args["id"],args["tipo"],args["chaincode"],args["amadeusid"],args["dupeid"],args["nombre"],args["estrellas"],args["ciudad"],args["latitud"],args["longitud"])
        return 200  # return data with 200 OK

    def delete(self):
        args = request.json
        DALHotel.DeleteHotel(args["id"])
        return 200  # return data with 200 OK