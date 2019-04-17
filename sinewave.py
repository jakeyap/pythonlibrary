# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:18:03 2015

@author: yyongkeo
"""

import matplotlib.pyplot as plt

counter = 0
x = []
y = []
corrupt = []
while counter < 1000:
    x.append(counter/100)
    counter = counter + 1
    y.append(sin(counter/100*pi))
    corrupt.append(sin(counter/100*pi) + 0.5*(rand()-0.5))
    
plt.subplot(1,2,1)
plt.plot(x,y)
plt.ylim([-2,2])
plt.subplot(1,2,2)
plt.plot(x,corrupt)
plt.ylim([-2,2])