#rect & sq area
def rect_area(l,b):
    area=l*b
    print("rect area:",area)
def sq_area(l):
    area=l*l
    print("sq area:",area)    
#main function
length1=int(input("enter the len of rec:"))
width1=int(input("enter the width of rec:"))
length2=int(input("enter the len of sq:"))
rect_area(length1,width1)
sq_area(length2)    