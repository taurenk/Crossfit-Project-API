
from flask import Flask
from flask_restful import Api
from models import db


def create_app(config_file):

    application = Flask(__name__)
    application.config.from_pyfile(config_file)
    db.init_app(application)
    api = Api(application)

    from athlete_api import AthletesAPI, AthletesListAPI
    from athlete_stats_api import StrongestAthletesAPI
    from app.scraper.scraper_api import scraper_api

    application.register_blueprint(scraper_api, url_prefix='/api/scraper')


    api.add_resource(AthletesListAPI, '/api/athletes', endpoint='athletes_list')
    api.add_resource(AthletesAPI, '/api/athletes/<int:id>', endpoint='athletes')
    api.add_resource(StrongestAthletesAPI, '/api/athletes/stats/strongest', endpoint='strongest_athletes')


    @application.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    return application