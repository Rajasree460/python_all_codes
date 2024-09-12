#print the armstrong no in the range 1 to 1000
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 
for i in range(lower,upper + 1):
   # initialize sum
   sum = 0
   copy= i
   while i > 0:
       rem = i % 10
       sum += rem ** 3
       i //= 10
 
   if copy== sum:
     print(copy)