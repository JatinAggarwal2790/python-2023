# delete rows
import sqlite3                          # import the database driver

conn = sqlite3.connect("mydatabase.db") # connect to the database

cursor = conn.cursor()                  # create a cursor

SQL = """DELETE FROM books WHERE bid = 2"""

cursor.execute(SQL)                     # execute the sql

conn.commit()

print(f"Deleted {cursor.rowcount} row(s)")

conn.close()                            # close the connection
