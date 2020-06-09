l =    [1,2,3,4,5,6,7,8,9,10]


"""
  

The bisect search is otherwise called as binary search where it takes a sorted list as input
Then gets the midpoint of the list (does not change the indices of the list). Checks if the 
number required is in the midpoint of the array. If absent, and if the number required is 
greater than the number in the midpoint, the start is changed to index next to the current 
midpoint. Otherwise if the number is less than the one that is searched, then the stop is 
changed to the index just before the current midpoint. This task is repetitively done until
the start point is lesser than or equal to the stop point. Should this condition fail, the
function returns that the number is not found in the list

1) first implementation is iterative
2) Second implementation is recursive

"""

def bisectSearch(n,arr):
  
  start = 0
  stop = len(arr)-1
  
  while start <=  stop:
    
    mid = (start + stop) // 2
    print(arr[mid])
    
    if arr[mid] == n:
      return f"{n} found at index : {arr[mid]}"
    elif n > arr[mid]:
      start = mid + 1
    else:
      stop = mid - 1 
  return "The number is not in list"
  
  
print(bisectSearch(3,l))



"""
The  binary search is implemented using reecursive function
The same methodology as above, except for while loop.
"""

l =    [1,2,3,4,5,6,7,8,9,10]
def recurBisect(n,l,start, stop):
  
  """
  the funcction takes in an array, finds the element in the midpoint.
  IF that is the element searched for returns it. Or it checks if the
  element is higher the midpoint and changes the start to index next
  to midpoint. If otherwise, stop is changed to index before midpoint.
  This happens recursively until element is found in the list. Base 
  condition is that, if the start is start index is higher then the
  stip index, the funtion returns that the list does not contain the
  element searched for.

  """
  
  if start > stop:
    return f"Element not found in the list"
  else:
    mid = (start+stop)//2
    if l[mid] == n:
      return f"{n} found at index {mid}"
    elif n > l[mid]:
      return recurBisect(n,l,mid+1, stop)
    else:
      return recurBisect(n,l,start,mid-1)

print(recurBisect(8,l,0,len(l)-1))

for i in range(1,16):
  print(recurBisect(i,l,0,len(l)-1))








list1 = [randint(1,1000) for i in range(0,100)]
print(recurBisect(10, list1, 0, len(list1)-1))      
  





