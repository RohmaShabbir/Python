"""
1: Conditional Statements 
if-elif-else (SYNTAX)

if condition:
    statement 1
elif condition:
    statement 2
else:
    statement 3
"""

light = "red"

if (light == "green"):
    print("Go")
elif (light == "red"):
    print("Stop")
elif (light == "yellow"):
    print("look for the signal")
else:
    print("Invalid Signal")

print("End of the Program")

#  <------------------------->

"""
2: Grade Student Based on marks

Marks >= 90, Grade = "A"
90 > Marks >= 80, Grade = "B"
80 > Marks >= 70, Grade = "C"
70 > Marks, Grade = "D" 
"""

Marks = int(input("Enter the Marks:"))

if (Marks >= 90):
    grade = "A"
elif (Marks >= 80 and Marks < 90):
    grade = "B"
elif (Marks >= 70 and Marks < 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the Student is:", grade)




