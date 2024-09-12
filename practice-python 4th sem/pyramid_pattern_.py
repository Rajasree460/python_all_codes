#pyramid pattern
def pattern(n):
    for i in range(0,n):
         for j in range(0,i+1):
             print("*",end=" ")
         print("\n")      
#main func
n=int(input("enter the height:"))  
pattern(n)       