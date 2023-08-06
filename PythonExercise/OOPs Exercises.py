
print("\n")
# create class attributes to initialize pi=3.14
class PI:
    pi = 3.14

print(f"PI.pi", "\n")

# create __init__() method to initialize radius of circle for each instance
class Circle(PI):

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        print(2 * 3.14 * self.radius)

    def set_radius(self, new_radius):
        self.radius = new_radius

c1 = Circle(5)
c2 = Circle(8)

print(f"Original radius of c1 circle is {c1.radius}")
c1.set_radius(88)
print(f"New radius of c1 circle is set using set_radius method which is {c1.radius}")

print(f"Original radius of c2 circle is {c2.radius}", "\n")

c1.get_circumference()
c2.get_circumference()



