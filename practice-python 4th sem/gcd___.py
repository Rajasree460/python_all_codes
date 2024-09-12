#gcd
def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    print("the gcd:",a)   
#main func
a=int(input("enter 1st no:"))    
b=int(input("enter 2nd no:")) 
gcd(a,b)