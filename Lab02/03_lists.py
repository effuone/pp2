# Creating a list in Python
thislist = ["apple", "banana", "cherry"]
print(thislist)  # Output: ['apple', 'banana', 'cherry']

# Lists allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

# Finding the length of a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))  # Output: 3

# Lists can contain different data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list with mixed data types
list1 = ["abc", 34, True, 40, "male"]

# Checking the data type of a list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))  # Output: <class 'list'>

# Using the list() constructor to create a list
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)  # Output: ['apple', 'banana', 'cherry']

# Accessing list items by index
mylist = ['apple', 'banana', 'cherry']
print(mylist[1])  # Output: banana