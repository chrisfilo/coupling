

import numpy as np
import pandas as pd

def coupling(data,smooth):
    """
        creates a functional coupling metric from 'data'
        data: should be organized in 'time x nodes' matrix
        smooth: smoothing parameter for dynamic coupling score
    """
    
    #define variables
    [tr,nodes] = data.shape
    der = tr-1
    td = np.zeros((der,nodes))
    td_std = np.zeros((der,nodes))
    data_std = np.zeros(nodes)
    fc = np.zeros((der,nodes,nodes))
    sma = np.zeros((der,nodes*nodes))
    
    #calculate temporal derivative
    for i in range(0,nodes):
        for t in range(0,der):
            td[t,i] = data[t+1,i] - data[t,i]
    
    
    #standardize data
    for i in range(0,nodes):
        data_std[i] = np.std(td[:,i])
    
    td_std = td / data_std
   
   
    #functional coupling score
    for t in range(0,der):
        for i in range(0,nodes):
            for j in range(0,nodes):
                fc[t,i,j] = td[t,i] * td[t,j]


    #temporal smoothing
    temp = np.reshape(fc,[der,nodes*nodes])
    temp = temp.transpose() # numpy transpose????
    sma = pd.rolling_mean(temp,smooth)
    sma = np.reshape(sma,[der,nodes,nodes])
    
    return (fc, sma)
    
    

#input the variables 'd' (data) and 's' (smooth) 
#I've made 'd' random for now, but this could just as easily be real data
d = np.random.rand(200,5)
s = 9

#run the script
coupling(d,s)
