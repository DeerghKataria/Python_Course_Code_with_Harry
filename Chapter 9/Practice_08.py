# WAP to find whether a file is identical and matches the content
# of another file.

with open("this.txt") as f:
    content = f.read()
    
with open("copy.txt", "w") as f:
    f.write(content)
    