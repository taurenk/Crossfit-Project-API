from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

athlete_teams = db.Table('athlete_teams',
                         db.Column('athlete_id', db.Integer, db.ForeignKey('athletes.id')),
                         db.Column('team_id', db.Integer, db.ForeignKey('teams.id'))
                         )

affiliate_athletes = db.Table('affiliate_athletes',
                         db.Column('affiliate_id', db.Integer, db.ForeignKey('affiliates.id')),
                         db.Column('athlete_id', db.Integer, db.ForeignKey('athletes.id'))
                         )


class Athlete(db.Model):
    __tablename__ = 'athletes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    height = db.Column(db.String(4))
    weight = db.Column(db.Integer)
    clean_and_jerk = db.Column(db.String(32))
    snatch = db.Column(db.String(32))
    deadlift = db.Column(db.String(32))
    back_squat = db.Column(db.String(32))
    max_pullups = db.Column(db.Integer)
    run_5k = db.Column(db.String(32))

    def __repr__(self):
        return "{'name' : '%s'}" % self.name


class Affiliates(db.Model):
    __tablename__ = 'affiliates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    state = db.Column(db.String(64))


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    captain = db.Column(db.String(64))
    athletes = db.relationship('Athlete', secondary=athlete_teams,
                               backref=db.backref('teams', lazy='dynamic'))

    def __repr__(self):
        return "<%s, %s>" % (self.name, self.athletes)
