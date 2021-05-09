import numpy as np
from time import process_time 
import os, psutil
import matplotlib.pyplot as plt
import copy
from numpy import random
process = psutil.Process(os.getpid())
t1 = 0
ts = 0
k = 0
list1=np.random.choice(101, 100)
list1 = sorted(list1)
val=2
if list1[0] == val:
    print("0")
i = 1
#Finding range for binarySearch
while(i<len(list1) and list1[i]<=val):
        i = i * 2
min1=min(i,len(list1))
def binarySearch(data_list,low,high,value):
    if(high>= low):
        mid=int(low + ( high-low )//2)
        if data_list[mid] == value:
            return mid
        if data_list[mid] > value:
            return binarySearch(data_list,low,mid - 1,value)
        else:
            return binarySearch(data_list,mid + 1,high,value)
    if(high<low):
        return -1
 
# Driver code
 
 


 
# This code is contributed by Hardik Jain

while k<=1000:
    t1_start = process_time()
    index=binarySearch(list1,i/2,min(i,len(list1)),val)
    t1_stop = process_time()
    t1 = t1_stop - t1_start
    ts = ts + t1
    if(index==-1):
        print("Element not found")
    else:
        print("Element found at ",index)
    t1_start = 0
    t1_stop = 0
    k=k+1
print(list1)
print("Time elapsed:", ts)
print("Memory Usage:", (process.memory_info().rss))  # in Mbits