
from flask import Flask
from flask_restful import Api
from models import db


def create_app(config_file):

    application = Flask(__name__)
    application.config.from_pyfile(config_file)
    db.init_app(application)
    api = Api(application)

    from athlete_api import AthletesAPI
    from athlete_stats_api import StrongestAthletesAPI

    api.add_resource(AthletesAPI, '/api/athletes/<int:id>', endpoint='athletes')
    api.add_resource(StrongestAthletesAPI, '/api/athletes/stats/strongest',
                                                endpoint='strongest_athletes')


    @application.route('/')
    def welcome():
        return 'Welcome to Taurenk\'s CrossfitProject API'

    return application