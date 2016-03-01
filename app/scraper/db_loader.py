from app.models import Athlete, db


def load_data(athletes_data):

    for athlete, athlete_data in athletes_data.iteritems():
        athlete_record = Athlete(
                name=athlete,
                age=clean_string(athlete_data['age']),
                hieght=clean_string(athlete_data['hieght']),
                wieght=clean_string(athlete_data['wieght']),

                run_5k=athlete_data['Run 5k'],
                back_squat=clean_string(athlete_data['Back Squat']),
                clean_and_jerk=clean_string(athlete_data['Clean & Jerk']),
                snatch=clean_string(athlete_data['Snatch']),
                deadlift=clean_string(athlete_data['Deadlift']),
                max_pullups=athlete_data['Max Pull-ups'],
        )
        db.session.add(athlete_record)
    db.session.commit()


def clean_string(s):
    if s is None:
        return s

    if s == '--':
        return None

    if 'lb' in s:
        s = s.replace('lb', '')

    return s.strip()


if __name__ == '__main__':
    load_data()
