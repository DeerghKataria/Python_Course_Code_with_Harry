with open("badwords.txt") as f:
    content = f.read()

words = ["shit", "fuck"]

for word in words:  
    content = content.replace(word, "$&#@")
    with open("badwords.txt", "w") as f:
        f.write(content)
    
# Don't run this code after running Practice_04.
# Because, moreover the issue would be that
# shit would be changed to $h!t and then
# you won't be able to edit that out.