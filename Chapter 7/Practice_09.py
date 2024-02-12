# WAP to print the following pattern:
#   ***
#   * *
#   ***

# In this case, we have the print the border elements.
# Making it for general case, i.e., n can be a variable.

n = int(input("Enter Number: "))

for i in range(n):
    print("\n", end = "")
    for j in range(n):
        if (i==0 or j == 0 or i==n-1 or j==n-1):
            print("*", end = "")
        else:
            print(" ", end = "")