import math
import itertools
import random

# 1. Convert grams to ounces
def convert_grams_to_ounces(grams): return 28.3495231 * grams

# 2. Fahrenheit to Celsius
def fahrenheit_to_celsius(f): return (5/9) * (f - 32)

# 3. Chicken-rabbit puzzle
def solve(numheads, numlegs):
    # y - kolvo zaycev
    # x - kolvo kuric
    # zaec - 1 head and 4 legs
    # kurica - 1 head and 2 legs
    # Poetomu:
    # x + y = numheads  (1)
    # 2x + 4y = numlegs (2)
    
    # x = numheads - y    
    # 2(numheads - y) + 4y = numlegs
    # 2numheads - 2y + 4y = numlegs
    # 2numheads + 2y = numlegs
    # 2y = numlegs - 2numheads
    
    # y = (numlegs - 2numheads) / 2
    # x = numheads - y
    
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    
    return y, x # zaycev, kuric

# 4. Filter prime numbers
def is_prime(n): return n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

def filter_prime(nums): return [n for n in nums if is_prime(n)]

# 5. Print permutations of a string
def permutations(s): return list(map("".join, itertools.permutations(s)))

# 6. Reverse words in a sentence
def reverse_words(s): return " ".join(s.split()[::-1])

# 7. Check for consecutive 3s
def has_33(nums): return "33" in "".join(map(str, nums))

# 8. Check if list contains 007 in order
def spy_game(nums): return "007" in "".join(map(str, [n for n in nums if n in {0, 7}]))

# 9. Compute volume of a sphere
def sphere_volume(r): return (4/3) * math.pi * r**3

# 10. Return list with unique elements
def unique_list(lst): return [x for i, x in enumerate(lst) if x not in lst[:i]]

# 11. Checkaem if palindrome
def is_palindrome(s): return s == s[::-1]

# 12. Print histogram
def histogram(lst): print("\n".join("*" * n for n in lst))

# 13. Guess the number game
def guess_number():
    name = input("Salamaleikum! What is your name?\n")
    num, guess, attempts = random.randint(1, 20), None, 0
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    # needs binary search lol
    while guess != num:
        guess, attempts = int(input("\nTake a guess.\n")), attempts + 1
        print("Nice!" if guess == num else "Too low" if guess < num else "Too high")
    print(f"\n{name}, you guessed my number in {attempts} guesses!")
