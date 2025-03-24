# Loop Control Statements

# Using 'continue' to skip specific iterations
for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        continue
    print("Current Letter:", letter)

# Using 'break' to stop the loop
for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        break
    print("Current Letter:", letter)

# Extra Example: Using 'pass' (does nothing but required syntactically)
for letter in "geeksforgeeks":
    if letter == "e":
        pass  # Placeholder for future code
    print("Processing:", letter)
