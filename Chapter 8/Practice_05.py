# WAP using functions to find
# ***
# **
# *
# For, n = 3

def pattern_printing(n):
    for i in range(n):
        print("*" * (n-i))

# Prefer using this way of doing over calling
# another 'j' loop as it would increase the time
# time complexity for no reason.
            
num = int(input("Enter Value of 'n': "))
pattern_printing(num)