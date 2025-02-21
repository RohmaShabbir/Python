#  Dictionaries are used to store data value in key:value pairs.
# They are unordered, mutable(changeable) & don't allow duplicate keys.

info = {
    "Key": "value",
    "Name": "John",
    "Age": 20,
    "City": "New York"
}
print(info)
# Output: {'Key': 'value', 'Name': 'John', 'Age': 20, 'City': 'New York'}
print(type(info))
# Output: <class 'dict'>

# <--------------------------------->

# Nested Dictionary

info = {
    "Name": "John",
    "Age": 20,
    "City": "New York",
    "Education": {
        "School": "ABC",
        "College": "XYZ"
    }
}

print(info)
# Output: {'Name': 'John', 'Age': 20, 'City': 'New York', 'Education': {'School': 'ABC', 'College': 'XYZ'}}
print(info["Education"]["School"])
# Output: ABC

# <--------------------------------->

#  Dictionary Methods

student = {
    "Name": "John",
    "Age": 20,
    "Subjects": {
        "Phy": 95,
        "Chem": 84.5,
    }
}

# 1: myDict.keys()  returns all keys
print(student.keys())
# Output: dict_keys(['Name', 'Age', 'Subjects'])

# 2: myDict.values()  returns all values
print(student.values())
# Output: dict_values(['John', 20, {'Phy': 95, 'Chem': 84.5}])

# 3: myDict.items()  returns all key-value pairs as tuples
print(student.items())
# Output: dict_items([('Name', 'John'), ('Age', 20), ('Subjects', {'Phy': 95, 'Chem': 84.5})])

pairs = list(student.items())
print(pairs[0])
# Output: ('Name', 'John')

# 4: myDict.get("key")  returns the key according to value
print(student.get("Age"))
# Output: 20

# 5: myDict.update({"key": "value"})  updates the dictionary
student.update({"City": "New York"})
print(student)
# Output: {'Name': 'John', 'Age': 20, 'Subjects': {'Phy': 95, 'Chem': 84.5}, 'City': 'New York'}








