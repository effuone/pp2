import math

# everything is rounded to 6 decimal places

# Write a Python program to convert degree to radian.
def degrees_to_radians(degrees):
    return round(degrees * math.pi / 180, 6)

# Write a Python program to calculate the area of a trapezoid.
def trapezoid_area(a, b, h):
    # a - base first value
    # b - base second value
    # h - height
    return round((a + b) / 2 * h, 6)

# Write a Python program to calculate the area of regular polygon.
def regular_polygon_area(n, s):
    return round(n * s ** 2 / (4 * math.tan(math.pi / n)), 6)

# Write a Python program to calculate the area of a parallelogram.
def parallelogram_area(b, h):
    return round(b * h, 6)

print("Python program to convert degree to radian:")
print(degrees_to_radians(15))

print("\nPython program to calculate the area of a trapezoid:")
print(trapezoid_area(6, 5, 5))

print("\nPython program to calculate the area of regular polygon:")
print(regular_polygon_area(4, 25))

print("\nPython program to calculate the area of a parallelogram:")
print(parallelogram_area(5, 6))