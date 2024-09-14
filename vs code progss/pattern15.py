#pattern 15
n=int(input('enter the height:'))
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end="") #for space,end=""(for new line)
    for k in range(0,2*i-1):    
        print("*",end="")       
    print()      