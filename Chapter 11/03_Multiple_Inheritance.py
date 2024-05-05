class Employee:
    company = "Visa"
    eCode = 123

class Freelancer:
    company = "Fiverr"
    level = 2

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Deergh"

p = Programmer()
p.upgradeLevel()
print(p.level)

# Here, Employee's company would be printed since while inherting we've
# written Employee first in the brackets. So, even if we define Freelancer
# first. Still it would remain the same.

print(p.company)