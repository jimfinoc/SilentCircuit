import serial
import os
import platform
import glob
import sys
import thread
import time


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
    typeFile = "/dev/ttyACM*"

ardunioLocation = glob.glob(typeFile)
if not ardunioLocation:
    print "I do not see an Arduino"
    sys.exit()
else:
    print "Your Arduino is at",
    print ardunioLocation[0]

def receiveFromArduino (threadName, delay):
    time.sleep(delay)
    print "%s: %s" % ( threadName, time.ctime(time.time()) )
    while True:
        print ser.readline(),

def sendToArduino (threadName, delay):
    time.sleep(delay)
    print "%s: %s" % ( threadName, time.ctime(time.time()) )
    while True:
        inputData = raw_input('Enter command: ')
        ser.write(inputData.encode('utf-8'))



ser = serial.Serial(ardunioLocation[0], 115200)
try:
    thread.start_new_thread( receiveFromArduino, ("Thread-1", 2, ) )
    thread.start_new_thread( sendToArduino, ("Thread-2", 4, ) )
except:
    print "Error: unable to start thread"

while 1:
    pass
