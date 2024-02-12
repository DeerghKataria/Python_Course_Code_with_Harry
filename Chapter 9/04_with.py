with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write('me')
print(a)

# In case of 'with' statement. You don't need to close
# 