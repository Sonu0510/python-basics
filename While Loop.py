# Printing numbers from 0 to 4 with while loop
print("Using while loop")
i = 0
while i < 5:
    print(i)
    i += 1
print("*---------------------------*--------------------------*\n")

# Printing numbers from 0 to 4 using for loop
print("Using for loop")
for num in range(0, 5):
    print(num)
print("*---------------------------*--------------------------*\n")

# Print characters in string

# Using for loop
for char in "strings":
    print(char)
print("\n")

# Using while loop
string = "Yugendra Ray"
i = 0
while i < len(string):
    print(string[i])
    i += 1
print("\n")


# Printing Fibonacci sequence
print("Fibonacci sequence using while loop")
n = 10
fibonacci_sequence = [0, 1]

while len(fibonacci_sequence) < n:
    next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_num)

print(fibonacci_sequence)
print("\n")

print("Fibonacci sequence using for loop")

a = 0
b = 1
n = int(input("Get Fibonacci sequence up to entered num: "))
for num in range(n):
    if a == 0:
        print(a)
    a, b = b, a+b
    print(b)

