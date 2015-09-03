__author__ = 'Nupur'
from flask import Flask
from flask_restful import Api, Resource
from com.service import UserAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')

if __name__ == '__main__':
    app.run(debug=True)