
from flask import Flask

from flask_restful import Api



def create_app(config_file):

    application = Flask(__name__)
    #application.config.from_pyfile(config_file)
    #db.init_app(application)


    @application.route('/')
    def testing():
        return 'testing!'

    return application