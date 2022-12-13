from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
import paq


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

api = Api(app)

api.add_resource(paq.Paq, '/paq')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)