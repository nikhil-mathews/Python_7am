'''
They are independent of object creation
'''

class Employee:

    @staticmethod
    def greet():
        print("Helllo")

e1=Employee()
e2=Employee()

e1.greet()
e2.greet()

