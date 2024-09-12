#the area of rectangle and square by function
def rect_area(length1,width1):
    area1=length1*width1
    print("the area of the reactangle is:",area1)    
def sq_area(length2,width2):
    area2=length2*width2
    print("the area of the reactangle is:",area2)
#main function
length1=int(input("enter the len of rec:"))
width1=int(input("enter the width of rec:"))
length2=int(input("enter the len of sq:"))
width2=int(input("enter the width of sq:"))
rect_area(length1,width1)
sq_area(length2,width2)