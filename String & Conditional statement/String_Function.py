# str.endswith

str = "Hello, welcome to my world."
print(str.endswith('world.')) # return trus if string end with substr
# Output: True

print(str.endswith('Welcome'))
# Output: False

# <----------------->

# str.capitalize   

str = "hello, welcome to my world."
print(str.capitalize()) # capitalize 1st later
# Output: Hello, welcome to my world.

# <----------------->

# str.replace(old, new)

str = "Hello, welcome to my world."
print(str.replace("o" , "a")) # replace all occurrance of old with new
# Output: Hella, welcame ta my warld.

# <----------------->

str = "Hello, welcome to my world."
print(str.replace("Hello" , "hyi")) # replace old with new
#  Output: hyi, welcome to my world.

# <----------------->

# str.find

str = "Hello, welcome to my world."
print(str.find("welcome")) # return 1st index of 1st occurror
# Output: 7

# <----------------->

# str.count

str = "Hello, welcome to my world."
print(str.count("o")) # count the occurrance of substr
# Output: 4