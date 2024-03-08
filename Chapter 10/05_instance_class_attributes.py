class Employee:
    company = "Google"
    salary = 100
    
deergh = Employee()
sam = Employee()

# Creating instance attributes salary 
# for both the objects
# deergh.salary = 300
# sam.salary = 400

deergh.salary = 45

# This is overwritting the attributes where the value 300
# will be overwritten by 45.

print(deergh.salary)
print(sam.salary)

# Below line throws an error as address is not present in instance/class
# print(deergh.address)

