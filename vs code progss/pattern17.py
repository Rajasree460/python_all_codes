#pattern 17 
n = int(input("Enter number of rows(height): "))
for i in range(n):
 for j in range(i+1):
  print(j+1, end="")
 print()
