# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:34:50 2019
A library for evaluating an ADC ramp file
@author: yap yong keong
"""

#def plot_inls_dnls(directory, filename):
import matplotlib.pyplot as plt
import numpy as np
import csv

def extract_ramp(directory, filename, ignore_row=0, ignore_col=0):
   '''
   This function extracts the transfer function of an ADC from a csv file.   
   Function returns a dictionary 
   {inputs: inputs list
   outputs: outputs list
   buckets: histogram horz axis list
   counts: histogram vert axis list
   }
   '''
   rawfile = open(directory+filename, 'r')
   file = csv.reader(rawfile)
    
   inputs = []
   outputs = []
   counter = 0
   for eachrow in file:
      if (counter > ignore_row):
         inputs.append( float(eachrow[ignore_col+0]) )
         outputs.append( int(eachrow[ignore_col+1]) )
      counter = counter + 1
    
   largest_output = max(outputs)
   num_bits = int(np.ceil(np.log2(largest_output)))
    
   buckets = []
   counts = []
   
   for i in range(2**num_bits):
      buckets.append(i)
      counts.append(0)
      
   for each in outputs:
      counts[each] = counts[each] + 1
   
   rawfile.close()
   cache = calculate_dnl_inl_histogram(buckets, counts)
   inl = cache['inl']
   dnl = cache['dnl']
   
   return {'inputs': inputs,
           'outputs': outputs,
           'buckets': buckets,
           'counts': counts,
           'inl': inl,
           'dnl': dnl,
           }

def plot_histogram(buckets, counts, name='histogram'):
   '''
   This function plots the histogram of an ADC.
   buckets: all the codes available
   counts: frequency of code
   '''
   # need to set the range well
   average_count = sum(counts[1:-1])
   average_count = average_count / (len(counts)-2)
   plt.title(name)
   plt.plot(buckets, counts)
   plt.ylabel('Counts')
   plt.ylim([0,average_count * 2])
   plt.xlabel('Codes')
   plt.grid(True)

def plot_ramp(inputs, outputs, name='ramp'):
   '''
   This function plots the transfer function of an ADC.
   inputs: input DAC codes
   outputs: ADC output
   '''
   plt.title(name)
   plt.plot(inputs,outputs)
   plt.ylabel('Outputs')
   plt.xlabel('Inputs')
   plt.grid(True)

def calculate_dnl_inl_histogram(buckets, counts):
   '''
   This function calculates the DNL
   '''
   # calculate average step size
   avg_counts = sum(counts[1:-1]) # exclude lowest & highest codes
   avg_counts = avg_counts / (len(counts)-2) # exclude highest & lowest codes
   
   dnl = []
   for each_count in counts:
      dnl_figure = (each_count - avg_counts) / avg_counts
      dnl.append(dnl_figure)
   
   inl = [0]
   inl_figure = 0
   # exclude for both end points
   for each_dnl in dnl[1:-1]:
      inl_figure = inl_figure + each_dnl
      inl.append(inl_figure)
   inl.append(0)
   
   return {'inl': inl, 'dnl': dnl}

def plot_inl(buckets, inl, name='INL'):
   plt.title(name)
   plt.plot(buckets, inl)
   plt.ylabel('LSB')
   plt.xlabel('Codes')
   plt.grid(True)

def plot_dnl(buckets, dnl, name='DNL'):
   plt.title(name)
   plt.plot(buckets, dnl)
   plt.ylim([-2,2])
   plt.ylabel('LSB')
   plt.xlabel('Codes')
   plt.grid(True)

def eval_adc(directory, filename):
   cache = extract_ramp(directory, filename)
   plt.figure()
   plt.subplot(2,2,1)
   plot_histogram(cache['buckets'], cache['counts'])
   plt.subplot(2,2,2)
   plot_ramp(cache['inputs'],cache['outputs'])
   plt.subplot(2,2,3)
   plot_dnl(cache['buckets'], cache['dnl'])
   plt.subplot(2,2,4)
   plot_inl(cache['buckets'], cache['inl'])