class Employee:
    company = "Google"
    salary = 100

deergh = Employee()
sam = Employee()
deergh.salary = 300
sam.salary = 400

print(deergh.company)
print(sam.company)

Employee.company = "YouTube"

print(deergh.company)
print(sam.company)