

CREATE TABLE athletes (
    id        	      serial PRIMARY KEY,
    name              varchar(64),
    gender            varchar(1),
    age      	        int,
    height            varchar(5),
    weight            int,
    clean_and_jerk    varchar(32),
    snatch            varchar(32),
    deadlift          varchar(32),
    back_squat        varchar(32),
    max_pullups       int,
    run_5k            varchar(32),
    week1_score       int,
    week2_score       int,
    week3_score       int,
    week4_score       int,
    week5_score       int,
    created_at        timestamp default current_timestamp
);


CREATE TABLE affiliates (
  id        	      serial PRIMARY KEY,
  affiliate_id      varchar(10),
  name              varchar(64),
  state             varchar(64),
  country           varchar(64),
  logo_url          varchar(128),
  created_at        timestamp default current_timestamp
);


CREATE TABLE affiliate_athletes (
   affiliate_id     int references affiliates(id),
   athlete_id       int references athletes(id),
   created_at       timestamp default current_timestamp
);

