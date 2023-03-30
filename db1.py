
import sqlite3                          # import the database driver

conn = sqlite3.connect("mydatabase.db") # connect to the database

print(conn)                             # test the connection

conn.close()                            # close the connection
