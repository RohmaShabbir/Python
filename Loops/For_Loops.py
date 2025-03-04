# Loops are used to repeat instructions

# For Loops

# Loops are used for sequential traversal. For traversing list[], string, tuples() etc

tuple = (1, 2, 3, 4, 5)
for x in tuple:
    print(x)

# list = input("Enter a list of any thing: ").split()
for i in list:
    print(i)
else:
    print("Done")

# Range()
# Range function returns a sequence of number, starting from 0 by deafault, and increments by 1 (by deafault), and stop before a specified number.
# range(start?, stop, step?)

for el in range(10): # range(stop)
    print(el)

for el in range(2, 10): # range(start, stop)
    print(el)

for el in range(2, 10, 2): # range(start, stop, step)
    print(el)

# <--------2nd method-------->
seq = range(5)

for i in seq:
    print(i)

# Range() Practice Question:

# Print numbers from 1 to 100
for i in range(1, 101):
    print(i)

# Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)

# Print the multiplication table of a numer n
n = int(input("Enter Number: "))

for i in range(1, 11):
    print(n * i)

# Pass Statement
# Pass is a null statement that does nothing. it is used as a placeholder for future code.
for i in range(10):
    pass

# <----------------------------------->

# Practice Question

# 1: Print the element of the followinglist using a loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in list:
    print(el)

# 2: Search a number x in this tuple using loop
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx:", idx)
        break
    idx += 1 

#  WAP to find the sum of first natural numbers. (while)
n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum = ",sum)
# <--------->
n = 5
sum = 0
for i in range(1, n+1):
    sum += i

print("total sum = ",sum)

# 3: to find the factorial of first n numbers.  (For)
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("total factorial = ",fact)


