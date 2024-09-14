#Array user input
a=[]  #array=a[]
n=int(input("Number of elements in array(lrngth of the array):"))
print("enter your array elements:")
for i in range(0,n):
 l=int(input())  #for taking input(working like scanf anf Scanner)
 a.append(l)     #inserting the elements 
print("your array is:"+str(a))   #for printing the array in the same line(horizontally)
#print("your array is:")   
#print(a)                #for printing the array at next line
#OTHER WAY TO PRINT
# print("your array is: ")
# for i in a:
#    print(i)   #printing vertically