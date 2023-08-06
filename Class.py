#Simple case of creating object
class MyClass(): #creating class
    x = 5 #this is called class attribute
Object1 = MyClass() #creating object from class
Object2 = MyClass() #creating object from class
print(Object2.x)
print(Object1.x)

Object2.x = 10
print(Object2.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Person1 = Person("Yugendra Ray", 23)
print(f"My name is {Person1.name}")

class Car:
    def __init__(self, make, mode):
        self.make = make
        self.mode = mode
S = Car("Tesla", "Automatic")
print(S.make)
print(S.mode)


class School:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def estdFunc(self):
        print(self.name + " was established in")

school1 = School("Skylark International School", 1998)
school1.estdFunc()


#String representation of an object without __str()__ function
class P:
    def __init__(self, name, value):
        self.name = name
        self.value = value

newPerson = P("Sam Altman", "2 Billions")
print(newPerson)


#String representation of an object with __str()__ function
class Per:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} has {self.value} in worth."


p2 = Per("Elon Musk", "200 Billion Dollars")
p2.value = "300 Billion Dollars"
print(p2)