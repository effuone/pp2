# Example of a simple if statement
a = 33
b = 200
if b > a:
    print("b is greater than a")  # Output: b is greater than a

# Example of an if statement without proper indentation (will cause an error)
a = 33
b = 200
if b > a:
    print("b is greater than a")  # Error: expected an indented block

# Example of using elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")  # Output: a and b are equal

# Example of using else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")  # Output: a is greater than b

# Example of an else without elif
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")  # Output: b is not greater than a

# Short Hand If
if a > b: print("a is greater than b")  # Output: a is greater than b

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")  # Output: B

# One line if else statement with 3 conditions
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")  # Output: =

# Using 'and' logical operator
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")  # Output: Both conditions are True

# Using 'or' logical operator
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")  # Output: At least one of the conditions is True

# Using 'not' logical operator
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")  # Output: a is NOT greater than b

# Nested if statements
x = 41
if x > 10:
    print("Above ten,")  # Output: Above ten,
    if x > 20:
        print("and also above 20!")  # Output: and also above 20!
    else:
        print("but not above 20.")

# Using the pass statement
a = 33
b = 200
if b > a:
    pass  # No output, pass is used to avoid error