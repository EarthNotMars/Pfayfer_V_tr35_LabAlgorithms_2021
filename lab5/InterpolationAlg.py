import numpy as np
from time import process_time 
import os, psutil
import matplotlib.pyplot as plt
import copy
from numpy import random

t1 = 0
ts = 0
k = 0
x = np.random.choice(101, 100) #creating list without repetitions (1,- random size 100, - arr size)
constX = x #memory list items and their orders 
process = psutil.Process(os.getpid())
x = sorted(x)

# Python3 program to implement
# interpolation search
# with recursion
 
# If x is present in arr[0..n-1], then
# returns index of it, else returns -1.
 
 
def interpolationSearch(arr, lo, hi, val):
 
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (lo <= hi and val >= arr[lo] and val <= arr[hi]):
 
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (val - arr[lo]))
 
        # Condition of target found
        if arr[pos] == val:
            return pos
 
        # If x is larger, x is in right subarray
        if arr[pos] < val:
            return interpolationSearch(arr, pos + 1,
                                       hi, val)
 
        # If x is smaller, x is in left subarray
        if arr[pos] > val:
            return interpolationSearch(arr, lo,
                                       pos - 1, val)
    return -1
 
# Driver code
 
 
# Array of items in which
# search will be conducted
n = len(x)
# Element to be searched

 
# This code is contributed by Hardik Jain

while k<=1000:
    t1_start = process_time()
    index = interpolationSearch(x, 0, n - 1, 20000) #(array, min index 0, max index n - 1, searching value-  900)
    t1_stop = process_time()
    t1 = t1_stop - t1_start
    ts = ts + t1
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")
    t1_start = 0
    t1_stop = 0
    k=k+1
print("Time elapsed:", ts)
print("Memory Usage:", (process.memory_info().rss))  # in Mbits