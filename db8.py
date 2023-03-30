# select rows
import sqlite3                          # import the database driver

conn = sqlite3.connect("mydatabase.db") # connect to the database

cursor = conn.cursor()                  # create a cursor

SQL = """SELECT * FROM books"""

cursor.execute(SQL)                     # execute the sql


# fetch one row

print(cursor.fetchone())

# fetch many rows
print(cursor.fetchmany(3))

# fetch all rows

print(cursor.fetchall())

# fetch using a for loop

for row in cursor.execute(SQL):
    print(row)
    
# fetch using for and unpack
for bid, title, author in cursor.execute(SQL):
    print(bid, title, author)


conn.close()                            # close the connection
