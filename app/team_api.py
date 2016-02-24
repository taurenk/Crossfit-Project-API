from models import Team
from flask_restful import Resource
from flask import abort
from flask.ext.restful import fields, marshal


athlete_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'uri': fields.Url('athletes')
}

team_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'captain': fields.String,
    'athletes': fields.List(fields.Nested(athlete_fields)),
    'uri': fields.Url('teams_list')
}



class TeamsListAPI(Resource):

    def __init__(self):
        super(TeamsListAPI, self).__init__()

    def get(self):
        team_records = Team.query.all()
        if not team_records:
            return abort(404)

        return {'results': marshal(team_records, team_fields)}
