# Prompt the user to enter a string and store it in variable 's'
s = input("Enter a string: ")

# Count the number of alphabetical characters in the string
# Using generator expression with isalpha() method
letters = sum(c.isalpha() for c in s)

# Count the number of digit characters in the string
# Using generator expression with isdigit() method
digits = sum(c.isdigit() for c in s)

# Print the count of alphabetical characters
print("Letters: ", letters)

# Print the count of digit characters
print("Digits:", digits)