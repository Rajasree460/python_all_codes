#rect sq area
def rect_area(l,w):
    area=l*w
    print("the area of rect:",area)
def sq_area(l):
    area=l*l
    print("the area of sq:",area)    
#main func
length1=int(input("enter the length of the rect:"))    
width1=int(input("enter the width of the rect:"))   
length2=int(input("enter the lengthof sq:")) 
rect_area(length1,width1)
sq_area(length2)