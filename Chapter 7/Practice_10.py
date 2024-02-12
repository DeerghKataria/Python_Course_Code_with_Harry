# WAP to print the multiplication table of n 
# using for loop in reversed order.

num = int(input("Enter Number: "))

for i in range (10, 1, -1):
    print(f"{num}X{i}={num*i}")
    
    
# The syntax for range function is as follows:
# (start, stop, step)

# And we solved it using fstrings.
# You can also do it using regular method.

