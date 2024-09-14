#swap using temp variable
def swap(a,b):
    temp=a
    a=b
    b=temp
    print("after swapping the no. is:",a,b)
#main func
a=int(input("enter 1st no.:"))    
b=int(input("enter 2nd no.:")) 
print("before swapping the no. is:",a,b)
swap(a,b)