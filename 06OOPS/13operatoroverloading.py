class Number:
    def __init__(self,num):
        self.num=num
    
    def __add__(self,num2):
        return self.num+num2.num
    def __mul__(self,num2):
        return f"this is multiplication"
    
    def __str__(self):
        return f"This is an object of class Number"

n1=Number(3)
n2=Number(6)

# print(n1 + n2)
# n1.__add__(n2)

# print(n1*n2)

print(n1)

# __add__