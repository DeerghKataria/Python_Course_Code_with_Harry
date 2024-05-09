class Employee:
    company = "DeVerse"
    salary = 5600
    salaryBonus = 500

    # For calculating the salary, we will use property decorator.
    # This is also called as 'getter'.
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    # To change it the other way around. Set overall salary that
    # we can calculate the salary bonus.
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary

e = Employee()
# You can return totalSalary and you don't have to call the function. Basically, in the backend
# it will be calculating those parameters. If the property decorator wasn't there, then you
# would have to call the function totalSalary().
print(e.totalSalary)

e.totalSalary = 5800
print(e.salary)
print(e.salaryBonus)