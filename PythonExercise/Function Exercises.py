"""
Notes: 
1. Function can return only once and it has just one function means function cannot do more that one task
"""
print("\n")


# Factorial calculation using 2 methods
# First method
def factorial(n):
    """ factorial calculation """
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1
print(factorial(5))
print(factorial(0))

# Second method
def another_factorial(n):
    """ factorial calculation another way """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(another_factorial(4))
print(another_factorial(0))
print("\n")



# Write a python function to print the even numbers from a given list.
def even_number():
    """ create even numbers list from original list """
    number_list = [1, 2, 3, 4, 5]
    even_number_list = []
    for num in number_list:
        if num%2 == 0:
            even_number_list.append(num)

    print(even_number_list)
even_number()
print("\n")


# Python program that takes a number as a parameter and check the number is prime or not.
def prime_number(number):
    """ check prime number or not """
    if number/number == 1 and number/1 == number and number%2 ==1:
        print(f"{number} is prime")
    else:
        print(f"{number} is not a prime")
prime_number(8)
print("\n")



# Python program that takes a list and returns a new list with unique elements of the original list
cities = ["Kathmandu","Kathmandu", "Kyoto", "Birgunj", "Birgunj", "Kyoto"]
unique_cities = []
def unique_items():
    """ Get unique items from list """
    for item in cities:
        if item not in unique_cities:
            unique_cities.append(item)
    return unique_cities

print(unique_items())
print("\n")


# Python program to calculate number of upper and lower case letters in string
def find_uppercase_lowercase():
    """ Prints uppercase and lowercase from given string"""
    string = input("Write something: \n")
    upper_case = []
    lower_case = []
    for char in string:
        if char.isalpha() and char in char.upper():
            upper_case.append(char)
        elif char.isalpha() and char in char.lower():
            lower_case.append(char)
    print(f"Number of upper case letters in:\n\"{string}\" is {len(upper_case)}\n")
    print(f"Number of lower case letters in:\n\"{string}\" is {len(lower_case)}\n")

find_uppercase_lowercase()


# Python program to count and return vowels and consonants in a string
def returns_vowels_and_consonants():
    """ counts and returns vowel and consonants from string """
    string = input("Enter a string to count vowels and consonants: \n")
    vowels = []
    consonants = []
    for char in string:
        if char in "aeiouAEIOU":
            vowels.append(char)
        elif char.isalpha() and char not in "aeiouAEIOU":
            consonants.append(char)
    print(f"Vowels are {vowels} \nConsonants are {consonants}")
    print(f"Number of vowels are {len(vowels)}")
    print(f"Number of consonants are {len(consonants)}")
returns_vowels_and_consonants()
print("\n")


# Python program to reverse a string
def reverse_string_by_words():
    """ Reverse string by words """
    string = input("Enter sentence to Reverse: ")
    print(string.split()[::-1])
reverse_string_by_words()

# String = "This is Yugendra"
# words = String.split()
# print(words[::-1])

def reverse_string():
    """ Reverse given string by characters"""
    string = input("Reverse any string: ")
    print(string[::-1])
reverse_string()


# Python program to find factorial of a given non negativenumber
def factorial(n):
    """ gives factorial of any number(n) """
    result =   1
    for num  in range(1, n+1):
        result *= num
    print(result)

factorial(0)
factorial(5)



# Program to add all the items in a list
def add_list_items(num):
    """ add all items in list """
    result = 0
    for item in num:
        result += item
    return result
added_value = add_list_items([1,2,3])
print(added_value)
print("*-----------------*---------------------*------------------*")


# Program to multiply all the items in a list
def multiply_list_items(*numbers):
    """ multiply all items in list """
    result = 1
    for items in numbers:
        result *= items
    return result

multiplied_value = multiply_list_items(2,3,4)
print((multiplied_value))
print("*-----------------*---------------------*------------------*")
print("\n\n\n\n")


# Python program of simple calculator with two arguments
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by 0"
    else:
        return num1 / num2

print("Select operation: ")
print("1 for Add")
print("2 for Subtract")
print("3 for Multiply")
print("4 for Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print(f"Sum of {num1} and {num2} is", add(num1, num2))

if choice == "2":
    print(f"Result of {num1} - {num2} is", subtract(num1, num2))

if choice == "3":
    print(f"Result of {num1} * {num2} is", multiply(num1, num2))

if choice == "4":
    print(f"Result of {num1} / {num2} is", divide(num1, num2))


# program for To-Do List

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def view_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks yet!")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print("Task removed:", removed_task)
    else:
        print("Invalid task index")

while True:
    print("\nSelect an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        task_name = input("Enter task name: ")
        add_task(task_name)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_index = int(input("Enter task index to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid input")


# Program for Dice Rolling Simulator

import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    result = roll_dice()
    print("You rolled:", result)

    play_again = input("Do you want to roll again? (yes/no): ").lower()
    if play_again != "yes":
        print("Goodbye!")
        break


