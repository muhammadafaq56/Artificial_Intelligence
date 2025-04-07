# Accept input from the user as comma-separated binary numbers
binary_numbers = input("Enter binary numbers separated by commas: ").split(',')

# Initialize an empty list to store numbers divisible by 5
result = []

# Iterate over each binary number
for num in binary_numbers:
    # Convert the binary number to its decimal equivalent
    decimal_value = int(num, 2)
    
    # Check if the decimal value is divisible by 5
    if decimal_value % 5 == 0:
        # If yes, add the binary number to the result list
        result.append(num)

# Print the result as a comma-separated string
print(",".join(result))