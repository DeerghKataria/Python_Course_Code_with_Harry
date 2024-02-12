# This code is for generating the multiplcation table from 2 to 20.
# Then, the data is stored in a file.

for i in range(2, 21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write('\n')

# The last part if for making sure that we don't have any extra spaces 
# left at the end of the code.