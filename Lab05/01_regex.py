import re

# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
def match_a_followed_by_b(s):
    return re.search(r'ab*', s)

# Write a Python program that matches a string that has an 'a' followed by two to three 'b''s.
def match_a_followed_by_2_3_b(s):
    return re.search(r'ab{2,3}', s)

# Write a Python program to find sequences of lowercase letters joined with a underscore.
def find_lowercase_letters_joined_with_underscore(s):
    return re.search(r'[a-zа-я]+_[a-zа-я]+', s, re.IGNORECASE)

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def find_uppercase_followed_by_lowercase(s):
    return re.search(r'[A-ZА-Я][a-zа-я]+', s, re.IGNORECASE)

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def match_a_followed_by_anything_ending_in_b(s):
    return re.search(r'a.*b$', s, re.IGNORECASE)

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def replace_space_comma_dot_with_colon(s):
    return re.sub(r'[ ,.]', ':', s)

# Write a python program to convert snake case string to camel case string.
def snake_to_camel(s):
    return re.sub(r'_([a-zа-я])', lambda x: x.group(1).upper(), s, flags=re.IGNORECASE)

# Write a Python program to split a string at uppercase letters.
def split_string_at_uppercase(s):
    return re.findall(r'[A-ZА-Я][^A-ZА-Я]*', s)

# Write a Python program to insert spaces between words starting with capital letters.
def insert_spaces_between_words_starting_with_capital(s):
    return re.sub(r'([A-ZА-Я][a-zа-я]+)', r' \1', s, flags=re.IGNORECASE)

# Write a Python program to convert a given camel case string to snake case.
def camel_to_snake(s):
    return re.sub(r'([A-ZА-Я])', r'_\1', s).lower()

# testing everythin in console 
def test_all_regex_functions(test_string):
    print(f"Testing string: '{test_string}'")
    print("-" * 50)
    
    print(f"1. Has 'a' followed by zero or more 'b's: {match_a_followed_by_b(test_string) is not None}")
    if match_a_followed_by_b(test_string):
        print(f"   Match found: {match_a_followed_by_b(test_string).group()}")
    
    print(f"2. Has 'a' followed by 2-3 'b's: {match_a_followed_by_2_3_b(test_string) is not None}")
    if match_a_followed_by_2_3_b(test_string):
        print(f"   Match found: {match_a_followed_by_2_3_b(test_string).group()}")
    
    print(f"3. Has lowercase letters joined with underscore: {find_lowercase_letters_joined_with_underscore(test_string) is not None}")
    if find_lowercase_letters_joined_with_underscore(test_string):
        print(f"   Match found: {find_lowercase_letters_joined_with_underscore(test_string).group()}")
    
    print(f"4. Has uppercase followed by lowercase: {find_uppercase_followed_by_lowercase(test_string) is not None}")
    if find_uppercase_followed_by_lowercase(test_string):
        print(f"   Match found: {find_uppercase_followed_by_lowercase(test_string).group()}")
    
    print(f"5. Has 'a' followed by anything ending in 'b': {match_a_followed_by_anything_ending_in_b(test_string) is not None}")
    if match_a_followed_by_anything_ending_in_b(test_string):
        print(f"   Match found: {match_a_followed_by_anything_ending_in_b(test_string).group()}")
    
    print(f"6. Replace space/comma/dot with colon: '{replace_space_comma_dot_with_colon(test_string)}'")
    
    print(f"7. Convert snake_case to camelCase: '{snake_to_camel(test_string)}'")
    
    print(f"8. Split at uppercase letters: {split_string_at_uppercase(test_string)}")
    
    print(f"9. Insert spaces between words starting with capital: '{insert_spaces_between_words_starting_with_capital(test_string)}'")
    
    print(f"10. Convert CamelCase to snake_case: '{camel_to_snake(test_string)}'")
    
    print("-" * 50)
    print()

# usin sample data from github task
with open('row.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    test_all_regex_functions(line.strip())


