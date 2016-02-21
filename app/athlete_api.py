
from models import db, Athlete
from flask_restful import Resource
from flask import abort
from flask.ext.restful import fields, marshal, reqparse

athlete_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'uri': fields.Url('athletes')
}



class AthletesAPI(Resource):

    def __init__(self):
        super(AthletesAPI, self).__init__()

    def get(self, id):
        athlete_record = Athlete.query.filter_by(id=id).one_or_none()

        if not athlete_record:
            return abort(404)
        return {'result': marshal(athlete_record, athlete_fields)}
