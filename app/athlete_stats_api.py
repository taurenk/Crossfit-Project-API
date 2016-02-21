
from models import Athlete
from flask_restful import Resource
from flask import abort
from flask.ext.restful import fields, marshal
import json

athlete_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'uri': fields.Url('athletes')
}

class StrongestAthletesAPI(Resource):

    def __init__(self):
        super(StrongestAthletesAPI, self).__init__()

    def get(self):
        athlete_records = Athlete.query.all()

        for athlete in athlete_records:
            total_pounds = 0

            if athlete.clean_and_jerk:
                total_pounds += int(athlete.clean_and_jerk)
            if athlete.snatch:
                total_pounds += int(athlete.snatch)
            if athlete.deadlift:
                total_pounds += int(athlete.deadlift)
            if athlete.back_squat:
                total_pounds += int(athlete.back_squat)
            athlete.total_pounds = total_pounds

            athlete.ratio = 0
            if athlete.wieght:
                athlete.ratio = athlete.total_pounds / athlete.wieght
        athlete_records.sort(key=lambda x: x.total_pounds, reverse=True)


        results = [{'total_pounds': athlete.total_pounds,
                    'id': athlete.id,
                    'name': athlete.name,
                    'ratio' : athlete.ratio}
                   for athlete in athlete_records]


        return {'results': results}