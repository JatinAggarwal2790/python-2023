# update rows
import sqlite3                          # import the database driver

conn = sqlite3.connect("mydatabase.db") # connect to the database

cursor = conn.cursor()                  # create a cursor

SQL = """UPDATE books SET author = 'Gandhi MK'
WHERE author = 'Gandhi'"""

cursor.execute(SQL)                     # execute the sql

conn.commit()

print(f"Updated {cursor.rowcount} row(s)")

conn.close()                            # close the connection
