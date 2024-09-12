#lcm
def lcm(a,b):
    a1=a
    b1=b
    while a!=b:
        if(a>b):
            a=a-b
        else:
            b=b-a
    print("gcd:",a)
    lcm=(a1*b1)/a
    print("lcm:",lcm)
#main func
a=int(input("enter 1st no:"))  
b=int(input("enter 2nd no:"))     
lcm(a,b)                