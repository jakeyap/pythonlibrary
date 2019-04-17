# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 16:00:25 2014
Arduino ADC reader. Channel 0
@author: project
"""

import serial

myport = serial.Serial()
myport.baudrate = 38400

myport.port = "COM4"
myport.open()
myport.flush()
myport.flushInput()
myport.flushOutput()

myfile = open("test_readings.csv", 'w')
data1 = []
counter = 0
oldtemp = ""
try:
    while True:
        holder = myport.read()
        if b'X'== holder:
            counter = counter+1
        if 10==counter:
            print("Starting...")
            break
except KeyboardInterrupt:
    pass

try:
    while True:
        temp = str(int.from_bytes(myport.read(),"big"))
        print (temp)
        oldtemp = temp
        myfile.write(temp+'\n')
except KeyboardInterrupt:
    pass
except Exception:
    pass
print("Exiting...")
myport.flush()
myport.flushInput()
myport.flushOutput()
myport.close()
myfile.close()