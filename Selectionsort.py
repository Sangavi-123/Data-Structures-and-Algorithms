import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Selection Sort

"""
This is the opposite of bubble sort. Bubble sort pushes the highest element to the last index(which is left)
But in insertion sort works by pushing the least element to the first index or the left extreme
This sort contrasts bubble sort in that, it checks each element with every element(from num to end of list),
(notice here, num is the element selected in the outer loop) in the list rather than 
just neighbors. Hence the complexity is O(n^2). The elements in the right are larger than those in the left as
the algorithm propagates further.
"""



l = [6,8,1,4,10,7,8,9,3,2,5]

def selectionSort(l):

  for num in range(len(l)):
    for val in range(num,len(l)):
      
      if l[num] > l[val]:
        l[num], l[val] = l[val],l[num]
        

    print(l)
    
selectionSort(l)


# optimised algorithm using while loop
l = [6,8,1,4,10,7,8,9,3,2,5]

def selectSort(l):
  
  indexer = 0
  while indexer < len(l):
    # print(l)
    for num in range(indexer,len(l)):
      # print(indexer)
      if l[indexer] > l[num]:
        #swap
        l[indexer], l[num] = l[num],l[indexer]
    
    indexer += 1
    print(l)
      
      
selectSort(l)
      