#!/usr/bin/python

import sqlite3
conn = sqlite3.connect('./data.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE ttl (id INTEGER PRIMARY KEY AUTOINCREMENT, imei LONG, latitude FLOAT, longitude FLOAT, time DATETIME DEFAULT CURRENT_TIMESTAMP)''')
