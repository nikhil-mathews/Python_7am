class A:
    def displayA(self):
        print("I am class A")

class B:
    def displayA(self):
        print("I am in class b")
class C(B,A):
    def display(self):
        print("I am in child class")

obj=C()
obj.display()
obj.displayA()