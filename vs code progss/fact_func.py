# Python program to find factorial of given number
def factorial(n):
 # single line to find factorial
 if (n==1 or n==0):
     return 1 
 else: 
    return n*factorial(n-1)
# Driver Code
num = int(input("enter a no: "))
print("factorial of",num,"is",factorial(num))