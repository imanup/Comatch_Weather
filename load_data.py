from sqlalchemy import create_engine
import logging
import sys
from datetime import datetime,date
import pandas as pd 
from meteostat import Stations, Daily
import json
import os

LOG_FILENAME = 'project.log'
APP_NAME = "Weather App"

#Read Config file for values
config_file='config.json'
root_dir=os.path.dirname(os.path.abspath(__file__))

dl_config=os.path.join(root_dir,config_file)

with open(dl_config) as json_file:
    conf = json.load(json_file)

MYSQL_DATABASE= conf["mysql_database"]
MYSQL_USER= conf['mysql_user']
MYSQL_PASSWORD= conf['mysql_pass']
HOST = conf["host"]

print(MYSQL_DATABASE,MYSQL_USER,MYSQL_PASSWORD)

def get_station_id(station,country='DE'):

    stations = Stations()
    stations = stations.region(country)
    stations = stations.fetch(sample=False)
    stations = stations[stations['name'].str.contains(station)]
    return list(stations.index.values)[0]


def load(station_id,load_type):
    if load_type =='Daily':
        dt=date.today()
        today=datetime(dt.year,dt.month,dt.day)
        data = Daily(station_id, today, today)
        data = data.fetch()
    elif load_type =="History":
        data = Daily(station_id)
        data = data.fetch()
    return data

def create_mysql_connection():
    mysql_conn_str = "mysql+pymysql://"+ MYSQL_USER + ":"+ MYSQL_PASSWORD +"@"+HOST+":3306/"+MYSQL_DATABASE
    print(mysql_conn_str)
    engine = create_engine(mysql_conn_str)
    return engine

def insert_data(engine,df):
    final_df=df[['station_id','station_name',\
                'time','tavg','tmin','tmax','prcp','snow',\
                  'wdir','wspd','wpgt','pres','tsun']].copy()
    final_df.to_sql(name='weather_data', con=engine, if_exists = 'append', index=False)

if __name__ == '__main__': 
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    logging.info(sys.argv)

    print(sys.argv,len(sys.argv))
    if len(sys.argv) is not 3:
        logging.warning("Load Type and Station Name is required")
        sys.exit(1)
    logging.info("Application Initialized: " + APP_NAME)

    load_type = sys.argv[1]
    station = sys.argv[2]

    station_id = get_station_id(station)
    
    df=pd.DataFrame()

    df = load(station_id,load_type)
    df['station_id']=station_id
    df['station_name']=station
    df=df.reset_index()
    engine=create_mysql_connection()
    insert_data(engine,df)
    logging.info("Application Done: " + APP_NAME)