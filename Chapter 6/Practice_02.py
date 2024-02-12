sub1 = int(input("Enter the Marks of Subject 1: "))
sub2 = int(input("Enter the Marks of Subject 2: "))
sub3 = int(input("Enter the Marks of Subject 3: "))

if(sub1>33 and sub2>33 and sub3>33):
    if((sub1 + sub2 + sub3) > 120):
        print("The Student is PASS!")
    else:
        print("The Student didn't score 40% Marks")
else:
    print("The Student didn't score 33% Marks in each subject")
