'''
DRY-> Do not repeat yourself
Single inheritance
multiple inheritance
multilevel inheritance

'''

# class A:
#     def displayA(self):
#         print("I am class A")

# class B(A):
#     def displayB(self):
#         print("I am in class b")

# obj=B()
# obj1=A()
# obj.displayB()
# obj.displayA()

# obj1.displayA()

class Employee:
    company="ABC"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language="Python"

    def code(self):
        print("I am writing code")
    
    def showDetails(self):
        print("I am a programmer")

e=Programmer()
e.showDetails()