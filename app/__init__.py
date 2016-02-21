
from flask import Flask
from flask_restful import Api
from models import db


def create_app(config_file):

    application = Flask(__name__)
    application.config.from_pyfile(config_file)
    db.init_app(application)
    api = Api(application)

    from athlete_api import AthletesAPI
    api.add_resource(AthletesAPI, '/api/athletes/<int:id>', endpoint='athletes')


    @application.route('/')
    def welcome():
        return 'Welcome to Taurenk\'s CrossfitProject API'

    return application