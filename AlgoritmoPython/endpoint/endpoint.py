from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
import hotel, vuelo, usuario, habitaciones, paquete


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

api = Api(app)

api.add_resource(vuelo.Vuelo, '/vuelo')
api.add_resource(hotel.Hotel, '/hotel')
api.add_resource(usuario.Usuario, '/usuario')
api.add_resource(habitaciones.Habitaciones, '/habitaciones')
api.add_resource(paquete.Paquete, '/paquete')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9879)