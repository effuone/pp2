#Create a generator that generates the squares of numbers up to some number N.
def gen_squares(n):
    for i in range(n):
        yield i ** 2
        
#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
            
#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b):
        yield i ** 2
        
#Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    for i in range(n, -1, -1):
        yield i
    
print("Squares up to 10:")
for i in gen_squares(10):
    print(i)

print("\nEven numbers up to 10:")
for i in even_numbers(10):
    print(i)
    
print("\nNumbers divisible by 3 and 4 up to 10:")
for i in divisible_by_3_and_4(10):
    print(i)

print("\nSquares from 5 to 10:")
for i in squares(5, 10):
    print(i)

print("\nCountdown from 10:")
for i in countdown(10):
    print(i)