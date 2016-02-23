

CREATE TABLE athletes (
    id        	      serial PRIMARY KEY,
    name              varchar(64),

    age      	        int,
    hieght            varchar(5),
    wieght            int,

    clean_and_jerk    varchar(32),
    snatch            varchar(32),
    deadlift          varchar(32),
    back_squat        varchar(32),
    max_pullups       int,
    run_5k            varchar(32),
    created_at        timestamp default current_timestamp
);

CREATE TABLE teams (
  id        	      serial PRIMARY KEY,
  name              varchar(64),
  captain           varchar(64),
  week_one_score    int,
  week_two_score    int,
  week_three_score  int,
  week_four_score   int,
  week_five_score   int
)

CREATE TABLE athlete_teams(
   id           serial PRIMARY KEY,
   athlete_id   int references athletes(id),
   team_id      int references teams(id)
)

INSERT INTO teams (name, captain)
    VALUES
    ('Premature WallBalding', 'Cam'),
    ('50 Shades of Gainz', 'Manny'),
    ('EMObility', 'Chris'),
    ('Panic at the Burpees', 'Adam'),
    ('MerMannies', 'Bobby');