#perfect no.
n=int(input("enter a no:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
    print("perfect no.")
else:
    print("not perfect no.")            