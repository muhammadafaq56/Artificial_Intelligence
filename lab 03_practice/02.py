# Display menu to the user
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Ask user for their choice
choice = int(input("Enter your choice (1 or 2): "))

# If user chooses Celsius to Fahrenheit
if choice == 1:
    c = int(input("Enter the temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit:", f)

# If user chooses Fahrenheit to Celsius
elif choice == 2:
    f = int(input("Enter the temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius:", c)

# If user enters invalid choice
else:
    print("Invalid choice! Please enter 1 or 2.")
