#  A built-in data type that lets us create 'immutable' sequences of value.

tup = (1, 2, 3, 4, 5)
print(tup)
# Output: (1, 2, 3, 4, 5)
print(type(tup))
# Output: <class 'tuple'>
print(tup[2])
# Output: 3

# <------------------------------------>

# Tuple Methods

tup = (2, 4, 5, 4, 8)

# tup.index(el) returns index of first occurance
print(tup.index(5))
# Output: 2

# tup.count(el) count total occurance
print(tup.count(4))
# Output: 2


