#  Practice Question:
 
# 1: WAP to enter marks of 3 subjects from the user and store them in dictionary. start with any empty dictionary & add one by one. use subject name as key & marks as value.

marks = {}

x = int(input("Enter phy marks:"))
marks.update({"phy": x})

y = int(input("Enter chem marks:"))
marks.update({"chem": x})

z = int(input("Enter math marks:"))
marks.update({"math": x})

print(marks)

# 2: Figure out a way to store 9 & 9.0 as a seperate values in the set

value = {9, 9.0, "9.0", 9.25, 8, 8.0}
print(value)