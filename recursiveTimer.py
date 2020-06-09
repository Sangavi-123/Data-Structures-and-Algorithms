import time

"""
Important thing to note in recursion is that the variables that are
passed to a function that contains a recursive call in it, are stored
in a global frame and their values arent changed, even though they may 
seem so.

For example down below, a variable n is defined with value 10 
and passed through the function with recursion. The value of n
keeps decrementing inside the function and that is also printed out
But when the variable n is printed outside the function definition 
it still has the same value 10, held in the global frame
"""

# recursive countdown timer
def recurTimer(n):
  
  if n == 0:
    return n
  else:
    print(n)
    time.sleep(1)
    return recurTimer(n-1)


n = 10    
print(recurTimer(n))
