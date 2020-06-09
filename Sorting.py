import time
from random import randint, choice
l = [6,8,1,4,10,7,8,9,3,2,5]
l = [randint(1,1000) for i in range(0,1000)]

# Bubble sort
def bubbleSort(l): 
  swap = True
  while swap:
    swap = False    
    for i in range(len(l)-1):
      if l[i] > l[i+1]:        
        #swap happens here
        l[i], l[i+1] = l[i+1], l[i]
        swap = True  
  return l


def selectionSort(l):  
  for num in range(len(l)):
    for item in range(num,len(l)):
      if l[num] > l[item]:
        
        #swap happens here
        l[num], l[item] = l[item], l[num]
  return l



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


l = [randint(1,1000) for i in range(0,100)]
insertionSort(l)


def sortNmerge(l1, l2):
  i,j = 0,0
  new = []
  while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
      new.append(l1[i])
      i += 1
    else:
      new.append(l2[j])
      j += 1
  while i < len(l1):
    new.append(l1[i])
    i += 1
  while j < len(l2):
    new.append(l2[j])
    j += 1
  return new

    
#mergeSort
def mergeSort(l):

  if len(l) < 2:
    return l[:]
  else:
    mid = len(l) // 2
    list1 = mergeSort(l[:mid])
    list2 = mergeSort(l[mid:])
    return sortNmerge(list1, list2)
l = [6,8,1,4,10,7,8,9,3,2,5]
print(mergeSort(l))

def quickSort(l):
  
  #base condition
  if len(l) < 2:
    return l
  else:
    
    pivot = l[randint(1,len(l)-1)]
    low = [item for item in l[:] if item < pivot]
    high = [item for item in l[:] if item > pivot]
    center = [item for item in l[:] if item == pivot]
    
    return quickSort(low)+center+quickSort(high)

l = [6,8,1,4,10,7,8,9,3,2,5]
print(quickSort(l))






