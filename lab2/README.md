import numpy as np <br />
from time import process_time   <br />
import os, psutil  <br />
import matplotlib.pyplot as plt <br />
import copy <br />

x = np.arange(1,100001,1) #creating list <br />
print(x) <br />
y=[] <br />
y= list(x) <br />
k=0 <br />
  
t1_start = process_time() <br />
for i in range(1,1000): <br />
    start = process_time() <br />
    for n in x[:900]: <br />
        y.pop(400) <br />
    stop = process_time() <br />
    k=k+stop <br />
    for n in x[:900]: <br />
        y.append(x) <br />
    
t=k/1000 <br />
print("average time t - ", t) <br />
plt.plot([50, 100, 500, 1000, 2000, 5000, 10000], [2.4, 3.25, 10.8, 20, 38.3, 91, 177.7]) <br />
