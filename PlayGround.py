print("\n")



# EXCEPTION HANDLING

a = int(input("Enter number_1: "))
b = int(input("Enter number_2: "))

try:
  print("Resource open")
  print(a/b)
  c = int(input("Enter a number again: "))
  print(c)

except ZeroDivisionError as e:
  print("Hi, You cannot divide a number by zero,", e)

except ValueError as e:
  print("Invalid input", e)

except Exception as e:
  print("Something went wrong>>>>>>>>")

finally:
  print("Resource closed")

print("\n")










# Exploring inner classes TELUSKO
class Student:
  def __init__(self, name, rollno):
    self.name = name
    self.rollno = rollno
    self.laptop = self.Laptop()
    # Inner Laptop class is accessed from here

  def show_details(self):
    print(self.name, self.rollno)
    self.laptop.laptop_details()


  class Laptop:
    def __init__(self):
      self.brand = "HP"
      self.cpu = "i5"
      self.ram = 8

    def laptop_details(self):
      print(self.brand, self.cpu, self.ram)


s1 = Student("Yugen", 1)
s2 = Student("Sonu", 2)

s1.show_details()
s2.show_details()

print("\n")



# Exploring concepts of private attributes and methods
class Vehicle:
  def __init__(self, color):
    self.__vehicle_color = color

  def reset_color(self, color="Black"):
    self.__vehicle_color = color
    return f"Car color after changing is {self.__vehicle_color}"

car = Vehicle('red')
print(car.reset_color("Navy"))


# Simple OOPs concepts
import math
class Circle:
  pi = math.pi
  def __init__(self, radius):
    self.radius = radius

  def get_circumference(self):
    return 2 * Circle.pi * self.radius

  def set_radius(self, new_value):
    self.radius = new_value
    return self.radius


circle1 = Circle(5)
cir_circum = circle1.get_circumference()
print("The circumference of a circle is", cir_circum)
print("\n")

new_radius = circle1.set_radius(2)
print(f"The new radius of a circle is {new_radius}")
print("\n")


# Create one private method and access it with help of method
class Bottle:
  def __init__(self, size):
    self.__bottle_size = size

  def bottle_size(self):
    return f"Bottle size is {self.__bottle_size}"

First_Bottle = Bottle("18cm")
first_size = First_Bottle.bottle_size()
print(first_size)
print("\n")


# Create private methods and access it with other methods
class Furniture:
  def __init__(self, move):
    self.move = move

  def __check_move(self):
    return f"This black chair {self.move}"

  def return_check_move(self):
    return self.__check_move()


Black_Chair = Furniture("does not moves.")
print(Black_Chair.return_check_move())
print("\n")


