def fibonacciRecursive(n): #O(2^n)
  if (n<2):
    return n

  return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
    
    
  
  
def fibonacciIterative(num): #O(n)
  fib = [0,1]
  for i in range(2,num+1):
    fib.append(fib[i-1]+fib[i-2])
    
  return fib[num]
  

print(fibonacciRecursive(8))
print(fibonacciIterative(8))