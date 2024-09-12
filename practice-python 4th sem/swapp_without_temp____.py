#swapp using temp
def swapp(a,b):
    a,b=b,a
    print("after swapping:",a,b)
#main func
a=int(input("enter 1st no:"))    
b=int(input("enter 2nd no:")) 
print("before swapping:",a,b)
swapp(a,b)