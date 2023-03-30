# create a table
import sqlite3                          # import the database driver

conn = sqlite3.connect("mydatabase.db") # connect to the database

cursor = conn.cursor()                  # create a cursor

SQL = """CREATE TABLE books(
bid integer primary key,
title text,
author text)"""

cursor.execute(SQL)                     # execute the sql

conn.close()                            # close the connection
