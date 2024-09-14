#lcm(least common multiple)
a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
a1=a
b1=b
while(a!=b):
    if(a>b):
        a=a-b
    else:
        b=b-a
print("gcd of",a1,"and",b1,"is:",a)
lcm=int((a1*b1)/a)
print("lcm of",a1,"and",b1,"is:",lcm)