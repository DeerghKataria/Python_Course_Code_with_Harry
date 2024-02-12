# WAP using functions to print the multiplication 
# table of a given number.

def mult_table(n):
    for i in range(11):
        print(f"{n}X{i}={n*i}")

num = int(input("Enter the Number: "))
mult_table(num)