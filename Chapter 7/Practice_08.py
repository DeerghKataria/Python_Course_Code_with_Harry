# WAP to print the following pattern:
#   *
#  ***
# *****
# for n = 3

n = int(input("Enter Number: "))

for i in range(3):
    for j in range(n-i-1):
        print(" " * (n-i-1), end = "")
        print("*" * (2*i+1), end = "")
        print(" " * (n-i-1)) 
        
# We use the end statement to make sure that there 
# are no lines being left out and you can just leave
# it empty.