# This is for explaining the significance
# of the word 'self' here.

class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for working in {self.company} is {self.salary}")
        
deergh = Employee()
deergh.salary = 10
deergh.getSalary()

# When you're pointing towards self you're 
# basically doing this ---> Employee.getsalary(deergh)