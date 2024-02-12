l1 = [1, 8, 7, 2, 21, 15, 16]
# l1_sorted = l1.sort()
# print(l1_sorted)
# Don't make this mistake, because this is invalid in Python.
# It will return the value as 'None'.

print(l1)   # ---> Before Sorting
l1.sort()
print(l1)   # ---> After Sorting
# Used to reverse the list
l1.reverse()
print(l1)

# It is used to append, i.e. add elements at the end of the list
l1.append(45)
print(l1)

# It will insert 544 at index 2.
l1.insert(2, 544)
print(l1)

# Pop Element at Index 2
l1.pop(2)
print(l1)

# Remove Element 21
l1.remove(21)
print(l1)

# There are so many methods that are associated with lists.
# If you wish to refer more of them.
# Refer python.docs and look at original python documentation.