#!/usr/bin/python

import sqlite3
conn = sqlite3.connect('./data.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE ttl (id INTEGER PRIMARY KEY AUTOINCREMENT, long IMEI, lat FLOAT, long FLOAT, time DATETIME DEFAULT CURRENT_TIMESTAMP)''')
