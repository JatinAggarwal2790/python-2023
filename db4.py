# select rows
import sqlite3                          # import the database driver

conn = sqlite3.connect("mydatabase.db") # connect to the database

cursor = conn.cursor()                  # create a cursor

SQL = """SELECT * FROM books"""

cursor.execute(SQL)                     # execute the sql

print(cursor.fetchall())

conn.close()                            # close the connection
