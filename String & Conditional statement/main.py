# 1: Indexing 
# Character value

str = "Artificial Intelligence is giving the world a new way to think and work"
ch = str[6]
print(ch)
# Ans: i

# 2: Slicing
# Accessing part of string
# str[string_idx : ending:idx] ending  index is not include

str = "Artificial Intelligence is giving the world a new way to think and work"
print(str[1:5])
# Ans: rtif

str = "Artificial Intelligence is giving the world a new way to think and work"
print(str[3:len(str)])
# Ans: ificial Intelligence is giving the world a new way to think and work

# Negative Index

str = "Artificial Intelligence is giving the world a new way to think and work"
print(str[-5: -1])
# Ans: ork
