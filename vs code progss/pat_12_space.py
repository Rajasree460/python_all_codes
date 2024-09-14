#pattern 12(user defined) with space
n=int(input('enter the height:'))
for i in range(n,0,-1):
    for j in range(n-i,0,-1):
        print(" ",end=" ") #for space,end=""(for new line, as well as space)
    for k in range(i):
        print("*",end=" ") 
    print()      