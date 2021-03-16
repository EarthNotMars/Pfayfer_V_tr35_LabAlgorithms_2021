import numpy as np
from time import process_time 
import os, psutil
import matplotlib.pyplot as plt
import copy

x = np.arange(1,100001,1) #creating list
print(x)
y=[]
y= list(x) 
k=0
  
t1_start = process_time()
for i in range(1,1000):
    start = process_time()
    for n in x[:900]:
        y.pop(400)
    stop = process_time()
    k=k+stop
    for n in x[:900]:
        y.append(x)
    
t=k/1000
print("average time t - ", t)
plt.plot([50, 100, 500, 1000, 2000, 5000, 10000], [2.4, 3.25, 10.8, 20, 38.3, 91, 177.7])
