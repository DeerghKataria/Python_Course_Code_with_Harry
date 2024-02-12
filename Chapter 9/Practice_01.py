f = open('text.txt')

text_file = f.read()
# Storing the file 

if 'Deergh' in text_file:
    print("Your Name is Present!")
else:
    print("Your Name isn't Present!")
f.close()