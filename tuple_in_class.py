# Tuples are heterogeneous i.e. it can store items of different data types

companies = ("Microsoft", "Google", "Facebook", "Netflix", "Apple")

companies_list = [item for item in enumerate(companies)]
print(companies_list) # Using list comprehension we can convert tuples to list
print("*------------------*---------------------*--------------------*\n")

for index, item in enumerate(companies):
    print(f"Index {index} : {item}")

print("------------------*---------------------*--------------------*\n")

for index, item in enumerate(companies):
    print(index)
    print(item)

print("------------------*---------------------*--------------------*\n")

simple_tuple = ("1", "fruits", True, 234)

print(simple_tuple)
print(type(simple_tuple))
print(len(simple_tuple))

nested_tuple = ("Bus", "Car", ("Aeroplane", "Helicopter"))
print(nested_tuple)
print(type(nested_tuple))
print(len(nested_tuple))

# Converting string to tuple
string_to_tuple = "Good Morning, Good Evening, Good Night"
list_from_str = string_to_tuple.split(",")
print(type(list_from_str))

tuple_from_list = tuple(list_from_str)
print(type(tuple_from_list))

# Accessing tuple items
list_of_clothes = ("pants", "shirts", "shocks", "shoes", "vests", "pants", "shirts", "pants")
print(list_of_clothes[len(list_of_clothes) - 1])  # Last item from tuple
print(list_of_clothes[1])  # second item from tuple

print(list_of_clothes[-len(list_of_clothes)])  # Accessing first item with negative indexing - dynamic coding

print(list_of_clothes[::2])
print(list_of_clothes[1::2])

print(list_of_clothes[2::-1])  # print first 3 items in reverse order

print(list_of_clothes[:-4:-1])  # print last 3 items in reverse order

print(list_of_clothes[::-1])  # printing items of tuples in reverse order

# TWO IMPORTANT METHOD OF TUPLES
print(list_of_clothes.count("pants"))  # Method to count specific item in a tuple
print(list_of_clothes.index("pants"))  # Method to print index number of first item of tuple

print("------------------*---------------------*--------------------*")

# Methods of adding items in tuple
medicines = ("cetamol", "metron")
list_of_medicines = list(medicines)
list_of_medicines.append("syrup")
medicines = tuple(list_of_medicines)
print(medicines)

print("------------------*---------------------*--------------------*")

# Concatenating tuple
first_tuple = [1, 2, 3, 4]
second_tuple = [5, 6, 6]
first_tuple += second_tuple
print(first_tuple)

print("------------------*---------------------*--------------------*")

# UNPACKING TUPLE
a, b, c, *d = first_tuple
print(a)
print(b)
print(c)
print(d)
print("----------------------------------------------\n")

*a, b, c, d = first_tuple
print(a)
print(b)
print(c)
print(d)
print("----------------------------------------------\n")

*a, = first_tuple  # if comma(,) is not given after 'a' result will give error
print(a)
print("----------------------------------------------\n")
