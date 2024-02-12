# WAP to find create an identical file of one file
# to another file.

file1 = "copy.txt"
file2 = "this.txt"

with open(file1)as f:
    f1 = f.read()

with open(file2)as f:
    f2 = f.read()
    
if f1 == f2:
    print("Files are identical!!!")
else:
    print("Files do not match!")
    
# Simply store the data of the file in two different variables.
# Then, opent them in write mode and compare them. If they compare
# print that they match otherwise they don't.