class Employee:
    
    company = "Google"
    
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = 100
        self.subunit = subunit
        print("Employee is created!")
    
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    
    def getSalary(self, signature):
        print(f"Salary for working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")
        
    @staticmethod
    def time():
        print("The time is 10PM at night")
        
deergh = Employee("Deergh", 100, "YouTube")
# deergh = Employee() ---> This will throw an error, since the 3 arguments would be missed.

# We're creating the object but still the constructor would run.

deergh.getDetails()