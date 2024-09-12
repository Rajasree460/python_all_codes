#lcm
def gcd(a,b,a1,b1):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    print("gcd:",a)
    lcm=(a1*b1)/a
    print("lcm:",int(lcm))         
#main func
a=int(input("enter 1st no:"))  
b=int(input("enter 2nd no:"))  
a1=a
b1=b   
gcd(a,b,a1,b1)