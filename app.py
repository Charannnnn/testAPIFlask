from flask import Flask
from flask_restful import Api, Resource

import db

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        res = db.query("SELECT * FROM Vehicle_GatePass_CBIT.credentials")
        return res


api.add_resource(Users, "/users")

if __name__ == "__main__":
    app.run()
