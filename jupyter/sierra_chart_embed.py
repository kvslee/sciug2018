# Step 1: import libraries (plotly, psycopg2, json)
# Step 2: connect sierra database, run sql querry, get data
# Step 3: process data for plotly (x axis and y axis)
# Step 4: feed data
# Step 5: decorate layout

import plotly
from plotly.graph_objs import Bar, Pie, Scatter, Layout
import psycopg2
import psycopg2.extras
import json
import bisect
import sys

# read data configuration (host, dbname, port, user, password)
with open('../offline/conn.json') as conn_file:
    config = json.load(conn_file)

# Connecting to Sierra PostgreSQL database, run a SQL command, and get data
try: 
    # connect sierra database
    conn = psycopg2.connect(config["sierra"]) 
    # create a database session in which SQL commands will run
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    # run a SQl command
    days = sys.argv[1] + 'days' if len(sys.argv) > 1 else '10 days' 
    trans_types = tuple(sys.argv[2]) if len(sys.argv) > 2 else ('o', 'i', 'f', 'r')
    cursor.execute(open("../offline/sql/circ_trans.sql", 'r').read(), {"interval": days, "trans_types": trans_types})
    # fetch all rows of a query result
    circ_trans = cursor.fetchall()
except psycopg2.Error as error:
    print("Unable to connect to database: " + str(error))
finally:
    conn.close()


# process data for plotly (x axis and y axis)
def chart_data(work_list, key):
    """ transform sql data to feed into plotly charts 
    """
    fields, values = [], []
    for obj in work_list:
        if obj[key] not in fields:
            bisect.insort_left(fields, obj[key])
            index = fields.index(obj[key])
            values.insert(index, 1)
        else:
            index = fields.index(obj[key])
            values[index] += 1
    return [fields, values]


# circulation by patron home library
home_libraries = chart_data(circ_trans, 'patron_home_library_code')

# circulation by location
trans_types = chart_data(circ_trans, 'op_code') 

# circluation by patron types
ptype = chart_data(circ_trans, 'ptype_code')

# circulation by location
item_location = chart_data(circ_trans, 'item_location_code')

# circulation by location
itype = chart_data(circ_trans, 'itype_code_num')

# circulation by location
time_data = chart_data(circ_trans, 'time')

# print("home libraryies", home_libraries)
# print("trans_types", trans_types)
# print("ptype", ptype)
# print("location", item_location)
# print("itype", itype)
# print("time_data", time_data)

home_libraries_chart = plotly.offline.iplot({
                        "data": [Bar(x=home_libraries[0], y=home_libraries[1])],
                        "layout": Layout(title="Home Libraries")
                    })

trans_types_chart = plotly.offline.iplot({
                        "data": [Pie(labels=trans_types[0], values=trans_types[1])],
                        "layout": Layout(title="Transaction Types")
                    })   

ptypes_chart = plotly.offline.iplot({
                        "data": [Bar(x=ptype[0], y=ptype[1])],
                        "layout": Layout(title="Patron Types", xaxis=dict(type='category'))
                    })                    

item_locations_chart = plotly.offline.iplot({
                        "data": [Bar(x=item_location[0], y=item_location[1])],
                        "layout": Layout(title="Item Locations")
                    }) 

itypes_chart = plotly.offline.iplot({
                        "data": [Bar(x=itype[0], y=itype[1])],
                        "layout": Layout(title="Item Types", xaxis=dict(type='category'))
                    }) 

time_chart = plotly.offline.iplot({
                        "data": [Scatter(x=time_data[0], y=time_data[1])],
                        "layout": Layout(title="Times")
                    })

