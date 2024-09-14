#gcd without recursion and not user defined
a=20
b=10
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print (a)