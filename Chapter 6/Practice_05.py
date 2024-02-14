# WAP to find out whether a given name is present
# in a list or not.

names = ["Jessica", "Nilson", "Smith", "Taylor", "Madison"]

name = input("Enter Name: ")

if(name in names):
    print("Your name is in the list!")
else:
    print("Your name isn't the list!!!")