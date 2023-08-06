class Father:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def details(self):
        print(f"Name is: {self.name} and address is {self.address}")


class Son(Father):
    #Can use pass method if don't want to make any methods and attributes
    def qualifaction(self):
        print("Qualification is Bachelor's Degree")


Fdetails = Father ("Suresh Ray", "Belhi")
Fdetails.details()

Sdetails = Son("Yugendra Ray", "Belhi")
Sdetails.details()
Sdetails.qualifaction()