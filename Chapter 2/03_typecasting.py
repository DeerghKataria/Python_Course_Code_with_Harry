# Type Casting: When you try to convert one datatype to the other.

a = '3534'
a = int(a)
print(type(a))
print(a +5)

# Even though 3534 was initially a string, but we converted it into integer.
# Then, we can perform, integer operation on it, which was not possible earlier.
# More importantly you cannot covnert everything to int. What if it's 'Deergh'. Then,
# in that particular case you won't just be able to do that. It should be possible in the
# first place. For example,

# a = 'Deergh'
# a = int(a)
# print(type(a))

# The compiler will throw an error.


