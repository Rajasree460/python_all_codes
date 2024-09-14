#pattern 10 with space
n=4
b=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(b,end=" ")
        b+=2
    print()     