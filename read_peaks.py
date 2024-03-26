import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

day = 26
n_tld= 7

file = 'peaks_curves/{}-02/tld_{}.csv'.format(day, n_tld)

peaks = pd.read_csv(file)

plt.plot(peaks['Temperature'], peaks['Fit.Signal'])
plt.plot(peaks['Temperature'], peaks['Peak.1'])
plt.plot(peaks['Temperature'], peaks['Peak.2'])
plt.plot(peaks['Temperature'], peaks['Peak.3'])

#Acceder a los datos guiandose por el valor maximo de un pico
npeak = 4
maximus = []
temps = []
columns = ['p1',
         'p2',
         'p3',
         'p4',
         
         't1',
         't2',
         't3',
         't4',
         ]
process_data = pd.DataFrame(columns = columns)

for tld in range(7, 17):
   
    file = 'peaks_curves/{}-02/tld_{}.csv'.format(day, tld)
    peaks = pd.read_csv(file)

    for peak in range(1, npeak + 1):
        
        max = peaks['Peak.{}'.format(peak)].max()
        ind_max = peaks['Peak.{}'.format(peak)].idxmax()
        temp_max = peaks.iloc[ind_max]['Temperature']
        
        maximus.append(max)
        temps.append(temp_max)

    df = pd.DataFrame([maximus + temps], columns = columns) 
    process_data = pd.concat([process_data, df], ignore_index=True)
    
    maximus = []
    temps = []

#save in excel file
process_data.to_excel('processed/{}-02.xlsx'.format(day))