# Creating a function definition that is the last merge
# The last two lists that will be merged and sorted together

def mergeSorted(l1,l2):
  
  """
  This function takes two lits. It is the last function of a merge sort
  It takes each element in first list with each corresponding elements 
  the second list and compares. It puts the smalles element into a new list
  and keeps moving incrementally in the other two lists repeating the same
  """
  
  # get some iterators initialised to zero to move through the sorted lists
  i,j = 0,0
  sortedList = []
  
  while i < len(l1) and j < len(l2): # If l1 reaches last elem and l2 has more elements the loop still breaks
    if l1[i] < l2[j]:
      sortedList.append(l1[i])
      i += 1
    else:
      sortedList.append(l2[j])
      j += 1
  # to append the remaining elements if any in one of the lists
  while i < len(l1):
    sortedList.append(l1[i])
    i += 1
  while j < len(l2):
    sortedList.append(l2[j]),
    j += 1
  
  return sortedList


# Recrsive division of the list into individual elements
ll = [8,6,2,5]

def recursiveDivide(l):
  
  """
  The list takes in a list as an input. Keeps dividing it cintinuously until it breaks into indivisual 
  elements. This is done by using recursion - A function calling itself. Later on merging will be included  
  """

  
  if len(l) < 2:
    # print("Reached the base conditions, no splits possible, the list contains {} ".format(l))
    return l[:]

  else:
    mid = len(l) // 2 # floor division , rounds off
    list1 = recursiveDivide(l[:mid])
    list2 = recursiveDivide(l[mid:])
    return mergeSorted(list1, list2)

    
# send to sorted lists to the mergeSorted function and merge them  by sorting
l = [6,8,1,4,10,7,8,9,3,2,5]
print(recursiveDivide(ll))

    
  