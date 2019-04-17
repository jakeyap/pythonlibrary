# -*- coding: utf-8 -*-
"""
This code does a FFT on a sine wave for an ADC
Date: 2015 Oct 12th
@author: yyk
"""
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
from scipy import signal

sampling_freq = 400     # This is in Hz
sinewave_freq = 20.13   #This is also in Hz

fullscale = 4096
samples = 262144        #This is 2**18
#samples = 204800       #This is 2**18
#samples = 800          #This is 2**18


time_vector = []
freq_vector = []
counter = 0
while counter<samples:
    time_vector.append(counter/sampling_freq)
    counter = counter + 1

y = [] 
for each in time_vector:
#    y.append(0.5*fullscale * (sin(2*pi*sinewave_freq*each)) + 0.5*fullscale)
    y.append(0.5*fullscale * (sin(2*pi*sinewave_freq*each))+0.5*fullscale * (sin(2*pi*5*sinewave_freq*each)))

window = signal.blackmanharris(samples,False)
#window = signal.hanning(samples)
counter = 0
y_windowed = []

while counter<samples:
    y_windowed.append(window[counter]*y[counter])
    counter = counter + 1

#Yf = 2*abs(fft(y)/(samples*fullscale))


Y_windowed = 20*log10(abs(2*fft(y_windowed)/samples))

Y_windowed[0] = Y_windowed[0]/2
Y_windowed = Y_windowed[0:samples/2]


##Yf[0] = 20 * log10 (Yf[0])
#counter = 1
#while counter<samples/2:
#    Yf[counter] = Yf[counter]*2
#    counter = counter + 1
counter = 0
while counter < (samples/2):
    freq_vector.append(counter * sampling_freq / samples)
    counter = counter + 1

plt.figure('fft')
#plt.clf()

plt.subplot(2,2,1)
plt.title('normal')
plt.plot(time_vector[0:100],y[0:100])
plt.grid('on')

plt.subplot(2,2,2)
plt.title('windowed')
plt.plot(time_vector,y_windowed)

plt.subplot(2,2,4)
plt.plot(freq_vector, Y_windowed)
plt.title("Windowed FFT")
plt.grid('on')
#plt.yscale('log')
print(max(Y_windowed))


Yf = 20 * log10(abs(2*fft(y)/samples))
Yf[0] = Yf[0]/2
Yf = Yf[0:samples/2]

plt.subplot(2,2,3)
plt.title("Normal FFT")
plt.plot(freq_vector, Yf)
#plt.yscale('log')
plt.grid('on')
print(max(Yf))