greeting = "Good Morning, "
name = "Deergh"
print(type(name))
# ---> This will be of type string

# Now concatenating both of these strings
c = greeting + name
print(c)

print("Print the first character ---> ", name[0])
# This will give us the index of the array. Because the 
# string is stored in the form of array.

print("Print from the ", name[0:3])
# Now, this will give the indeces 0,1 and 2.
# This is called as string slicing.

# print(name[:4]) ---> This will give take it as 0:4
# print(name[1:]) ---> This is equivalent to 1:5
# To simply print till the last element just leave the second
# index empty. Like print(name[0:])

# You can also use negative indices
print("Print from 4th last to the 2nd last index --->",name[-4:-1])
# This is same as 1:4, we just use negative indeces
# when we are not aware of the end length of a particular
# string type.


d = name[1:4:1] # Here no such value will be skipped, since skip value is '1'. So, nothing will be skipped.
print(d)

d = name[1:4:2] # Here the skip value is of '2', so 1 space will be skipped
print(d)

