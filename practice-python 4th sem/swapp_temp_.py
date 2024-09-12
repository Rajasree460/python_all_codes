#swapp by temp
def swap_temp(a,b):
    temp=a
    a=b
    b=temp
    print("after swapping:",a,b)
#main function
a=int(input("enter the 1st no.:"))   
b=int(input("enter the 2nd no.:"))   
print("before swapping:",a,b)
swap_temp(a,b)    