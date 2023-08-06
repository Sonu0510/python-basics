print("\n")

num = [1, 2]
# num is an object of a list class
print(type(num))

num1 = 4
print(type(num1)) #int

num2 = 4.4
print(type(num2)) #float

c = "Hello"
# c is an object of a string class
print(type(c))

a_tuple = ("Apple", "Banana", "Watermelon")
# a_tuple is an object of tuple class
print(type(a_tuple))
print("\n")


class Schools:
    def location(self):
        print(f"The school is located in Dhapasi")

Skylark = Schools()

Schools.location(Skylark)
Skylark.location() # most commonly used to call methods
print("\n")



# Class and objects
class Students:
    school = "Skylark International"
    def __init__(self, fname, id):
        self.fname = fname
        self.id = id

Samar = Students("Samar Gates", 234)
print(Samar.school)

print(f"{Samar.fname}'s id is {Samar.id}.")
print("\n")

# Create class methods
class Vehicle:
    is_electric = False

    @classmethod
    def display_car_type(cls):
        print(f"Is vecicle electric: {Vehicle.is_electric}")

Vehicle.display_car_type()
print("\n")


class Vehicle:

    def __init__(self, color):
        self.color = color

    def display_car_color(self):
        print(f"The car color is {self.color}")

car1 = Vehicle("Black")
car2 = Vehicle("Silver")

car1.display_car_color()
car2.display_car_color()
print("\n")








class Person:
    def __init__(self, f, l, o): # Dunder method
        self.fname = f
        self.lname = l
        self.occupation = o

    def fullname(self):
        return f"{self.fname} {self.lname}"
"""
-__init__ method is used to assign attribute value to objects
-Here n and o is like a parameter whose value will be passed as arguments while making objects
-self means that object which it was called
"""


a = Person("Julius Robert", "Oppenheimer", "Scientist")
print(a.fullname())
print(f"{a.lname} is a {a.occupation}\n")


b = Person("Elon", "Musk", "Engineer")
print(b.fullname())
print(f"{b.lname} is a {b.occupation}\n")


# EXPLORING SPECIAL METHODS IN PYTHON
class Vehicle:
    def __init__(self, name, color, price, num_tire):
        self.name = name
        self.color = color
        self.price = price
        self.num_tire = num_tire

    def __str__(self):
        return f"{self.color} {self.name} price is = {self.price}"

    def __add__(self, other):
        return self.num_tire + other.num_tire

    def __gt__(self, other):
        if self.price > other.price:
            return f"{self.name} is expensive than {other.name}"
        else:
            return f"{self.name} is cheaper than {other.name}"

    def __call__(self):
        return "printing __call__ magic method"

car = Vehicle("BMW", "Navy Blue", 200000, 4)
bus = Vehicle("Volvo", "Silver", 500000, 12)

print(car)
print(bus)

print(car + bus)
print(car>bus)


# EXPLORING CONCEPTS OF PRIVATE ATTRIBUTES AND METHODS
class Vehicle:
  def __init__(self, color):
    # create private attributes
    self.__vehicle_color = color

# Accessing private attribute and giving new value to private attribute
  def reset_color(self, color="Black"):
    self.__vehicle_color = color
    return f"Car color after changing is {self.__vehicle_color}"

# create object
car = Vehicle('red')
print(car.reset_color("Navy"))