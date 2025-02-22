# Set is the collection of the onordered items.
# Each elements in the set must be unique & immutable.

collection = {1, 2, 3, 4, "Hello", "World"}
print(collection)
# Output: {1, 2, 3, 4, "Hello", "World"}
print(type(collection))
# Output: <class 'set'>
print(len(collection))
# Output: 6

# repeated element stored only once, so it resolve to {1, 2}
collection2 = {1, 2, 2, 2, 3, "Hello", "World", "World" }
print(collection2)
# Output: {1, 2, 3, 'World', 'Hello'}
print(len(collection2))
# Output: 5  


# empty set synatx
collection3 = {} # empty dictionary
print(type(collection3))
# Output: <class 'dict'>

null_set = set()
print(type(null_set))
# Output: <class 'set'>

# <------------------------------------>

# Set Methods 
set = {1, 2, 3 , "Hello"}

# set .add(el) adds an element
set.add("World")
print(set)
# Output: {1, 2, 3, 'World', 'Hello'}

# set.remove(el) removes the element an
set.remove(3)
print(set) 
# Output: {1, 2, 'World', 'Hello'}

# set.clear(el) emptiesthe set
set.clear()
print(set)
# Output: set()

# set.pop(el) removes a random element
print(set.pop())
# Output: 1

# <------------>

# set.union(set2) combine both set values & return news
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
# Output: {1, 2, 3, 4, 5}

# set.intersection(set2) combines common values & return news
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))
# Output: {3}