from flask import jsonify
from flask_restful import Resource, Api, reqparse, request

import fake as f


class Paq(Resource):
    def post(self):
        args = request.json
        x = f.Fake(args["origen"], args["fechaIda"], args["fechaVuelta"], int(args["presupuesto"]))
        return x, 200  # return data with 200 OK