# Example: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Example: Looping through a string
for x in "banana":
    print(x)

# Example: Using break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Example: Using break before print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# Example: Using continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Example: Using range() function
for x in range(6):
    print(x)

# Example: Using range() with start parameter
for x in range(2, 6):
    print(x)

# Example: Using range() with increment
for x in range(2, 30, 3):
    print(x)

# Example: Else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Example: Else block with break
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

# Example: Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# Example: Using pass statement
for x in [0, 1, 2]:
    pass