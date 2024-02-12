myDict = {
    "Livre": "Book",
    "L'Ecole": "School",
    "Bonjour": "Good Morning!"
}

print("Options are ", myDict.keys())
a = input("Enter the French Word:\n")
# print("The Meaning of your word is:", myDict[a])

# Below line will not throw an error if they key is not
# present in the dictionary.
print("The Meaning of your word is:", myDict.get(a))