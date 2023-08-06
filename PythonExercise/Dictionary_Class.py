# Ordered, changeable and does not allow duplicates

simple_dict = {"Mango": 2, "Banana": 4}

nested_dict = {"fruits": {"mango": 2, "banana": 4}, "drinks": {"coke": 2, "fanta": 3}, "guava_juice": 6}
print(nested_dict)
print(nested_dict["fruits"]["banana"])
print("\n")

nested_dict["fruits"]["mango"] = 66
print(nested_dict["fruits"]["mango"])
print("\n")
print(nested_dict["drinks"]["coke"])
print("*------------------*----------------------*--------------------*\n")

car = {"ford": 6, "toyota": 4}
print(car)
print(car.get("ford"))
print(car.keys())
print(car.values())
print(car.items())
print("*------------------*-----------------------*--------------------*\n")

capital_city = {
    "Nepal": "Kathmandu",
    "India": "Delhi",
    "China": "Beijing",
    "Japan": "Tokyo",
    "Sri Lanka": "Colombo"
}
print(capital_city)
print(dir(capital_city))  # dir gives list of available methods
capital_city.update({"India": "New Delhi"}) # updating the value of specified keys or can use to add key:value pairs
print(capital_city)
print("*------------------*-----------------------*--------------------*\n")

# Using loop in dictionaries
for country, capital in capital_city.items():
    print(country + ":" + capital)
    print("*------------------*-----------------------*--------------------*\n")
    print(f"country = {country}, capital_city = {capital}")

    # print({key_: value_ for key_, value_ in simple_dict.items()})