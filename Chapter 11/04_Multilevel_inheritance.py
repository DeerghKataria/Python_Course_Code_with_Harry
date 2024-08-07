class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing!")


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an employee. So, I am luckily breathing")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

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