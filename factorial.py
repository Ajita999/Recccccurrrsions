
def factorialRecursive(num):
  if num ==1:
    return num
  return num * factorialRecursive(num-1)

def factorialIterative(num):
  factorial = 1
  for i in range(1,num+1):
    factorial = factorial*i
  return factorial

print(factorialRecursive(5))
print(factorialIterative(5))