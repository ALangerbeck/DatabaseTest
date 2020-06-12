import sqlite3
from sqlite3 import Error

try:
    sqliteConnection = sqlite3.connect('SQLite_python.db')
    cursor = sqliteConnection.cursor()
    print("Database and cursor sucessfullycreated")

    sqlite_select_Query = "Select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is:",record)
    cursor.close

except sqlite3.Error as error:
    print("Error while connecting to sqlite",error)
finally:
    if(sqliteConnection):
        sqliteConnection.close
        print("The SQLite connetion is closed")


