'''
class makes the calling og class method and can access the class attributes
'''

class Employee:
    company="ABC"
    salary=100

    @classmethod
    def changeSalary(cls,sal):
        # this will not change class attribute instead will initiate instance attribute
        # self.salary=sal
        # self.__class__.salary=sal
        cls.salary=sal


e1=Employee()
print(e1.salary)
# e1.changeSalary(500)
Employee.changeSalary(900)

e2=Employee()
print(e2.salary)