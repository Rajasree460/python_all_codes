#perfect no
def perfect_no(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print("perfect")
    else:
        print("not perfect") 
#main func
n=int(input("enter a no:")) 
perfect_no(n)                   