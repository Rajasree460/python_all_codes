#swapp using temp
def swap_temp(a,b):
    temp=a
    a=b
    b=temp
    print("after swapping:",a,b)
#main func
a=int(input("enter 1st no:"))  
b=int(input("enter 2nd no:"))
print("before swapping:",a,b)    
swap_temp(a,b)    