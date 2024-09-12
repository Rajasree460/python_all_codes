#bubble sort
def bubble_sort_a(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    print("the sorted array(ascending):",list)             
def bubble_sort_d(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]<list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp    
    print("the sorted array(adescending):",list)             
#main function
list=[]
n=int(input("enter the length of the array:"))
print("enter your array elements:")
for i in range(0,n):
    l=int(input())
    list.append(l)   
print("unsorted array:",list)
bubble_sort_a(list) 
bubble_sort_d(list)                             