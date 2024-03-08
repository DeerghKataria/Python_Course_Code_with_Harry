# WAP using functions to remove 
# a given word from a list and
# strip at the same time.

# strip is used to terminate all the unnecessary spaces in between.
# for ex:
# str = "   Deergh   "
# print(str)
# print(this.str())

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()
this = "  Deergh is learning how to be a programmer"
print(remove_and_split(this, "Deergh"))

# Here, we have replaced that particular word with empty space.
# And then we have deleted the spaces using the strip() method.