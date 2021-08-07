# class A:
#     def displayA(self):
#         print("I am class A")
# class B(A):
#     def displayB(self):
#         print("I am class B")
# class C(B):
#     def displayC(self):
#         print("I am class C")

# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayC()


class Person:
    '''This is a person class'''
    country="India"
    def breathe(self):
        print("I am breathing....")

class Employee(Person):
    company="XYZ"

    def getSAlary(self):
        print(f"salary is {self.salary}")
    
    def breathe(self):
        print("Employee is breathing")

class Programmer(Employee):
    lang="Python"

    def getSAlary(self):
        print("Yeah got it!!")
    
    def breathe(self):
        print("Barely time to breathe...")

p=Person()
p.breathe()
print(p.__doc__)
# print(p.company)

# e=Employee()
# e.breathe()

pr=Programmer()
pr.breathe()

