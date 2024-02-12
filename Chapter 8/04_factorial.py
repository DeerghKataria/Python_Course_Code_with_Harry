# n! = 1 * 2 * 3 * 4 * .... * n

# n = int(input("Enter Number: "))
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)


# Now, finding factorial using Recursive Function.
# Using the concept that we already know:
# n! = n * (n-1)!

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
def factorial_recursive(n):
    if n == 1 or n == 0:    # For finding factorial of 0 or 1.
        return 1
    return n * factorial_recursive(n-1)
    
f = factorial_iter(5)
print(f)
    
# When you're using recursive functions, you need to make
# sure that you're extra careful. In case of iterative
# functions, it doesn't really matter that much.