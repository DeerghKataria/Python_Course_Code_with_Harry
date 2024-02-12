# WAP to calculate the sum of n
# natural numbers using recursive functions.

def calcSum(n):
    if(n > 0):
        return n + calcSum(n-1)
    else:
        return n
    
num = int(input("Enter Number: "))
sumCalculator = calcSum(num)
print("Sum of " +str(num) + " is " +str(sumCalculator))