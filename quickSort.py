import time
# l = [6,8,1,4,10,7,8,9,3,2,5]



def quickSort(l):
  count = 0
  
  if len(l) < 2:
    return l[:]
 
  else:
    
    print("At the beginning: {}".format(l))
    pivot = l[-1]
    print("pivot is {}".format(pivot))

    center, high, low = [], [], []

    for i in range(len(l)):
     
      if l[i] < pivot:
        low.append(l[i])
      elif l[i] > pivot:
        high.append(l[i])
        count += 1
        # print(high)
      else:
        center.append(l[i])
    print("Combined: {}".format(low+center+high))
    
    return quickSort(low)+center+quickSort(high)


l = [1, 4, 3, 2, 5, 6, 8, 7, 8, 9, 10]

print(quickSort(l))



# quick sort from Grokking Algorithms

def quickSort1(l):
  
  #define the base case for the recursion to stop with
  if len(l) < 2:
    return l
  else:
    pivot = l[0]
    small = [i for i in l[1:] if i <= pivot]
    large = [i for i in l[1:] if i > pivot]
    return quickSort1(small) + [pivot] + quickSort1(large)


print(quickSort1(l))    
print(timeit.timeit(quickSort1(l)))
    
    
    
    