# Loops are used to repeat instructions

# While Loop

count = 1   # Iterators
while count<= 8:  # Iteration
    print("Hello", count)
    count += 1
print(count)

# Print number 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

print()

x = 5
while x >= 1:
    print(x)
    x -= 1

#  Break & Continue

# Break: used to terminate the loop when encountered.

i = 1
while i<=5:
    print(i)
    if(i == 3):
        break
    i += 1
    
# Continue: terminate execution in the current interation & continues execution of the loop with the next iteration.

i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1

# <------------------------------------>

# Practice Questions

# 1: Print numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i += 1

# 2: Print numbers from 100 to 1
x = 100
while x >= 1:
    print(x)
    x -= 1

# 3: Print the multiplication table of a number n.
n = int(input("enter number: "))
x = 1
while x <= 10:
    print(n * x)
    x += 1

# 4:Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0
while i < len(num):
    print(num[i])
    i += 1

hero = ["superman", "batman", "wonder woman", "flash", "aquaman", "cyborg", "green lantern"]
x = 0
while x < len(hero):
    print(hero[x])
    x += 1

# 5: Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

num = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

x = 100

i = 0
while i < len(num):
    if(num[i] == x):
        print("Found at index:", i)
        break
    i += 1
else:
    print("Not Found")
