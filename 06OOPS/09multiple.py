# class A:
#     def displayA(self):
#         print("I am class A")

# class B:
#     def displayA(self):
#         print("I am in class b")
# class C(B,A):
#     def display(self):
#         print("I am in child class")

# obj=C()
# obj.display()
# obj.displayA()

class Freelancer:
    company="XYZ"

class Employee:
    company="ABC"

class Programmer(Freelancer,Employee):
    def __init__(self,name):
        self.name=name

e=Programmer("Sam")
print(e.company)