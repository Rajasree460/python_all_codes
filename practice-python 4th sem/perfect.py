#perfect no.
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    if(sum==n):
        print("perfect no")
    else:
        print("not perfect no")          
#main func
n=int(input("enter a no:"))
perfect(n)