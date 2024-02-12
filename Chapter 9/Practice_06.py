# This code is for finding whether the word 'python' is present in it or not.

with open("log.txt") as f:
    content = f.read()
    
if 'python' in content.lower():
    print("Yes, python is present")
else:
    print("No, python isn't present")
    
# We're converting the following text to lower case since
# if the compiler has written Python in it. Then, in that case
# we won't be able to tell it. So, you can do two things:
# Option 1:
# content = f.read().lower() ---> This is opening the entire file in lower case.
# Option 2:
# if 'python' in content.lower() ---> Here, the content is converted into lower case.