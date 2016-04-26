import serial
import os
import platform
import glob
import sys

## This lets us know if we are running the program on a Mac or Linux Computer.
#print platform.system()
if platform.system() == 'Darwin':
    computerSystem = 'Mac'
elif platform.system() == 'Linux':
    computerSystem = 'Raspi'
else:
    computerSystem = 'Unknown'
print "I hope you are using a", computerSystem


if computerSystem == 'Mac':
    typeFile = "/dev/cu.usbmodem*"
elif computerSystem == 'Raspi':
    typeFile = "/dev/ttyAMC*"

ardunioLocation = glob.glob(typeFile)
if not ardunioLocation:
    print "I do not see an Arduino"
    sys.exit()
else:
    print "Your Arduino is at",
    print ardunioLocation[0]


ser = serial.Serial(ardunioLocation[0], 115200)
while True:
	print ser.readline(),

## Function that writes coordinates to TABLE ttl in DATABASE data.db
## Must Create DATABASE AND TABLE prior to this code running
## Table creation script can be found under SilentCircuit/createTable.py
def wt2Sqlite3(coord):
	import sqlite3
	conn = sqlite3.connect('./data.db')
	curs = conn.cursor()
	ins = 'INSERT INTO ttl (lat, long) VALUES (?,?)'
	curs.execute(ins, coord)
	conn.commit()
	print('record successfully imported')

##simulates coordinate input and calls the above function
coord1 = [10.0000, -20.0000]
wt2Sqlite3(coord1)
coord2 = [30.0000, -40.0000]
wt2Sqlite3(coord2)
coord3 = [50.0000, -60.0000]
wt2Sqlite3(coord3)
coord4 = [70.0000, -80.0000]
wt2Sqlite3(coord4)
coord5 = [90.0000, -10.0000]
wt2Sqlite3(coord5)
