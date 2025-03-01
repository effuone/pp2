# Example of Boolean values in Python
print(10 > 9)  # True, because 10 is greater than 9
print(10 == 9)  # False, because 10 is not equal to 9
print(10 < 9)  # False, because 10 is not less than 9

# Using Boolean in an if statement
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")  # This will be printed

# Using the bool() function to evaluate values
print(bool("Hello"))  # True, because the string is not empty
print(bool(15))  # True, because 15 is a non-zero number

# Evaluating variables with bool()
x = "Hello"
y = 15

print(bool(x))  # True, because x is a non-empty string
print(bool(y))  # True, because y is a non-zero number

# Most values are True
print(bool("abc"))  # True
print(bool(123))  # True
print(bool(["apple", "cherry", "banana"]))  # True

# Some values are False
print(bool(False))  # False
print(bool(None))  # False
print(bool(0))  # False
print(bool(""))  # False
print(bool(()))  # False
print(bool([]))  # False
print(bool({}))  # False

# Custom class with __len__ method returning 0
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))  # False, because __len__ returns 0

# Function returning a Boolean value
def myFunction():
    return True

print(myFunction())  # True

# Using function's Boolean return value in an if statement
if myFunction():
    print("YES!")  # This will be printed
else:
    print("NO!")

# Using isinstance() to check data type
x = 200
print(isinstance(x, int))  # True, because x is an integer