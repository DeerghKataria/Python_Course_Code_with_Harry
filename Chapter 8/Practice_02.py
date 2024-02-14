# WAP using functions to convert Calsius to Fahrenheit.

def farh(cel):
    return (cel*(9/5))+32

c = int(input("Enter Temperature in Celsius: "))
f = farh(c)

print("The Temperature in Farhenheit: " +str(f))

# Try with -40. Since, it would return -40.0 which is
# the same value.