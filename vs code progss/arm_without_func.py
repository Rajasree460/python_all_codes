# Python program to check if the number is an Armstrong number or not
num = int(input("Enter a number: "))
rev = 0
copy = num
while num > 0:
 rem = num % 10
 rev += rem ** 3
 num //= 10  #num=num//10
# display the result
if copy == rev:
 print(copy,"is an Armstrong number")
else:
 print(copy,"is not an Armstrong number")
