class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name: {self.name}")
        print(f"Train: {self.train}.")

DeerghApplication = RailwayForm()
DeerghApplication.name = "Deergh"
DeerghApplication.train = "Rajdhani Express"
DeerghApplication.printData()