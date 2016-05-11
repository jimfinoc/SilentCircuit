import serial
import os
import platform
import glob
import sys
from multiprocessing import Process
import time


typeFile = "/dev/ttyAMA0"
ttyLocation = glob.glob(typeFile)

ser = serial.Serial(ttyLocation[0], 115200)


def receiveFromSerial (processName, delay):
    time.sleep(delay)
    print "%s: %s" % ( processName, time.ctime(time.time()) )
    while True:
        command = ser.read()
        print command,

def sendToSerial (processName, delay):
    time.sleep(delay)
    print "%s: %s" % ( processName, time.ctime(time.time()) )
    time.sleep(0.5)
    print (b'ATZ\r')
    ser.write(b'ATZ\r')
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

print "Before starting processes"
try:
    pR = Process(target=receiveFromSerial, args=("Receive", 0))
    pR.start()
    pR.join()
except:
    print "Error: Cannot execute Receive"
try:
    pS = Process(target=sendToSerial, args=("Send", 1))
    pS.start()
    pS.join()
except:
    print "Error: Cannot execute Send"

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

# testSend()
while 1:
    pass
