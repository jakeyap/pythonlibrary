# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:44:15 2019
Commonly used functions on step waveforms
@author: yyk
"""

def risetime1090 (time, waveform, startpt = 0):
    '''
    Finds 10-90 rise time of a step. 
    Inputs
    time:       list of time steps
    waveform:   list of values
    start_pt:   where to start counting from, in fraction of time
    
    Returns: [risetime, lo_value, hi_value]
    '''
    return risetime (time, waveform, 0.1, 0.9, startpt)
    

def risetime2080 (time, waveform, startpt = 0):
    '''
    Finds 20-80 rise time of a step. 
    Inputs
    time:       list of time steps
    waveform:   list of values
    start_pt:   where to start counting from, in fraction of time
    
    Returns: [risetime, lo_value, hi_value]
    '''
    return risetime (time, waveform, 0.2, 0.8, startpt)
    
    
def risetime (time, waveform, lo_percent, hi_percent, startpt = 0):
    '''
    Finds 10-90 rise time of a step. 
    Inputs
    time:       list of time steps
    waveform:   list of values
    hi_percent: high crossing point
    lo_percent: low crossing point
    start_pt:   where to start counting from, in fraction of time
    '''
    
    max_y = max(waveform)
    hi_y = hi_percent * max_y
    lo_y = lo_percent * max_y
    
    stopindex = len(time)
    counter = int(startpt * stopindex)
    
    hi_x = 0    # stores the 90% time index
    lo_x = 0    # stores the 10% time index
    
    lo_found = False
    
    while(counter < stopindex):
        if ((waveform[counter] > lo_y) and (not lo_found)):
            lo_x = counter
            lo_found = True
        
        if (waveform[counter] > hi_y):
            hi_x = counter
            break
        
        counter = counter + 1
        
        risetime = time[hi_x] - time[lo_x]
        
        return [risetime, lo_y, hi_y]