b = set()
print(type(b))

# Here, you can add elements into the set. More than one occurence, will be ignored.
b.add(4)
b.add(5)
b.add(5)

# b.add([4, 5, 6])
# This will throw an error.
# Since, list is unhashable type. So, the
# contents of the list can be changed later.

# b.add((4, 5, 6))
# But, a tuple can be added.
# Moreover, a dictionary can also not be added.
# Since, the contents inside the dictionary are hashable.

print(b)

# More set methods
print(len(b))   # ---> For printing the length of the set.
b.remove(5)     # ---> For removing elements from the set.

# b.remove(15)  # this will throw an error. Since, '15' is not present.

print(b)

# pop() method will pop a random value from the set.
print(b.pop())
