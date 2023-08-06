# To store multiple items in a single variable
# Lists are created with square brackets. Lists are ordered, changeable and allow duplicates
# -- Ordered(Indexed): Items have defined order and will not change
# -- Changeable: can change, add, and remove items in a list
# -- Allow Duplicates: same items is allowed more than once


Fortune500 = ["Facebook", "Amazon", "Apple", "Netflix", "Google", "Microsoft"]
print(Fortune500)
print(Fortune500[1:4])
# --------------------------------------------------------------------------------
CEOofMicrosoft = ["Bill Gates", "Steve Ballmer", "Satya Natdella"]
print(len(CEOofMicrosoft))
# --------------------------------------------------------------------------------
assets = [198.3, 83.4, 72.7, 364.8, 166.5]
print(type(assets))
# --------------------------------------------------------------------------------
# Accessing list items
microsoft = list(("Bill Gates", "Paul Allen", "Microsoft", 1975, "48 years ago", "USA"))  # list function - list()
print(microsoft[-5:-1])
print(microsoft[1:5])

# THIS PROGRAMME IS CREATED BY MYSELF USING TECHNIQUES I HAVE LEARNT TILL NOW
name = input("Enter your name: ")
if name in microsoft:
    print(name + " is in Microsoft")
else:
    print(name + " is soon going to be in Microsoft")
# --------------------------------------------------------------------------------

# Change Item Value
fruits = ["Banana", "Carrot", "Guava"]
# Carrot is changed to Cucumber
fruits[1] = "Cucumber"
print(fruits)

# Change range of item value
vegetables = ["Potato", "Onion", "Tomato", "Asparagus", "Spinach"]
# More items is replaced
vegetables[1:4] = ["Garlic", "Brinjal", "Parbal", "Chicken"]
print(vegetables)

carCompany = ["Mahindra", "Tata", "Suzuki", "Toyota", "Tesla"]
# Here 2 items is replaced with 1 item
carCompany[1:3] = ["Honda"]
print(carCompany)

carCompany.insert(0, "Hyundai")
print(carCompany)

carCompany.append("Kia")
print(carCompany)

otherCarCompany = ["Mercedes", "BMW", "VW"]
# with extend we can add any iterable objects like tuple, sets, dictionaries etc.
carCompany.extend(otherCarCompany)
print(carCompany)

# Remove items from list
carCompany.remove("Mercedes")
print(carCompany)

carCompany.pop(0)
print(carCompany)

carCompany.pop()
print(carCompany)

carCompany.clear()
print(carCompany)
