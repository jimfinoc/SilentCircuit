import serial
import os
import platform
import glob
import sys
import thread
import time


typeFile = "/dev/ttyAMA0"
ttyLocation = glob.glob(typeFile)

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
        ser.write(b'AT+CMGS="' + phoneNumber.encode() + b'"\r')
        time.sleep(0.5)
        ser.write(message.encode() + b"\r")
        time.sleep(0.5)
        ser.write(b"\x1A\r\n")
        time.sleep(0.5)
    except :
        exit()

testSend()
while 1:
    pass
