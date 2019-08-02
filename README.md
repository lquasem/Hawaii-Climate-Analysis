# Hawaii-Climate-Analysis

PART A: 
1)Climate Analysis and Exploration

Python and SQLAlchemy has been used to do basic climate analysis and data exploration of the Hawaii  climate database. All of the following analysis has been completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

 Resources: 
‘hawaii.sqlite’
‘hawaii.measurements’
‘Hawaii.stattions’ 

* vacation range is approximately 3-15 days total.

* Used SQLAlchemy `create_engine` to connect to your sqlite database.

* Used SQLAlchemy `automap_base()` to reflect  tables into classes and save a reference to those classes called `Station` and `Measurement`.

2) Precipitation Analysis

*  Designed query to retrieve the last 12 months of precipitation data in the database

* Query results converted into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method. (Jpeg file is added separately).

* Used Pandas to print the summary statistics for the precipitation data.

3) Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

  * Listed the stations and observation counts in descending order.

  * Results for the station with the highest number of observations?

* Designed a query to retrieve the last 12 months of temperature observation data 

 * Filtered by the station with the highest number of observations.

 * Plotted the results as a histogram with `bins=12` (Jpeg file is added separately).

- - -

## Part B - Climate App

Designed a Flask API based on the queries developed above using Flask to create routes

### Routes – all returns are in json format

* `/` Welcome page

•	/Profile page

* `/api/v1.0/precipitation`

* `/api/v1.0/stations`

* `/api/v1.0/tobs`

* `/api/v1.0/<start>` 

* `/api/v1.0/<start>/<end>`
