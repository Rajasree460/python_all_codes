#gcd(greatest common diviser)
a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
while(a!=b):
    if(a>b):
        a=a-b
    else:
        b=b-a
print("gcd:",a)