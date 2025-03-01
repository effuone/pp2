import functools
import math

# 1. Write a Python program with builtin function to multiply all the numbers in a list
def multiply_all_numbers(numbers):
    return round(functools.reduce(lambda x, y: x * y, numbers), 6)

# 2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_upper_and_lower_case_letters(s):
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    return
# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

# 4. Write a Python program that invoke square root function after specific milliseconds.
def square_root_after_milliseconds(n, ms):
    import time
    time.sleep(ms / 1000)
    return round(math.sqrt(n), 6)

# 5. Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_elements_true(t):
    return all(t)


print("1. Multiply all numbers in a list")
print(multiply_all_numbers([1, 2, 3, 4, 5]))

print("\n2. Count upper and lower case letters")
print(count_upper_and_lower_case_letters("Hello, World!"))

print("\n3. Check if palindrome")
print(is_palindrome("hello"))

milliseconds = 2123
print(f"\n4. Square root after {milliseconds} milliseconds")
print(square_root_after_milliseconds(25100, milliseconds))

print("\n5. Check if all elements of a tuple are true")
print(all_elements_true((True, True, True)))