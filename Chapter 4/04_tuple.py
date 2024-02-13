# Creating a Tuple using ()
t = (1, 2, 4, 5)

# Print the Elements of a Tuple
print(t[0])

# Cannot update the value of a tuple
# t[0] = 34 ---> This can't be done, this
# is one of the downside of using tuple.

t1 = ()
print(t1)   # ---> It will print an empty tuple

# Tuple with single element
t2 = (1, )
print(t2)

# t2 = (1)  
# print(t2)
# ---> This is the wrong way of doing it.
# It won't be able to tell
# that a tuple is being declared.

print(t.count(1))   # ---> Tell us the number of occurences
print(t.index(5))   # ---> Tell us about the Index where 5 is located.

# To refer more methods tuple. 
# Check out python.org