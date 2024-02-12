# WAP to calculate the grade of a student

marks = int(input("Enter the Marks: "))

if(marks>=90):
    Grade =  "A"
elif(marks>=80):
    Grade =  "B"
elif(marks>=70):
    Grade =  "C"
elif(marks>=60):
    Grade =  "D"
elif(marks>=50):
    Grade =  "E"
else:
    Grade =  "F"
    
print("Your Grade: " + Grade)