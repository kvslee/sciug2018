# Step 1: import libraries (plotly, psycopg2, json)
# Step 2: get Sierra data (connect, run a querry, get data)
# Step 3: transform Sirera data for Plotly (x axis and y axis)
# Step 4: generate Plotly with Sierra data


import plotly
from plotly.graph_objs import Bar, Pie, Scatter, Layout
import psycopg2
import psycopg2.extras
import json
import bisect

# read data configuration (host, dbname, port, user, password)
with open('./conn.json') as conn_file:
    config = json.load(conn_file)

# Connecting to Sierra PostgreSQL database, run a SQL command, and get data
try: 
    # connect sierra database
    conn = psycopg2.connect(config["sierra"]) 
    # create a database session in which SQL commands will run
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    # run a SQl command  
    cursor.execute(open("./sql/circ_trans.sql", 'r').read(), {"interval": '10 days', "trans_types": ('o', 'i', 'f', 'r')})
    # fetch all rows of a query result
    circ_trans = cursor.fetchall()
except psycopg2.Error as error:
    print("Unable to connect to database: " + str(error))
finally:
    conn.close()


# transform Sierra data for Plotly (x axis and y axis)
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
home_library = chart_data(circ_trans, 'patron_home_library_code')
print("Transactions by patron home library: ", home_library)


# creating a Plotly chart
plotly.offline.plot({
    "data": [Bar(x=home_library[0], y=home_library[1])],
    "layout": Layout(title="Transactions by Patron Home Library")
}, filename='output/sierra_bar.html')

# creating a Plotly chart
plotly.offline.plot({
    "data": [Pie(labels=home_library[0], values=home_library[1])],
    "layout": Layout(title="Transactions by Patron Home Library")
}, filename='output/sierra_pie.html')