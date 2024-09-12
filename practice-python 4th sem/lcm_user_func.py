#lcm by user defined & func
def lcm(a,b,a1,b1):
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    lcm=(a1*b1)/a
    print("lcm:",int(lcm))             
#main function
a=int(input("enter the 1st no:"))
b=int(input("enter the 2nd no:"))  
a1=a
b1=b 
lcm(a,b,a1,b1)      