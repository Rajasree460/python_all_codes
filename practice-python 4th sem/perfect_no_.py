#perfect no
def perfect_no(n):
    sm=0
    for i in range(1,n):
        if n%i==0:
            sm=sm+i
    if sm==n:
        print("perfect no.")
    else:
        print("not perfect no.")        
#main func
n=int(input("enter a no:"))
perfect_no(n)            