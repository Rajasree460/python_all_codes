#swap without using temp variable
def swap(a,b):
    a,b=b,a
    print("after swapping:",a,b)    
#main function
num1=int(input("enter the 1st no.:"))   
num2=int(input("enter the 2nd no.:"))   
print("before swapping:",num1,num2)
swap(num1,num2)