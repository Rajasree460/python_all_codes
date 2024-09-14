#diamond pattern(user defined) with space
n=int(input('enter the height:'))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end=" ") #for space,end=""(for new line)
    for k in range(0,2*i+1):
        print("*",end=" ") 
    print()      
for i in range(n-1,0,-1):
    for j in range(0,n-i):
        print(" ",end=" ") #for space,end=""(for new line)
    for k in range(0,2*i-1): 
        print("*",end=" ")       
    print()       