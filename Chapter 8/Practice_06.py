# WAP to convert inches to cms using functions.

def height_converter(i):
    c = i * 2.54
    return c

inch = int(input("Height (in inches): "))
print("Height (in cms): " +str(height_converter(inch)))