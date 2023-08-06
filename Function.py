"""
Should I use the 'return' statement or the 'print' function inside a function?

If you want the function to produce a result that can be used later in your code or to perform further computations, then you should use the return statement.

On the other hand, if you just want to display some information or output during the function's execution for debugging or user interaction purposes, then you should use the print function.
"""


import math
# RETURN STATEMENTS SCENARIOS

# 1. Value calcualtion scenario
def calculate_circle_area(radius):
    return math.pi * radius ** 2

area_of_circle = calculate_circle_area(4)
rounded_area = round(area_of_circle)
print("The area of a circle is ", rounded_area)

# 2. Data processing scenario
def double_elements(numbers):
    doubled = [num * 2 for num in numbers]
    return doubled

print(double_elements([1, 2, 3, 4, 5]))



def i_greet():
    return "Hello"
while True:
    name = input("Enter your name: ")
    result = i_greet() + f" {name}"
    print(result)




# Create function to print Fibonacci sequence up to given number
def fibonacci_sequence(num):
    """Gives fibonacci sequence"""
    a = 0
    b = 1
    for n in range(num):
        if a == 0:
            print(a)
        a, b = b, a + b
        print(a)
    return a


num = int(input("Fibonacci sequence up to: "))
result = fibonacci_sequence(num)

print("*---------------------*----------------------*-------------------------*")


def average_mean(x, y):
    return (x + y) / 2


x = int(input("First number: "))
y = int(input("Second number: "))

print(f"The average mean of {x} and {y} is", average_mean(x, y))

print("*---------------------*----------------------*-------------------------*")


def calc_geometric_mean(a, b):
    return (a * b) / (a + b)


while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    gm_of_a_and_b = calc_geometric_mean(a, b)
    print(gm_of_a_and_b)

    if a == 0:
        break

print("*---------------------*----------------------*-------------------------*")


# With return statement and without parameters
def check_greater():
    """
    """
    num1 = int(input("Number first: "))
    num2 = int(input("Number second: "))

    if num1 > num2:
        return "num1 is greater"
    else:
        return "num2 is greater"


result = check_greater()
print(result)
print("*---------------------*----------------------*-------------------------*")


# without parameters and return statement
# def check_greater_num():
#     a = float(input("Enter one number: "))
#     b = float(input("Enter other number: "))
#
#     if a > b:
#         print(a)
#     else:
#         print(b)
#
# check_greater_num()

# With parameters without return statement
# def check_greater_num(num1, num2):
#     """
#     function prints greater number between two numbers
#     parameters: num1 (int), num2(int)
#     """
#     if num1 > num2:
#         print("num1 is greater")
#     else:
#         print("num2 is greater")
#
#
# check_greater_num(2, 4)
#
# print("\n")


def my_function(name):
    print("Hello" + name)


my_function(" Sonu")
my_function(" Ray")
my_function(" Yugendra")
print("*---------------------*----------------------*-------------------------*")


# Number of parameters and arguments should be equal otherwise it will give you error
# If number of arguments passed is unknown add a * before parameter name (Arbitrary Arguments, *args)
def sur_name_func(*sname):
    print(sname[1] + " " + sname[0])


sur_name_func("Ray", "Yadav", "SAH")
print("*---------------------*----------------------*-------------------------*")


# keyword arguments: we can also use arguments in format key = value syntax. This way order of arguments does not matter
def first_car_priority(car2, car3, car1):
    print(car1)


first_car_priority(car1="Toyota", car3="Ford", car2="BMW")
print("*---------------------*----------------------*-------------------------*")


# Arbitrary kwargs, **kwargs
def nameFunc(**person):
    print("His full name is " + person["fname"] + " " + person["lname"])


nameFunc(fname="Yugendra", lname="Ray")
print("*---------------------*----------------------*-------------------------*")


# Default Parameter value: It is a value that is passed if there is no arguments given at all
def fruits(name="Apple"):  # arbitrary arguments cannot have default value
    print("The fruit you should eat atleast a day is " + name)


fruits("Orange")
fruits()  # When no arguments is given it prints default value which is apple in this case
print("*---------------------*----------------------*-------------------------*")


# Passing List as arguments in Function
def items_in_list(given_list):
    for items in given_list:
        print(items)


fruitNames = ["Apple", "Guava", "Mango"]  # passed fruitNames as arguments in above function
items_in_list(fruitNames)
print("________________________________________________")

vegNames = ["Potato", "Bitter Gourd"]  # passed vegNames as well as arguments in above function
items_in_list(vegNames)
print("*---------------------*----------------------*-------------------------*")


# Return Values in Function
def multiplyFun(x):
    return 5 * x


print(multiplyFun(4))
print("________________________________________________")

print(multiplyFun(8))
print("*---------------------*----------------------*-------------------------*")


# Using return method inside function
def greet_user(name="User"):
    return ("Hello " + name)


message = greet_user("Samar")  # function is passed to object("message") and is called later
print(message)


# Using print method directly inside function
def solve(x, y, z):
    print(int(2 * x / y + z - 6))


solve(8, 4, 6)
print("*---------------------*----------------------*-------------------------*")
