# Diamond pattern another shape
n=int(input('enter the height:'))
for i in range(0,n):
    for j in range(0,(n-1)-i):
        print(" ",end="") #for space,end=""(for new line, as well as space)
    for k in range(0,i+1):
        print("* ",end="") 
    print()      
for i in range((n-1),0,-1):
    for j in range((n-1)-(i-1),0,-1):
        print(" ",end="") #for space,end=""(for new line, as well as space)
    for k in range(i):
        print("* ",end="") 
    print()      