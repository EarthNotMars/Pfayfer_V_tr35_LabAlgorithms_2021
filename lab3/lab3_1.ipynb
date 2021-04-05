#Generation of single-list with 10 000 elements and checking methods 
#src:https://www.educative.io/
#Lab3: V8 Vova Pfayfer 

import numpy as np
from time import process_time 
import os, psutil
import matplotlib.pyplot as plt
import copy
from numpy import random

t1 = 0
x = random.randint(1000000, size=(10000)) #creating list
process = psutil.Process(os.getpid())

#A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
    
  def deleteHead(self): #sam write
    if(self.head):
      current = self.head
      self.head = current.next
    else:
        return
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

# Singly Linked List with insertion and print methods
LL=LinkedList()
for i in x:
    LL.insert(i)

    
for k in range(1,10001,1):
    t1_start = process_time()
    LL.insert(random.randint(0,50000))
    t1_stop = process_time()
    t=t1_start+t1_stop
    t1=t1+t
    LL.deleteHead()
    av_t=t1/10000
print("average t for 10000 elements is: ", av_t)
    
    
    
print("Memory Usage:", (process.memory_info().rss))  # in Mbits
    
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([50, 100, 500, 1000, 2000, 5000, 10000], [2.84, 2.77, 3.45, 3.92, 4.82, 9.57, 18.9])  # Plot some data on the axes.
plt.ylabel('Time')
plt.xlabel('number of elements in single list')

fig, mx = plt.subplots()  # Create a figure containing a single axes.
mx.plot([50, 100, 500, 1000, 2000, 5000, 10000], [787, 785, 786, 787, 792, 797, 806])  # Plot some data on the axes.
plt.ylabel('Memory')
plt.xlabel('number of elements in single list')
