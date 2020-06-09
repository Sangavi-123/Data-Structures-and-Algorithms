"""
This file is an analyser to analyse the running time of various sorting algorithms
The sorting algorithms are defined as functions in python file called Sorting.py
The file is imported with the function names. Then each function is called and
the start and end time is noted followed by the elapsed time for each algorithm
"""


# step 1: Get input from user for the maximum integer and the range
# step 2: note the start and the end time for each function promptly before and after calling the function 
# step 3: find the time elapsed


import time
from random import randint
import os
from Sorting import bubbleSort, insertionSort, selectionSort, mergeSort, quickSort, sortNmerge

os.chdir("C:\\Users\\sangavi\\Desktop\\Courses\\DataStructuresAndAlgorithms\\codes\\LectureCodes\\Algorithms")


# Get input from user
def inpuT():
  
  maxim = int(input("Enter the maximum value in the list"))
  rangE = int(input("Enter the total number of elements you want in the list"))
  
  l = [randint(1,maxim) for i in range(1, rangE)]
  return l

l = inpuT()


# function to calculate the elapsed time

def calcTime(funcName, l):
  """
  

  Parameters
  ----------
  1) pass a function. Ex - bubblesort func, selectionSort func, insertionSort func
  2) a list on which the passed function should be executed upon

  func : 
  Take the list of eleemnts passed and run the passed sorting function on it
  

  Returns
  -------
  Time it took to sort using the function passed

  """
  
  start = time.time()
  funcName(l)
  end = time.time()
  
  return (f"The elapsed time for {funcName.__name__} is          -> {end-start}")


# run it for n number of times, get n from the user too
nTimes = int(input("How many time so you want to run the sorting functions"))

for i in range(nTimes):
  print(f"num :{i+1}")
  print(calcTime(bubbleSort, l.copy()))
  print(calcTime(selectionSort,l.copy()))
  print(calcTime(insertionSort,l.copy()))
  print(calcTime(mergeSort,l.copy()))
  print(calcTime(quickSort,l.copy()))
  print('-'*50)


