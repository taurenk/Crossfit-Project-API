from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Athlete(db.Model):

    __tablename__ = 'athletes'

    id =            db.Column(db.Integer, primary_key=True)
    name =          db.Column(db.String(64))

    age =           db.Column(db.Integer)
    hieght =        db.Column(db.String(4))
    wieght =        db.Column(db.Integer)

    clean_and_jerk = db.Column(db.String(32))
    snatch =        db.Column(db.String(32))
    deadlift =      db.Column(db.String(32))
    back_squat =    db.Column(db.String(32))
    max_pullups =   db.Column(db.Integer)
    run_5k =        db.Column(db.String(32))

    def __repr__(self):
        return "<%s>" % self.name
