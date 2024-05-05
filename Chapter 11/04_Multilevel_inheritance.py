class Person:
    country = "India"

    def takeBreak(self):
        print("I am breathing!")


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreak(self):
        print("I am an employee. So, I am luckily breathing")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

p = Person()
e = Employee()
pr = Programmer()