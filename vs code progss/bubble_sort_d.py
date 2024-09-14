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
list = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list)  
print("The sorted list is(asending): ", bubble_sort_a(list))
print("The sorted list is(desending): ", bubble_sort_d(list))