CREATE DATABASE weather_report;

use weather_report;

CREATE TABLE weather_data (
station_id INT,
station_name varchar(20),
time date,
tavg DECIMAL(10,2),
tmin DECIMAL(10,2),
tmax DECIMAL(10,2),
prcp DECIMAL(10,2),
snow DECIMAL(10,2),
wdir DECIMAL(10,2),
wspd DECIMAL(10,2),
wpgt DECIMAL(10,2),
pres DECIMAL(10,2),
tsun DECIMAL(10,2),
load_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

CREATE USER 'comatch'@'localhost' IDENTIFIED BY 'comatch';

GRANT ALL PRIVILEGES ON *.* TO 'comatch'@'localhost' WITH GRANT OPTION;