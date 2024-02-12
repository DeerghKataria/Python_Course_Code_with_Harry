# WAP using functions to find the greatest of 3 integers

def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))

m = maximum(n1, n2, n3)
print("\nThe value of the maximum is " + str(m)) 