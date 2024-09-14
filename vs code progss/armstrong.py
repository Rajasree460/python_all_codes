# Function to check whether the given number is Armstrong number or not
def isArmstrong(x):
 copy=x
 rev = 0
 
 while (x!= 0):
  rem = x% 10
  rev = rev + (rem*rem*rem)
  x= x // 10
 # If condition satisfies
 if(copy==rev):
     print("armstrong no.")
 else:
     print("not armstrong no.")    
# Driver code
x = int(input("enter a no.: "))
print(isArmstrong(x))