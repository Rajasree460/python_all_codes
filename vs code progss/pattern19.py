#pattern 19 
n = int(input("Enter number of rows(height): "))
ascii_value = 65
for i in range(n):
 for j in range(i+1):
  alphabet = chr(ascii_value)
  print(alphabet, end="")
 
  ascii_value += 1
 print()
