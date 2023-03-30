# Insert a row
import sqlite3                          # import the database driver

conn = sqlite3.connect("mydatabase.db") # connect to the database

cursor = conn.cursor()                  # create a cursor

SQL = """INSERT INTO books
(title,author)
VALUES ('Wings of Fire','Abdul Kalam')
"""

cursor.execute(SQL)                     # execute the sql

conn.commit()                           # save the data permanently
print(f"Inserted {cursor.rowcount} row(s)")

conn.close()                            # close the connection
