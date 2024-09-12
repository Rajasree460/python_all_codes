#gcd by user anf func
def gcd(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    print("gcd:",a)                
#main function
a=int(input("enter the 1st no:"))
b=int(input("enter the 2nd no:"))   
gcd(a,b)      