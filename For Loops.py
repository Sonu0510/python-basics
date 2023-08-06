print("\n")


# program that takes a string as input and counts the number of vowels (a, e, i, o, u) using a for loop.
string = input("Enter something: ")
vowels_in_string = []
consonants_in_string = []
for char in string:
    if char in "aeiouAEIOU":
        vowels_in_string.append(char)
    elif char not in "aeiouAEIOU ,.<>!@#$%^&*()'\"\/[]{}&*-_+=~`?":
        consonants_in_string.append(char)
print("Vowels in given string are", vowels_in_string)
print("Number of vowels in given string is", len(vowels_in_string))
print("\n")
print("Consonants in given string are", consonants_in_string)
print("Number of consonants in given string is", len(consonants_in_string))

print("*----------------*--------------------*------------------------*\n")

# Display file contents using for loop
with open("microsoft.txt", "r") as file:
    for line in file:
        print(line)
print("*----------------*--------------------*------------------------*\n")
# For loop is used for iterating over a sequence

list_of_num = [990, 1, 10, 20, 33, 4, 243, 32, 55]
list_of_num.sort()

for num in list_of_num:
    if num % 2 == 0:
        print(f"Even: {num}")
    else:
        print(f"Odd: {num}")
print("*----------------*--------------------*------------------------*")

for i in range(10):
    print("*" * i)
print("*----------------*--------------------*------------------------*")


var = "*"
for i in range(5):
    print(var * i)
print("*----------------*--------------------*------------------------*")

for i in range(4):
    print("a" * (i+1))
print("*----------------*--------------------*------------------------*\n")

while i in range(10):
    print(i)
    i = i +1

print("*----------------*--------------------*------------------------*\n")

start_idx = 1
end_idx = 3

for i in range(start_idx, end_idx):
  for j in range(start_idx, end_idx):
    print((i, j))




#
# Q.2 Write a program that generates all possible combinations of three numbers from 1 to 5 using nested for loops and prints them.
# for i in [1, 5]:
#   for j in [1, 5]:
#     for k in [1, 5]:
#       print((i, j, k))
