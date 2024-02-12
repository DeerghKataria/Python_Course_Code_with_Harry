num = int(input("Enter Number: "))

for i in range(1, 11):
    # print(str(num) + "X" + str(i) + "=" + str(i*num))
    # You can also do this using 'fstrings'
    
    print(f"{num}X{i}={num*i}")
    # This is the syntax of 'fstring'