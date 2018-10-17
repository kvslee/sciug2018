import psycopg2
import psycopg2.extras
import json
import bisect
import sql_commands as sql
from collections import Counter

# read data configuration (host, dbname, port, user, password)
with open('../offline/conn.json') as conn_file:
    config = json.load(conn_file)

def find_expired_patron(*home_lib):
    # Connecting to Sierra PostgreSQL database, run a SQL command, and get data
    try: 
        # connect sierra database
        conn = psycopg2.connect(config["sierra"]) 
        # create a database session in which SQL commands will run
        cursor = conn.cursor()
        # run a SQl command
        if len(home_lib) == 1:
            cursor.execute(sql.expired_patron_home_library, {'home_library': home_lib})
        else:
            cursor.execute(sql.expired_patron)

        # fetch all rows of a query result
        Expired_Patron = cursor.fetchall()
        Expired_Patron.insert(0, ('Record Number', 'Last Name', 'First Name', 'Expiration Date', 'Checkout Count')) 
        return Expired_Patron

    except psycopg2.Error as error:
        print("Unable to connect to database: " + str(error))
    finally:
        conn.close()

# # Expired_Patron_Array = list(zip(*Expired_Patron))


def find_ill_lending(*home_lib):
    # Connecting to Sierra PostgreSQL database, run a SQL command, and get data
    try: 
        # connect sierra database
        conn = psycopg2.connect(config["sierra"]) 
        # create a database session in which SQL commands will run
        cursor = conn.cursor()
        # run a SQl command
        if len(home_lib) == 1:
            cursor.execute(sql.ill_lending_home_library, {'home_library': home_lib})
        else:
            cursor.execute(sql.ill_lending)

        # fetch all rows of a query result
        ILL_Lending = cursor.fetchall()
        ILL_Lending = list(zip(*ILL_Lending))
        ILL_Lending = Counter(ILL_Lending[2])
        ILL_Lending = [list(ILL_Lending), list(ILL_Lending.values())]
        print(ILL_Lending)
        return ILL_Lending

    except psycopg2.Error as error:
        print("Unable to connect to database: " + str(error))
    finally:
        conn.close()

def find_ill_partners(*home_lib):
    # Connecting to Sierra PostgreSQL database, run a SQL command, and get data
    try: 
        # connect sierra database
        conn = psycopg2.connect(config["sierra"]) 
        # create a database session in which SQL commands will run
        cursor = conn.cursor()
        # run a SQl command
        if len(home_lib) == 1:
            cursor.execute(sql.ill_partners_home_library, {'home_library': home_lib})
        else:
            cursor.execute(sql.ill_partners)

        # fetch all rows of a query result
        ILL_PARNTERS = cursor.fetchall()
        ILL_PARNTERS = list(zip(*ILL_PARNTERS))
        ILL_PARNTERS = Counter(ILL_PARNTERS[2])
        ILL_PARNTERS = [list(ILL_PARNTERS.keys()), list(ILL_PARNTERS.values())]
        print(ILL_PARNTERS)
        return ILL_PARNTERS

    except psycopg2.Error as error:
        print("Unable to connect to database: " + str(error))
    finally:
        conn.close()        

