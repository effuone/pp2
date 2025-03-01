# Arithmetic Operators
x = 10
y = 5

# Addition
print(x + y)  # Output: 15

# Subtraction
print(x - y)  # Output: 5

# Multiplication
print(x * y)  # Output: 50

# Division
print(x / y)  # Output: 2.0

# Modulus
print(x % y)  # Output: 0

# Exponentiation
print(x ** y)  # Output: 100000

# Floor division
print(x // y)  # Output: 2

# Assignment Operators
x = 5

x += 3  # Same as x = x + 3
print(x)  # Output: 8

x -= 3  # Same as x = x - 3
print(x)  # Output: 5

x *= 3  # Same as x = x * 3
print(x)  # Output: 15

x /= 3  # Same as x = x / 3
print(x)  # Output: 5.0

x %= 3  # Same as x = x % 3
print(x)  # Output: 2.0

x //= 3  # Same as x = x // 3
print(x)  # Output: 0.0

x **= 3  # Same as x = x ** 3
print(x)  # Output: 0.0

# Comparison Operators
x = 5
y = 3

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: True
print(x < y)   # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False

# Logical Operators
x = 5

print(x < 5 and x < 10)  # Output: False
print(x < 5 or x < 10)   # Output: True
print(not(x < 5 and x < 10))  # Output: True

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # Output: True
print(x is y)  # Output: False
print(x == y)  # Output: True

# Membership Operators
x = ["apple", "banana"]

print("banana" in x)  # Output: True
print("pineapple" not in x)  # Output: True

# Bitwise Operators
x = 6  # 110 in binary
y = 3  # 011 in binary

print(x & y)  # Output: 2 (010 in binary)
print(x | y)  # Output: 7 (111 in binary)
print(x ^ y)  # Output: 5 (101 in binary)
print(~x)     # Output: -7 (inverts all bits)
print(x << 2) # Output: 24 (11000 in binary)
print(x >> 2) # Output: 1 (1 in binary)

# Operator Precedence
print((6 + 3) - (6 + 3))  # Output: 0
print(100 + 5 * 3)        # Output: 115

# Same precedence, evaluated left to right
print(5 + 4 - 7 + 3)  # Output: 5