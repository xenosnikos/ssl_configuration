from flask import Flask
from flask_restful import Api

from controllers.ssl_configuration import SSLConfiguration

app = Flask(__name__)
api = Api(app)

api.add_resource(SSLConfiguration, "/v2/sslConfiguration")

if __name__ == "__main__":
    app.run()
