from app.models import Athlete, Affiliate, db


def load_affiliate_data(affiliate_data):

    affiliate_record = Affiliate(id=string_to_integer(affiliate_data['affiliate_id']),
                                 name=affiliate_data['name'],
                                 logo_url=affiliate_data['logo_url'],
                                 state=affiliate_data['state'],
                                 country =affiliate_data['country']
                                 )

    db.session.add(affiliate_record)
    db.session.commit()
    return affiliate_record.id


def load_athlete_data(athletes_data, sql_affiliate_id):

    athletes = []

    for athlete, athlete_data in athletes_data.iteritems():

        gender =  athlete_data.get("gender")
        if gender == 'Male':
            gender = "M"
        elif gender == "Female":
            gender = "F"

        print athlete, athlete_data
        athlete_record = Athlete(
                name=athlete,
                gender=gender,

                age=string_to_integer(athlete_data.get('age')),

                height=clean_string(athlete_data.get('height')),

                weight=clean_string(athlete_data.get('weight')),

                run_5k=athlete_data.get('Run 5k'),
                back_squat=clean_string(athlete_data.get('Back Squat')),
                clean_and_jerk=clean_string(athlete_data.get('Clean & Jerk')),
                snatch=clean_string(athlete_data.get('Snatch')),
                deadlift=clean_string(athlete_data.get('Deadlift')),
                max_pullups=athlete_data.get('Max Pull-ups'),
                affiliate_id=sql_affiliate_id,

                week1_score=string_to_integer(athlete_data.get("week_1_score")),
                week2_score=string_to_integer(athlete_data.get("week_2_score")),
                week4_score=string_to_integer(athlete_data.get("week_3_score")),
                week5_score=string_to_integer(athlete_data.get("week_4_score"))
        )

        db.session.add(athlete_record)
        athletes.append(athlete_record)

    db.session.commit()
    return athletes


def string_to_integer(string):
    if string is None:
        return

    try:
        return int(string)
    except ValueError:
        return None


def clean_string(string):

    if string == '--' or string is None:
        return None

    return string.strip()


if __name__ == '__main__':
    load_athlete_data()
