#pattern 11(user defined) with space
n=int(input('enter the height:'))
for i in range(0,n):
    for j in range(0,(n-1)-i):
        print(" ",end=" ") #for space,end=""(for new line)
    for k in range(0,i+1):
        print("*",end=" ") 
    print()      