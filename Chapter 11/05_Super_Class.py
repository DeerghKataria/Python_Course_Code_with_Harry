class Person:
    country = "India"

    def __init__(self):
        print("Initialising Person...\n")

    def takeBreath(self):
        print("I am breathing!")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super.__init__()
        print("Initialising Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an employee. So, I am luckily breathing")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        # super.__init__()
        print("Initialising Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()    # Running this method of the super class i.e. Employee
        print("I am an employee. So, I am breathing++")

p = Person()
p.takeBreath()
e = Employee()
# If they have their own method, then they will execute it. Otherwise, they will inherit
# from the latest inherited class.
e.takeBreath()
print(e.company)
pr = Programmer()
pr.takeBreath()

# Since, it didn't have his own country. It inherited it's country all the way from Person.
print(pr.country)