introduction = "hello, my name is Deergh Kataria. \
And I love coding and making YouTube Videos."

# String Functions
print("String length: ", len(introduction))
# This is used for calculating String Length

print(introduction.endswith("Videos."))
# If it ends with the what's written in the "".
# Then, it will return True value.

print("Number of times 'a' occured: ", introduction.count("a"))
# Counts the No of Occurences of "a"
# It can also be used to count words.

print(introduction.capitalize())
# The first character will be capitalized

print("Index where 'Deergh' is located: ",introduction.find("Deergh"))
# It will return the index.

print(introduction.replace("coding","programming"))