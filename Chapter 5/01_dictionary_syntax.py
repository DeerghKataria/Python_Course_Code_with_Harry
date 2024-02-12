# In a dictionary we have a key and for that
# key we have a correponding value.

myDict = {
    "Fast": "In a Quick Manner",
    "Deergh": "A Coder",
    "Marks": [1, 2, 5],
    "anotherDict": {'Deergh': 'Player'}
    # Creating a Dictionary another dictionary
}

print(myDict['Fast'])
print(myDict['Deergh'])
myDict['Marks'] = [45, 78]      # ---> This will override the pre-existing numbers
print(myDict['Marks'])
print(myDict['anotherDict']['Deergh'])
# Searching a word within a word.
print(myDict['anotherDict'])