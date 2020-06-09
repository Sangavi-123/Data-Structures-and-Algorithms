# Bubble sort implementation


# create a list
l = [6,8,1,4,10,7,8,9,3,2,5]

# Algorithm

"""
The algorithms has two loops
Inner for loop takes each element and compares it with neighboring elements
If the element is bigger than neighbor the element is swapped. This is done
for each element in the list. But one iteration through the entire list may
not sort it completely
Hence there is an outer while loop. Because using another for loop outside may
not be efficient. The number of iterations to sort the entire list may be less 
than the total number of elements in the list
Hence while loop saves few iterations by quitting the process once all elements 
are sorted
"""
plt.ion()
# Define  a function that performs bubble sort
def bubbleSort(iterable):
  
  swap = True 
  
  while swap:
    swap = False
    for item in range(len(iterable)-1):                                       # Last element doesnt have next element
      if iterable[item] > iterable[item + 1]:
        swap = True
        iterable[item], iterable[item+1] = iterable[item + 1], iterable[item] # * Dynamic assignment
    print(iterable)
  return iterable

sortedList = bubbleSort(l)
        
        
        
        