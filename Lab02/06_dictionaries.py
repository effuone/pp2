# Creating a dictionary with car details
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print the entire dictionary
print(thisdict)

# Accessing a specific item in the dictionary using its key
print(thisdict["brand"])

# Demonstrating that duplicate keys are not allowed in dictionaries
# The second 'year' key will overwrite the first one
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Finding the number of items in the dictionary
print(len(thisdict))

# Dictionary with different data types as values
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Checking the data type of the dictionary
print(type(thisdict))

# Creating a dictionary using the dict() constructor
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)