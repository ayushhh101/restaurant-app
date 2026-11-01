-- EXPERIMENT 5 — Apache Pig Latin script
-- Run: pig -x local, then at grunt> type: exec Exp5_Code.pig;

-- ========== PART 1: AGRICULTURE ==========
agriculture_raw = LOAD 'crop_production.csv'
USING PigStorage(',')
AS (
  state_name:chararray,
  district_name:chararray,
  crop_year:chararray,
  season:chararray,
  crop:chararray,
  area:chararray,
  production:chararray
);

-- Remove a possible header row and cast numeric fields.
agriculture_clean = FILTER agriculture_raw BY state_name IS NOT NULL
  AND state_name != 'state_name';

agriculture = FOREACH agriculture_clean GENERATE
  state_name,
  district_name,
  (int)crop_year AS crop_year,
  season,
  crop,
  (double)area AS area,
  (double)production AS production;

DESCRIBE agriculture;
DUMP agriculture;

-- Group all records state-wise.
state_group = GROUP agriculture BY state_name;
DUMP state_group;

-- Highest-production record for each state.
top_crop = FOREACH state_group {
  ordered = ORDER agriculture BY production DESC;
  top1 = LIMIT ordered 1;
  GENERATE FLATTEN(top1);
};
DUMP top_crop;

-- Store the top crop rows to local filesystem in Pig local mode.
STORE top_crop INTO 'data_top' USING PigStorage(',');

-- ========== PART 2: TITANIC ==========
-- Assumed columns: PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,
-- Parch,Ticket,Fare,Cabin,Embarked
titanic_raw = LOAD 'titanic.csv'
USING PigStorage(',')
AS (
  PassengerId:chararray,
  Survived:chararray,
  Pclass:chararray,
  Name:chararray,
  Sex:chararray,
  Age:chararray,
  SibSp:chararray,
  Parch:chararray,
  Ticket:chararray,
  Fare:chararray,
  Cabin:chararray,
  Embarked:chararray
);

-- Filter header row if present.
titanic = FILTER titanic_raw BY PassengerId IS NOT NULL
  AND PassengerId != 'PassengerId';

-- Query 1: first 10 passenger records.
first10 = LIMIT titanic 10;
DUMP first10;

-- Query 2: count passengers by gender.
gender_group = GROUP titanic BY Sex;
gender_count = FOREACH gender_group GENERATE group AS gender, COUNT(titanic) AS passengers;
DUMP gender_count;

-- Query 3: count survivors and non-survivors.
survival_group = GROUP titanic BY Survived;
survival_count = FOREACH survival_group GENERATE group AS survived, COUNT(titanic) AS passengers;
DUMP survival_count;

-- Query 4: number of passengers in each class.
class_group = GROUP titanic BY Pclass;
class_count = FOREACH class_group GENERATE group AS passenger_class, COUNT(titanic) AS passengers;
DUMP class_count;

-- Query 5: average fare for each passenger class.
fare_rows = FOREACH titanic GENERATE Pclass, (double)Fare AS fare;
fare_valid = FILTER fare_rows BY fare IS NOT NULL;
fare_group = GROUP fare_valid BY Pclass;
average_fare = FOREACH fare_group GENERATE group AS passenger_class, AVG(fare_valid.fare) AS avg_fare;
DUMP average_fare;
