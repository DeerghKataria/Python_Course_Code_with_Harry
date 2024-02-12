# WAP to rename a file.
# File Format: "renamed_by_python.txt"

import os

oldname = "sample.txt"
newname = "renamed_by_python.txt"

with open(oldname) as f:
    content = f.read()
    
with open(newname, "w") as f:
    f.write(content)

# The concept here is the same. Just open the 
# file in write mode and change the name by opening
# it another name.

os.remove(oldname) # ---> By using this command. It will delete the file.
