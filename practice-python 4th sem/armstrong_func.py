#armstrong no
def armstrong(n):
    sum=0
    k=n
    while(n!=0):
        rem=n%10
        sum+=(rem*rem*rem)
        n//=10
    if(k==sum):
     print("arm")  
    else:
        print("not arm")  
#main func
n=int(input("enter a no"))
armstrong(n)        