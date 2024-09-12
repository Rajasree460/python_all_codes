#swapp without temp
def swap_without_temp(a,b):
    a,b=b,a
    print("after swapping:",a,b) 
#main function
a=int(input("enter the 1st no.:"))   
b=int(input("enter the 2nd no.:"))   
print("before swapping:",a,b)
swap_without_temp(a,b)     