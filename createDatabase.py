#!/usr/bin/python

import sqlite3
conn = sqlite3.connect('./data.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE ttl_entries (id INTEGER PRIMARY KEY AUTOINCREMENT, phoneNumber long, latitudeDegrees FLOAT, longitudeDegrees FLOAT, time DATETIME DEFAULT CURRENT_TIMESTAMP)''')
curs.execute('''CREATE TABLE ttl_list (id INTEGER PRIMARY KEY AUTOINCREMENT, phoneNumber long, IMEINumber long, time DATETIME DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()
print('database created')
