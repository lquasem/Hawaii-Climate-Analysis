from flask import Flask 
from flask import Flask , jsonify

import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect


app = Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo =False,connect_args={'check_same_thread': False})
session = Session(engine)
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station

@app.route('/')
def index():
    return "Welcome to Hawaii climate information"

@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username

#  Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
#  Return the JSON representation of your dictionary.

def prcp():
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    prcp = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > last_year).\
    order_by(Measurement.date).all()
    return jsonify(prcp)



#   Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def station():
    # session = Session(engine)
    station = session.query(Station.id, Station.station).\
    order_by(Station.id).all()
    return jsonify(station)


#   Query for the dates and temperature observations from a year from the last data point.
#   Return a JSON list of Temperature Observations (tobs) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs ():
    # session = Session(engine)
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs = session.query(Measurement.station,Measurement.date, Measurement.tobs).\
    filter(Measurement.date > last_year).\
    order_by(Measurement.date).all()
    return jsonify(tobs)

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range

@app.route("/api/v1.0/weather/<start_range>") 
def weather(start_range):
    temps = [Measurement.station, Measurement.date,
         func.avg(Measurement.tobs),
         func.min(Measurement.tobs),
         func.max(Measurement.tobs)]
    start_date =  dt.datetime.strptime(start_range,"%Y-%m-%d").date()
    start_range = session.query(*temps).\
    filter(Measurement.date >= start_date).\
    order_by(Measurement.tobs).\
    group_by(Measurement.station).all()
    return jsonify ("TAVG, TMIN, TMAX  %s" %start_range)


@app.route("/api/v1.0/temps/<date_start>/<date_end>")
def temps(date_start,date_end):   
    dobs = [Measurement.station, Measurement.date,
         func.avg(Measurement.tobs),
         func.min(Measurement.tobs),
         func.max(Measurement.tobs)]
    end_date = dt.datetime.strptime(date_end,"%Y-%m-%d").date() 
    start_date = dt.datetime.strptime(date_start,"%Y-%m-%d").date()
    date_range = session.query(*dobs).\
    filter(Measurement.date.between (date_start, date_end)).\
    group_by(Measurement.station).\
    order_by(Measurement.station).all()
    return jsonify ("TAVG, TMIN, TMAX  %s" %date_range)



if __name__ == '__main__':
    app.run(debug=True)





