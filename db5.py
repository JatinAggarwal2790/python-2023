# bulk insert
import sqlite3                          # import the database driver

conn = sqlite3.connect("mydatabase.db") # connect to the database

cursor = conn.cursor()                  # create a cursor

SQL = """INSERT INTO books
(title,author)
VALUES (?,?)
"""

mybooks = [('Ikigai','Hector'),
           ('5 AM Club','Robin Sharma'),
           ('My experiments with truth','Gandhi')
        ]

cursor.executemany(SQL, mybooks)                     # execute the sql

conn.commit()                           # save the data permanently
print(f"Inserted {cursor.rowcount} row(s)")

conn.close()                            # close the connection
