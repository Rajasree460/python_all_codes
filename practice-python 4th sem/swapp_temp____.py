#swapp using temp
def swapp_temp(a,b):
    temp=a
    a=b
    b=temp
    print("after swapping:",a,b)
#main func
a=int(input("enter 1st no:"))    
b=int(input("enter 2nd no:")) 
print("before swapping:",a,b)
swapp_temp(a,b)