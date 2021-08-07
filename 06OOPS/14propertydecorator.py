class Employee:
    company="ABC"
    salary=5600
    salaryBonus=400

    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

    # setter
    @totalSalary.setter
    def totalSalary(self,new_sal):
        self.salaryBonus=new_sal-self.salary

e1=Employee()
print(e1.totalSalary)

e1.totalSalary=7000
# print(e1.totalSalary())
print(e1.salaryBonus)