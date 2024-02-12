# WAP to find the sum of first
# n natural numbers using a while loop.

num = int(input("Enter Number: "))
sum = 0
# You have to initialize the value of sum as 0.
# Otherwise, it will have a type mismatch error or it may have
# an error since the initial value is not fixed.

for i in range(1, num+1):
    sum = sum + i
    
print("The Sum of " + str(num) + " is " + str(sum))
