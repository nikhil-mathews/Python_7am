class Employee:
    company="ABC"

    def __init__(self,n,a):
        # print("Init is called")
        self.name=n
        self.age=a

    def profile(self):
        print(f"{self.name} has age {self.age} works in {self.company}")
        

sam=Employee("sam",21)
sam.profile()

john=Employee("john",23)
john.profile()