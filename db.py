import sqlite3
from flask import g
import datetime

import os
DATABASE = 'dograntcounty.sqlite'


# Connect to the database.
def connect_db():
    db_path = os.path.join('', DATABASE)
    # if not os.path.isfile(db_path):
        # raise RuntimeError("Can't find database file '{}'".format(db_path))
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


# Open a database connection and hang on to it in the global object.
def open_db_connection():
    g.db = connect_db()


# If the database is open, close it.
def close_db_connection():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


# Convert the 'row' retrieved with 'cursor' to a dictionary
# whose keys are column names and whose values are column values.
def row_to_dictionary(cursor, row):
    dictionary = {}
    for idx, col in enumerate(cursor.description):
        dictionary[col[0]] = row[idx]
    return dictionary


######################################

months = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12
}


def events(year, month):
    from_month = months[month]
    to_year = year
    to_month = from_month + 1
    if to_month > 12:
        to_month = 1
        to_year = year + 1
    from_date = datetime.datetime.strptime(str(year) + '/' + str(from_month), '%Y/%m')
    to_date = datetime.datetime.strptime(str(to_year) + '/' + str(to_month), '%Y/%m')
    return g.db.execute('SELECT * FROM event WHERE start_date BETWEEN ? AND ? ORDER BY start_date, start_time, end_date, end_time, title', (from_date,to_date,)).fetchall()
