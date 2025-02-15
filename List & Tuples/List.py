# A built-in data type that store set of value
# It can store element of different type (int, float, string, etc)

marks = [99.5, 86.5, 78.5, 65.5, 45.5]

print(marks) 
# Output: [99.5, 86.5, 78.5, 65.5, 45.5]
print(type(marks)) 
# Output: <class 'list'>
print(len(marks)) 
# Output: 5
print(marks[0]) 
# Output: 99.5
print(marks[2]) 
# Output: 78.5

# <------------------------------------>

# List Slicing
# Similar to string slicing

marks = [99.5, 86.5, 78.5, 65.5, 45.5]

print(marks[1 : 4])
# Output: [86.5, 78.5, 65.5]
print(marks[1 :], len(marks)) 
# Output: [86.5, 78.5, 65.5, 45.5] 5
print(marks[-3 : -1]) 
# Output: [78.5, 65.5]


# <------------------------------------>

# List Methods

list = [2, 6, 8, 4, 7]

# 1: list.append()  adds one element at the end
list.append(9)
print(list) 
# Output: [2, 6, 8, 4, 7, 9]

# 2: list.sort()  sort is ascending order
list.sort()
print(list)
# Output: [2, 4, 6, 7, 8]

# 3: list.sort(reverse = True)   sort in descending order
list.sort(reverse = True)
print(list)
# Output: [8, 7, 6, 4, 2]

# 4:list.reverse()  reverse the list
list.reverse()
print(list)
# Output: [7, 4, 8, 6, 2]

# 5: list.insert(idx, el) insert element at index
list.insert(2, 5)
print(list)
# Output: [2, 6, 5, 8, 4, 7]

#  6: list.remove() remove element from list
list.remove(8)
print(list)
# Output: [2, 6, 4, 7]

# 7: list.pop() remove last element from list
list.pop(2)
print(list)
# Output: [2, 6, 4, 7]


