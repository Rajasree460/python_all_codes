#pyramid pat
def pyramid_pat(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
#main func
n=int(input("enter the height:"))
pyramid_pat(n)                                 