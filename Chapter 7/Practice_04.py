# WAP to check whether a given number is prime or not.

# Using While Loop

# num = int(input("Enter Number: "))

# is_Prime = True
# # is_Prime is used as a Flag to check whether the number holds true a particular criteria
# # even till the end. For some reason, if it doesn't. We can still verify.

# count = 2
# # It is for the intial value for the divisibility check.

# while count<(num/2):
#     rem = num % 2
#     if rem != 0:
#         count  = count + 1
#     else:
#         is_Prime = False
#         break
#         # We're using the break statement, since we want it to exit the loop
#         # once it is divisible by a paritcular number.

# if is_Prime:   
#     print("The Entered Number is a Prime Number")
# else:
#     print("The Number is not Prime")
    
    
# Alternative Method Using for Loop:

num = int(input("Enter Number: "))
isPrime = True

for i in range(2, num):
    if num%i==0:
        isPrime = False
        break

if isPrime:
    print("The Entered Number is a Prime Number")
else:
    print("The Entered Number is not a Prime Number")