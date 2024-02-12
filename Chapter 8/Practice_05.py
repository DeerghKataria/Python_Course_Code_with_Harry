# WAP using functions to find
# ***
# **
# *
# For, n = 3

def pattern_printing(n):
    for i in range(n):
        print("*" * (n-i))
            
num = int(input("Enter Value of 'n': "))
pattern_printing(num)