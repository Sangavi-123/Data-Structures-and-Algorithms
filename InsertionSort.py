import numpy as np


l = [6,1,8,4,10]
l1 = [2,6,11,90,3,2,4]
l3 = [17,2,9,3,7]


# Algorithm

"""
the algorithm iterated from the first element and not the zeroth element.
it compare each element with previous elements and if the other element is large, 
it is swappped. Now the element [identity - just a name] which is before the swapped index is checked and
it is repeated until there is no element at all.

this process is repeated for each element in the list

"""

def insertionSort(l):
  
  for i in range(1,len(l)):
    if l[i] < l[i-1]:
      #swap
      l[i],l[i-1] = l[i-1],l[i]
      key = i-1
      while(key!=0):
        if l[key] < l[key-1]:
          #swap
          l[key], l[key-1] = l[key-1], l[key]
        key -=  1
  return l

print(insertionSort(l3))



