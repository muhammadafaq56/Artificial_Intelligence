# Initialize an empty list to store input lines
lines = []

# Continuously take user input until an empty line is entered
while True:
    line = input()  # Prompt for input (no visible message, just waits for input)
    if line == "":  # If the input is an empty string (user pressed Enter without typing)
        break       # Exit the loop
    lines.append(line.lower())  # Convert the line to lowercase and add it to the list

# Print each processed line (in lowercase) from the list
for line in lines:
    print(line)