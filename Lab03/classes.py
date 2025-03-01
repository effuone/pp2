import math

# 1. Class to get and print strings
class StringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())

# k primeru
# sh = StringHandler()
# sh.getString()
# sh.printString()


# 2. Shape and Square classes
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# k primeru
# sq = Square(5)
# print(sq.area())


# 3. Rectangle class dochka Shape class'a
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# k primeru
# rect = Rectangle(3, 5)
# print(rect.area())


# 4. Point class with methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# k primeru
# p1 = Point(3,4)
# p2 = Point(228,8)
# print(p1.dist(p2))


# 5. Kaspi Bank Account class
class KaspiBankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money bro.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

# k primeru
# acc = KaspiBankAccount("Alibek", 100)
# acc.deposit(50)
# acc.withdraw(30)
# acc.withdraw(200)  # Should print "Not enough money bro."


# 6. Filter prime numbers using filter and lambda function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1,2,3,4,5,6,7,8,9,10,15, 17,19, 23,24, 29, 30]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)
