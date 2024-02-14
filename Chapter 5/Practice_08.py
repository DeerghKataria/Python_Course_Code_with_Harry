# If the names of 2 friends are the same;
# what will happen to the program in Program 6?

# To check the same

# Here, we created an empty dictionary.
favLang = {}

# Taking Input 
a = input("Enter your Favourite Langauge Friend1:")
b = input("Enter your Favourite Langauge Friend2:")
c = input("Enter your Favourite Langauge Friend3:")
d = input("Enter your Favourite Langauge Friend4:")

# Taking Values for the corresponding names
favLang['Friend1'] = a
favLang['Friend2'] = b
favLang['Friend3'] = c
favLang['Friend3'] = d

print(favLang)

# In this case, we can see in output that the value
# of 'd' is overwritting 'c'. 