# recursive fibanocci 

"""
Fibanocci series  is  aseries of numbers in which any random number chosen is the
sum of the numbers preceding it. this can be brought into a model like the one that
follows. 

f(n) = Finbanocci of nth element of a series
f(n) = f(n-1) + f(n-2)

Building this using function call
"""


n = 5
def recursiveFibanocci(n):
  
  
  # Base condition - condition that determines when the recursion stops
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return (recursiveFibanocci(n-1) + recursiveFibanocci(n-2))
  
print(recursiveFibanocci(5))



"""
Why recursion?
--------------

for ex: to find the fibanocci number of the second element in the sequence,
you must know the fibonacci number of the first and second element in the
series. to find the fib number of 3 element in the series, you should know
the fibonacci value of second and first. For second again you must know the 
fibanocci values of one and zero. For any element you would have to start
from 0 and 1.

"""



