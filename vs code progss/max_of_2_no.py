# Python program to find the maximum of two numbers
def maximum(a, b): 
 if a >= b:
  return a
 else:
  return b
 
# Driver code(main func)
A = float(input("enter 1st no.: "))
B = float(input("enter 2nd no.: "))
print(maximum(A, B))