from app.models import Athlete, db


def load_affiliate_data(affiliate_data):
    pass



def load_athlete_data(athletes_data):

    for athlete, athlete_data in athletes_data.iteritems():

        gender =  athlete_data.get("gender")
        if gender == 'Male':
            gender = "M"
        elif gender == "Female":
            gender = "F"

        athlete_record = Athlete(
                name=athlete,
                gender = gender,
                age=clean_string(athlete_data['age']),
                height=clean_string(athlete_data['height']),
                weight=clean_string(athlete_data['weight']),

                run_5k=athlete_data['Run 5k'],
                back_squat=clean_string(athlete_data['Back Squat']),
                clean_and_jerk=clean_string(athlete_data['Clean & Jerk']),
                snatch=clean_string(athlete_data['Snatch']),
                deadlift=clean_string(athlete_data['Deadlift']),
                max_pullups=athlete_data['Max Pull-ups'],

                week1_score = athlete_data.get("week_1_score"),
                week2_score = athlete_data.get("week_2_score"),
                week4_score = athlete_data.get("week_3_score"),
                week5_score = athlete_data.get("week_4_score"))


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
    load_athlete_data()
