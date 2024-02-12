# WAP to wipe out the contents of a file 
# using python.

filename = "badwords.txt"
with open(filename, "w") as f:
    f.write("")
    
# We're basically replacing everything with nothing.