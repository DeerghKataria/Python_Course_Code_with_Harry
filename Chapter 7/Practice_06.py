# WAP to calcualte the Factorial of a Given Number.

num = int(input("Enter Number: "))
fact = 1

for i in range(1, num+1):
        fact = fact * i

print("The factorial of " +str(num) + " is " +str(fact))