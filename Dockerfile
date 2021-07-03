FROM python:3-onbuild

WORKDIR /usr/src/app

RUN pip3 install mysqlclient \
    mysql-connector-python \
    SQLAlchemy \
    pymysql \
    pandas \
    meteostat

COPY config.json /usr/src/app/
COPY  .  .

EXPOSE 4000
