#bubble sort user
def bubble_sort_a(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1):
            if(list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list
def bubble_sort_d(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1):
            if(list[j]<list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list                   
#main function
list=[]
n=int(input("enter the length of the array:"))
print("enter your array elements:")
for i in range(0,n):
    l=int(input())
    list.append(l)   
print("unsorted array:",list)
print("the sorted array(asending):",bubble_sort_a(list)) 
print("the sorted array(desending):",bubble_sort_d(list))    