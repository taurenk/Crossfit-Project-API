
DROP TABLE athletes;
DROP TABLE  affiliates;


CREATE TABLE athletes (
    id        	      serial PRIMARY KEY,
    name              varchar(64),
    gender            varchar(1),
    age      	        int,
    height            varchar(10),
    weight            varchar(10),
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

    affiliate_id      int references affiliates(id),

    created_at        timestamp default current_timestamp
);


CREATE TABLE affiliates (
  id                int PRIMARY KEY,
  name              varchar(64),
  state             varchar(64),
  country           varchar(64),
  logo_url          varchar(128),
  created_at        timestamp default current_timestamp
);


