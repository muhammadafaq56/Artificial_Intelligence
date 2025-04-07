# Loop through numbers from 1 to 50
for i in range(1, 51):
    # Check if the number is divisible by both 3 and 5
    if i % 5 == 0 and i % 3 == 0:
        print("Fizzbuzz")
    # Check if the number is divisible by 3 only
    elif i % 3 == 0:
        print("Fizz")
    # Check if the number is divisible by 5 only
    elif i % 5 == 0:
        print("Buzz")
    # If the number is not divisible by 3 or 5, print the number itself
    else:
        print(i)
