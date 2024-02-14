# WAP to calculate the sum of n
# natural numbers using recursive functions.

print("Recusrive Sum: 5 = 5 + 4 + 3 + 2 + 1")

def calcSum(n):
    if(n > 0):
        return n + calcSum(n-1)
    else:
        return n
    
num = int(input("Enter Number: "))
sumCalculator = calcSum(num)
print("Sum of " +str(num) + " is " +str(sumCalculator))