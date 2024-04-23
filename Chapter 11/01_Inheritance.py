# The basic idea of using Inheritance is so that it doesn't violate
# the DRY principle (Don't Repeat Yourself).

class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

# Making a child class Programmer that is inheriting from Employee
class Programmer(Employee):
    language = "Python"
    # We can override the variable as well
    company = "YouTube"

    def getLanguage(self):
        print(f"The language is {self.language}")
    # Declaring showDetails here would override the one from the base class.
    def showDetails(self):
        print("This is a progammer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()     # Even in this case, we're going to get the same output since the class in inherited

# Similarly, in this case as well. It is going to inherit from the parent class
print(p.company)        # It is going to return Google which is the company of Employee Class