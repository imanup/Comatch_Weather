
# Comatch Data Engineer Test

## Steps to run the job

This is how it works:

  * Launch the Docker packaged Mysql database and Python-App server with:
    ```
    docker-compose up
    ```

  * For daily load  run `docker-compose exec python_app python load_data.py <load_type> <City Name>`.
  *  Load Types:
    - Daily
    - History
  * City Name :
    - Tegel

The job will run in two modes dependending upon the paramete given (Daily, History). Each job gets station id 
from Meteostat API (stations = stations.region(country)) and proceed with execution.

Daily run - The job will get the statio id from api and fetch data for current day. The dataframe is build with 
additional columns and all records are inserted to Mysql DB. 

History Run - The Job fetch data for all available years for the station provided and loads data into mysql db. 

## Database Schema
 * Table Name : Weather Report
 ![Database Schema] (Schema.png)

* `init.sql`: contains the scripts that are necessary to initialize the
  database. Every time you check a solution script, the whole database gets
  dropped and regenerated using these fixtures.

* Sql_queries.txt: Contains solution sql queries