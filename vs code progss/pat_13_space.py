#pattern 13(pyramid) with space
n=int(input('enter the height:'))
for i in range(0,n):
    for j in range(0,2-i):
        print(" ",end=" ") #for space,end=""(for new line)
    for k in range(0,2*i+1):
        print("*",end=" ") 
    print()  