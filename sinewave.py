# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:18:03 2015

@author: yyongkeo
"""

import matplotlib.pyplot as plt
import scipy

#counter = 0
#x = []
#y = []
#corrupt = []
#while counter < 1000:
#    x.append(counter/100)
#    counter = counter + 1
#    y.append(scipy.sin(counter/100*scipy.pi))
#    corrupt.append(scipy.sin(counter/100*scipy.pi) + 0.5*(scipy.rand()-0.5))

def coswave(wave_freq=2, samp_freq=100, amp=1, time=1, time_offset=0):
    t = []
    y = []
        
    counter = 0
    end_index = time * samp_freq
    
    while (counter < end_index):
        timestep = counter / samp_freq - time_offset
        t.append(timestep)
        y.append(amp * scipy.cos( scipy.pi * 2 * timestep * wave_freq))
        counter = counter + 1
        
    return [t,y]

def sinwave(wave_freq=2, samp_freq=100, amp=1, time=1, time_offset=0):
    t = []
    y = []
        
    counter = 0
    end_index = time * samp_freq
    
    while (counter < end_index):
        timestep = counter / samp_freq - time_offset
        t.append(timestep)
        y.append(amp * scipy.sin( scipy.pi * 2 * timestep * wave_freq))
        counter = counter + 1
        
    return [t,y]


[x,y] = coswave(3,150,1,1)
plt.plot(x,y,'.-')

[x,y] = sinwave(3,150,1,1)
plt.plot(x,y,'x-')