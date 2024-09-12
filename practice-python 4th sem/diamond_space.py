#diamond with sapace
n=int(input("enter the no of rows:"))
for i in range(0,n):
    for j in range(0,n-1-i):
        print(" ",end=" ")
    for k in range(0,2*i+1):
        print("*",end=" ")   
    print()
for i in range(n-1,0,-1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print("*",end=" ")   
    print()