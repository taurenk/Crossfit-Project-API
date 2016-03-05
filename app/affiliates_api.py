
from models import Affiliate
from flask_restful import Resource
from flask import abort
from flask.ext.restful import fields, marshal

athlete_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'uri': fields.Url('athletes')
}

affiliate_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'country': fields.String,
    'logo_url': fields.String,
    'athletes': fields.List(fields.Nested(athlete_fields)),
    'uri': fields.Url('affiliates'),
}


class AffiliateAPI(Resource):

    def __init__(self):
        super(AffiliateAPI, self).__init__()

    def get(self, id):
        affiliate_record = Affiliate.query.filter_by(id=id).one_or_none()

        if not affiliate_record:
            return abort(404)
        return {'result': marshal(affiliate_record, affiliate_fields)}