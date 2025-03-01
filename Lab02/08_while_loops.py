# Example of a while loop
# Print i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i += 1  # Increment i to avoid infinite loop

# Example of using break in a while loop
# Exit the loop when i is 3
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # Stop the loop
    i += 1

# Example of using continue in a while loop
# Skip the iteration when i is 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # Skip the rest of the code in this iteration
    print(i)

# Example of using else with a while loop
# Print a message once the condition is false
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")  # This runs after the loop ends