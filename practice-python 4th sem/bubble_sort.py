#bubble sort
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
list=[3,5,8,2,1,7,6]    
print("unsorted array:",list)
print("the sorted array(asending):",bubble_sort_a(list)) 
print("the sorted array(desending):",bubble_sort_d(list))    