
"""
Factorial using recursion is based on this formula of factorial which is n(n-1)!
n is multiplied with recursive function call. Each of this function calls will 
recursively return back numbers multiplied with the number next to it

The last function call will have n = 0, hence it will return 1 which will then
multiply the corresponding value of n (1) and return it to function that called it
That will multiply one with n =2, which will be returned to function that called it
That wil multiply 2 with n= 3 and return 6 to the function that called it. Which will
then multiply 6 with n = 4 and return it to the function that called it. Then it will
multiply 24 with n = 5 and return it to the function that called it which is the 
GLOBAL FUNCTION  call. Hence it will return the value 120 which is the factorial of 5
"""
def recurFactorial(n):
  
  if n == 0:
    return 1
  else:
    return n * recurFactorial(n-1)

recurFactorial(4)