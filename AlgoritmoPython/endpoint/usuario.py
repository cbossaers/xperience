from flask import jsonify
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import ast
import json

import DALUsuario

class Usuario(Resource):
    def get(self):
        return {'info': 'GET está actualmente deshabilitado'}, 200  # return data and 200 OK

    def post(self):
        args = request.json
        x = DALUsuario.GetVueloByFechaPrecio(args["fechaSalida"], args["fechaLlegada"], args["precio"])
        return x, 200  # return data with 200 OK

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('location', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('Vuelos.csv')
        
        if args['userId'] in list(data['userId']):
            # evaluate strings of lists to lists !!! never put something like this in prod
            data['Hoteles'] = data['Hoteles'].apply(
                lambda x: ast.literal_eval(x)
            )
            # select our user
            user_data = data[data['userId'] == args['userId']]

            # update user's Hoteles
            user_data['Hoteles'] = user_data['Hoteles'].values[0] \
                .append(args['location'])
            
            # save back to CSV
            data.to_csv('Vuelos.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise the userId does not exist
            return {
                'message': f"'{args['userId']}' user not found."
            }, 404

    def delete(self):
        args = request.json
        DALUsuario.DeleteUsuario(args["correo"])
        return 200  # return data with 200 OK