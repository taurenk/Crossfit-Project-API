from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Athlete(db.Model):

    __tablename__ = 'athletes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    gender = db.Column(db.String(1))
    age = db.Column(db.Integer)
    height = db.Column(db.String(10))
    weight = db.Column(db.String(10))
    clean_and_jerk = db.Column(db.String(32))
    snatch = db.Column(db.String(32))
    deadlift = db.Column(db.String(32))
    back_squat = db.Column(db.String(32))
    max_pullups = db.Column(db.Integer)
    run_5k = db.Column(db.String(32))

    affiliate_id = db.Column(db.Integer, db.ForeignKey('affiliates.id'))

    week1_score = db.Column(db.Integer)
    week2_score = db.Column(db.Integer)
    week4_score = db.Column(db.Integer)
    week5_score = db.Column(db.Integer)

    def __repr__(self):
        return "{'name' : '%s'}" % self.name


class Affiliate(db.Model):

    __tablename__ = 'affiliates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    state = db.Column(db.String(64))
    country = db.Column(db.String(64))
    logo_url = db.Column(db.String(128))

    athletes = db.relationship('Athlete', backref='affiliate',
                                lazy='dynamic')

