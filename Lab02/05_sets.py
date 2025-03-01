# Creating a set in Python
thisset = {"apple", "banana", "cherry"}
print(thisset)  # Output may vary as sets are unordered

# Demonstrating that duplicate values are ignored in sets
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # 'apple' appears only once

# Showing that True and 1 are considered the same in sets
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)  # True and 1 are treated as duplicates

# Showing that False and 0 are considered the same in sets
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)  # False and 0 are treated as duplicates

# Getting the length of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))  # Outputs: 3

# Sets can contain different data types
set1 = {"abc", 34, True, 40, "male"}
print(set1)  # Output may vary as sets are unordered

# Checking the data type of a set
myset = {"apple", "banana", "cherry"}
print(type(myset))  # Outputs: <class 'set'>

# Creating a set using the set() constructor
thisset = set(("apple", "banana", "cherry"))  # Note the double round-brackets
print(thisset)  # Output may vary as sets are unordered