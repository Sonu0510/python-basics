print("\n")

def calculate_square_root(num):
  if num < 0:
    raise ValueError("Cannot calculate sqrt of -ve number")
  else:
    return num ** 0.5

num = -4
sqrt = calculate_square_root(4)
print(sqrt)

try:
  calculate_square_root(num)

except ValueError as e:
  print(e)







try:
  num = int(input("Enter number: "))
  result = 10/num
  print(f"Result: {result}")

except ZeroDivisionError as e:
  print(e)

except ValueError as e:
  print(e)

finally:
  print("Program execution completed")

print("\n")



# Handling multiple error
try:
  n1 = int(input("Enter number_1: "))
  n2 = int(input("Enter number_2: "))
  division = n1 / n2

except ValueError as e:
  print("Invalid input, ", e)

except ZeroDivisionError as e:
  print("Can't divide by zero, ", e)

else:
  print(division)



# Handling ZeroDivisionError
c = 10
d = 2
try:
  print(c/d)

except ZeroDivisionError as e:
  print("Something went wrong....", e)

print("\n")


# Handling ValueError
try:
  a = int(input("Input Number: "))
  print(a)

except ValueError as e:
  print("Invalid input, ", e)

print("\n")


