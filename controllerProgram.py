import serial
import os
import platform
import glob
import sys
import thread
import time

## Recognize Machine
computerSystem = ""
typeFile = ""
if platform.system() == 'Darwin':
    computerSystem = 'Mac'
elif platform.system() == 'Linux':
    computerSystem = 'Raspi'
else:
    computerSystem = 'Unknown'
print "I hope you are using a", computerSystem

## Predict location of terminal
if computerSystem == 'Mac':
    typeFile = "unusable"
    print "Sorry, you need to use a Raspi."
    sys.exit()
elif computerSystem == 'Raspi':
    typeFile = "/dev/ttyAMA0"

ttyLocation = glob.glob(typeFile)
if not ttyLocation:
    print "I do not see the serial connection"
    sys.exit()
else:
    print "Your serial connection is at",
    print ttyLocation[0]

ser = serial.Serial(ttyLocation[0], 115200)


def receiveFromSerial (threadName, delay):
    time.sleep(delay)
    print "%s: %s" % ( threadName, time.ctime(time.time()) )
    while True:
        print ser.readline(),

def sendToSerial (threadName, delay):
    time.sleep(delay)
    print "%s: %s" % ( threadName, time.ctime(time.time()) )
    while True:
        inputData = raw_input('Enter command: ')
        ser.write(inputData.encode('utf-8'))

def wt2Sqlite3(phoneNumber, latitudeDegrees , longitudeDegrees):
    import sqlite3
    conn = sqlite3.connect('./data.db')
    curs = conn.cursor()
    insertStatement = 'INSERT INTO ttl_entries (phoneNumber, latitudeDegrees, longitudeDegrees) VALUES (?,?,?)'
    insertData = [phoneNumber,latitudeDegrees,longitudeDegrees]
    curs.execute(insertStatement, insertData)
    conn.commit()
    print('record successfully imported')

print "Before starting threads"
try:
    thread.start_new_thread( receiveFromArduino, ("Thread-1", 2, ) )
    # thread.start_new_thread( sendToArduino, ("Thread-2", 4, ) )
    thread.start_new_thread( testSend, ("Thread-3",5 ))

except:
    print "Error: unable to start threads or something broke!"

while 1:
    pass


def testSend(phoneNumber = None, message = None):
    if phoneNumber is None:
        phoneNumber = raw_input('Enter phone number to text (+1234567890): ')
    if message is None:
        message = raw_input('Enter message to send: ')
    try:
        time.sleep(0.5)
        ser.write(b'ATZ\r')
        time.sleep(0.5)
        ser.write(b'AT+CMGF=1\r')
        time.sleep(0.5)
        ser.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
        time.sleep(0.5)
        ser.write(message.encode() + b"\r")
        time.sleep(0.5)
        ser.write(bytes([26]))
        time.sleep(0.5)
