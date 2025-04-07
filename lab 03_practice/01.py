# Loop through numbers from 1500 to 2700 (inclusive of 2700)
for i in range(1500, 2701):
    # Check if the number is divisible by both 5 and 7
    if(i % 5 == 0 and i % 7 == 0):
        # If the condition is true, print the number
        print(i)
