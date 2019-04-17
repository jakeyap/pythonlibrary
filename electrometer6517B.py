# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 18:03:14 2014

Electrometer 6517B controls

@author: yyk
"""
import serial

def send_e_meter(string_to_send):   #formats a string to send to Emeter
    global e_meter
    e_meter.write(string_to_send.encode()+'\r\n'.encode())
    
def read_e_meter():     #take raw readings from Emeter
    global e_meter
    send_e_meter('SENS:DATA:FRESH?')
    #send_e_meter(':READ?')

    string_read = ""
    current_char = ""

    while True:
        current_char = str(e_meter.read().decode())
        #print(current_char)
        if current_char == '\r': break
        string_read = string_read + current_char

    string_read = string_read.replace('E+00', '')
    string_read = string_read.replace('+','')
    
    return string_read

def stop_e_meter():
    global e_meter
    e_meter.close()

def start_e_meter():
    global e_meter
    e_meter.open()

def setup_e_meter():    
    global e_meter
    e_meter = serial.Serial()
    e_meter.baudrate = 115200
    e_meter.port = "COM1"
    e_meter.xonxoff = True
    
    e_meter.open()
    e_meter.flush()
    e_meter.flushInput()
    e_meter.flushOutput()
    
    send_e_meter('SYST:ZCH ON')             # Measure offset
    send_e_meter('FUNC "VOLT"')             # Change to voltmeter function
    send_e_meter('VOLT:RANGE 20')           # Set range to 20V max
    send_e_meter('SYST:ZCOR ON')            # Turn on zero cancelling
    send_e_meter('SENS:VOLT:DC:DIGITS 6.5') # Max out decimals
    send_e_meter('FORM:ELEM READ')          # turns off timestamps
    send_e_meter('SENSE:VOLT:DC:NPLCycles 0.1')
    #send_e_meter('DISPLAY:ENABLE 0')
    send_e_meter('SYST:ZCH OFF')            # Turn off offset
    e_meter.close()
    # Finish setting up electrometer