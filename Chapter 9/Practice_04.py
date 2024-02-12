# This code is for finding bad words and then censoring them.

with open("badwords.txt") as f:
    content = f.read()
    
content = content.replace("shit", "$h!t")

with open("badwords.txt", "w") as f:
    f.write(content)
    
# Make sure that you open the file in write mode.
# Otherwise the operation would be invalid.