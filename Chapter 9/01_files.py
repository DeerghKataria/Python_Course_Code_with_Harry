# Use open function to read the contents of a file!

f = open("D:\\OneDrive - Amity University\\1. Projects\\Programming (Active Projects)\\Python Course - Code with Harry\\Chapter 9\\sample.txt", "r")
# data = f.read()
data = f.read(5)    # ---> reads first 5 characters from the file.
print(data)
f.close()

# In case the file is not read, specify the entire 
# file path for it to work. Moroever, always remember.
# Whenever you're writing the file path. You have to
# to write it within '\\' double backslash. Python 
# Interpreter assumes it to be escape sequence.
 