#hollow sq
def hollow_sq(n):
    for i in range(0,n):
        for j in range(0,n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("&",end=" ")
            else:
                print(" ",end=" ")
        print()        
#main func
n=int(input("enter the height:"))         
hollow_sq(n)                    