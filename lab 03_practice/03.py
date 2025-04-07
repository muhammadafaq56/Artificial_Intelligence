import random  # Import the random module to generate random numbers

# Ask the user to make an initial guess
x = int(input("Enter guess: "))

# Generate a random number between 1 and 9
y = random.randint(1, 9)

# Keep asking the user to guess until the correct number is guessed
while x != y:
    x = int(input("Enter guess: "))

# If guessed correctly, print success message
print("Well guessed!")
