# Creating a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry')

# Tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')

# Getting the length of a tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # Output: 3

# Creating a tuple with one item
thistuple = ("apple",)
print(type(thistuple))  # Output: <class 'tuple'>

# Not a tuple, just a string
thistuple = ("apple")
print(type(thistuple))  # Output: <class 'str'>

# Tuples can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)  # Output: ('abc', 34, True, 40, 'male')

# Checking the data type of a tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))  # Output: <class 'tuple'>

# Using the tuple() constructor to create a tuple
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)  # Output: ('apple', 'banana', 'cherry')