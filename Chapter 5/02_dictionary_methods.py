# Make sure that keys are in lower case. 
# So, you don't have to make sure that you have 
# to enter them as capital letters.

myDict = {
    "Fast": "In a Quick Manner",
    "Deergh": "A Coder",
    "Marks": [1, 2, 5],
    "anotherDict": {'Deergh': 'Player'}
    # Creating a Dictionary another dictionary
}

# Dictionary Methods

print(list(myDict.keys()))
# Converting the elements of dictionary as List.

print(list(myDict.values()))
# Prints the values of the dictionary

print(list(myDict.items()))
# For printing the keys along with their values.