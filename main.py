class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def ShowDeatils(self):
        print(f"The name of Employee with id {self.id} is {self.name}")

class Programmer(Employee):
    def programLanguage(self):
        print("His default language is Python")


E1 = Employee("Yugendra Ray", 201)
E1.ShowDeatils()

E2 = Programmer("Sam Altman", 101)
E2.ShowDeatils()
E2.programLanguage()