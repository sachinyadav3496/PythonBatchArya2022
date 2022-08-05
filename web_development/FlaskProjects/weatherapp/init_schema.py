import sqlite3 as sql

db = sql.connect("weather.db")
cursor = db.cursor()

query = "CREATE TABLE user(username TEXT PRIMARY KEY,\
 email TEXT NOT NULL, first_name TEXT NOT NULL, \
last_name TEXT NOT NULL, password TEXT NOT NULL)"

cursor.execute(query)

query = "CREATE TABLE city(username TEXT NOT NULL, city TEXT NOT NULL)"

cursor.execute(query)

db.commit()

cursor.close()
db.close()