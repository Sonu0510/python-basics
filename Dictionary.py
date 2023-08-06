car={"make":"Ford", "model":"Mustang", "year": 2012, "engine":"6 litre"}
print(car["make"])
print(car["engine"])
print(len(car)) #to know number of items in dictionary

#Values in dictionaries items can be of any data types
mustangCar = {
    "make":"Ford",
    "model":"GT Mustang",
    "yearMade":2019,
    "engine":"V8",
    "engineType": "Petrol",
    "colors" : ["yellow", "black", "brown", "red", "orange"]
}
print("Number of items(key:value pairs) in mustangCar object is " + " " + str(len(mustangCar)))
print(type(mustangCar)) #To get type of data type
#Accessing items keys and values
print(mustangCar["make"])
print(mustangCar["model"])
print(mustangCar["colors"])#Acessing all colors from the list of colors
print(mustangCar["colors"][0])#Accessing specific colors from the list of colors




