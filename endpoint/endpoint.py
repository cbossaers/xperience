from flask import Flask
from flask_restful import Api
import hotel, vuelo

app = Flask(__name__)

api = Api(app)

api.add_resource(vuelo.Vuelo, '/vuelo')
api.add_resource(hotel.Hotel, '/hotel')

if __name__ == '__main__':
    app.run(host='0.0.0.0')