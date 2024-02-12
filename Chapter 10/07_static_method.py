class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")
        
    @staticmethod
    def time():
        print("The time is 10PM at night")
       
deergh = Employee()
deergh.salary = 100000
deergh.getSalary("Thanks!")

# When you're pointing towards self you're 
# basically doing this ---> Employee.getsalary(deergh)

deergh.greet()
# If you wish to run it in the way Employee.greet()
# You can do that using static method.
# It will realise that you are not willing to change 
# Employee.getSalary() into Employee.getSalary(deergh)

# Also, you can also send any other parameter other than self.


deergh.time()