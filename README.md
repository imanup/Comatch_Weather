
# Comatch Data Engineer Test

## Steps to run the job

This is how it works:

  * Launch the Docker packaged Mysql database and Python-App server with:
    ```
    docker-compose up
    ```

  * For daily load  run `docker-compose exec python_app python load_data.py <load_type> <City Name>`.
  Load Types:
    - Daily
    - History
  City Name :
    - Tegel

The job will run in two modes dependending upon the paramete given (Daily, History). Each job gets station id 
from Meteostat API (stations = stations.region(country)) and proceed with execution.

Daily run - The job will get the statio id from api and fetch data for current day. The dataframe is build with 
additional columns and all records are inserted to Mysql DB. 

History Run - The Job fetch data for all available years for the station provided and loads data into mysql db. 

## Database Schema
 Table Name : Weather Report
+--------------+---------------+------+-----+-------------------+-------+
| Field        | Type          | Null | Key | Default           | Extra |
+--------------+---------------+------+-----+-------------------+-------+
| station_id   | int(11)       | YES  |     | NULL              |       |
| station_name | varchar(20)   | YES  |     | NULL              |       |
| time         | date          | YES  |     | NULL              |       |
| tavg         | decimal(10,2) | YES  |     | NULL              |       |
| tmin         | decimal(10,2) | YES  |     | NULL              |       |
| tmax         | decimal(10,2) | YES  |     | NULL              |       |
| prcp         | decimal(10,2) | YES  |     | NULL              |       |
| snow         | decimal(10,2) | YES  |     | NULL              |       |
| wdir         | decimal(10,2) | YES  |     | NULL              |       |
| wspd         | decimal(10,2) | YES  |     | NULL              |       |
| wpgt         | decimal(10,2) | YES  |     | NULL              |       |
| pres         | decimal(10,2) | YES  |     | NULL              |       |
| tsun         | decimal(10,2) | YES  |     | NULL              |       |
| load_dt      | timestamp     | NO   |     | CURRENT_TIMESTAMP |       |
+--------------+---------------+------+-----+-------------------+-------+


There are other directories inside `src/` that can be interesting to you:

* `init-fixtures`: contains the scripts that are necessary to initialize the
  database. Every time you check a solution script, the whole database gets
  dropped and regenerated using these fixtures.

* `solution`: contains your solution files.

* `output-obtained`: contains the latest execution results of your solutions in
  CSV format.

* `output-expected`: contains the expected results from each query in CSV
  format.

**Note:** To know the exact name you have to use for your solutions, you can
check the filenames in the `output-expected` folder. The files there should
match the files in the `solution` folder.

## Instructions to submit the solution

Please submit a modified compressed file including an SQL file for each of the 
tasks in `src/solution/`