#bubble sort asending and desending
def bubble_sort_a(list):  
    for i in range(0,len(list)-1):  
        for j in range(0,len(list)-1):  
            if(list[j]>list[j+1]):  
                temp = list[j]  
                list[j] = list[j+1]  
                list[j+1] = temp  
    return list  
def bubble_sort_d(list):  
    for i in range(0,len(list)-1):  
        for j in range(0,len(list)-1):  
            if(list[j]<list[j+1]):  
                temp = list[j]  
                list[j] = list[j+1]  
                list[j+1] = temp  
    return list  
#main function
#Array user input
list=[]  #array=list[]
n=int(input("Number of elements in array(lrngth of the array):"))
print("enter your array elements:")
for i in range(0,n):
 l=int(input())  #for taking input(working like scanf anf Scanner)
 list.append(l)     #inserting the elements 
print("The unsorted list is: ",list)   #for printing the array in the same line(horizontally)
                                       #as well can ,print("The unsorted list is: ",str(list))
print("The sorted list is(asending): ", bubble_sort_a(list))
print("The sorted list is(desending): ", bubble_sort_d(list))