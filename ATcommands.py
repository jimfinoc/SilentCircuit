import serial
import os
import platform
import glob
import sys
import thread
import time



recipient = "5613129933"
message = "Hello, World!"

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




phone = serial.Serial(ardunioLocation[0],  115200)
try:
    time.sleep(0.5)
    phone.write(b'ATZ\r')
    print (b'ATZ\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGF=1\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
    print (b'AT+CMGS="' + recipient.encode() + b'"\r')
    time.sleep(0.5)
    phone.write(message.encode() + b"\r")
    time.sleep(0.5)
    phone.write(bytes([26]))
    time.sleep(0.5)
finally:
    phone.close()
