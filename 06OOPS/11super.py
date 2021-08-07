class Person:
    '''This is a person class'''
    country="India"

    def __init__(self):
        print("Initialising Person")

    def breathe(self):
        print("I am breathing....")

class Employee(Person):
    company="XYZ"

    def __init__(self):
        super().__init__()
        print("Initialising Employee")

    def getSAlary(self):
        print(f"salary is {self.salary}")
    
    def breathe(self):
        super().breathe()
        print("Employee is breathing")

class Programmer(Employee):
    lang="Python"

    def __init__(self):
        super().__init__()
        print("Initialising Programmer")

    def getSAlary(self):
        print("Yeah got it!!")
    
    def breathe(self):
        super().breathe()
        print("Barely time to breathe...")

pr=Programmer()
pr.breathe()