#area of rect and sq
def rect_area(l,b):
    area=l*b
    print("rect area:",area)
def sq_area(l):
    area=l*l
    print("sq area:",area)
#main func
l=int(input("enter length:"))  
b=int(input("enter breadth:"))     
rect_area(l,b)   
sq_area(l)