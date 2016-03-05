
from models import Athlete
from flask_restful import Resource
from flask import abort
from flask.ext.restful import fields, marshal


athlete_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'uri': fields.Url('athletes'),

    'age': fields.Integer,
    'height': fields.String,
    'weight': fields.String,
    'clean_and_jerk': fields.String,
    'snatch': fields.String,
    'deadlift': fields.String,
    'back_squat': fields.String,

    'affiliate_id':  fields.Integer
}


class AthletesAPI(Resource):

    def __init__(self):
        super(AthletesAPI, self).__init__()

    def get(self, id):
        athlete_record = Athlete.query.filter_by(id=id).one_or_none()

        if not athlete_record:
            return abort(404)
        return {'result': marshal(athlete_record, athlete_fields)}


class AthletesByAffiliateAPI(Resource):

    def __init__(self):
        super(AthletesByAffiliateAPI, self).__init__()

    def get(self, id):
        athlete_records = Athlete.query.filter_by(affiliate_id=id).all()

        if not athlete_records:
            return abort(404)

        return {'results': marshal(athlete_records, athlete_fields)}
