# WAP to create a class programmer for storing information of a 
# few programmer working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f"The name of the prorgammer is {self.name} and the product is {self.product}")
        
deergh = Programmer("Deergh", "Skype")
sam = Programmer("Sam", "GitHub")
jessica = Programmer("Jessica", "Visual Studio Code")

deergh.getInfo()
sam.getInfo()
jessica.getInfo()
