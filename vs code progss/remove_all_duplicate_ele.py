#remove all duplicate elements from a list
def remove(list):
    final_list=[]
    for i in list:
        if i not in final_list:
            final_list.append(i)
    return final_list
#main function
list= []  #user input
n=int(input("enter the length of your array:"))
print("take your array element:")
for i in range(0,n):  
    l=int(input())
    list.append(l)        
print("original list:",list)
print("after removing the duplicate elements the list is:",remove(list))    