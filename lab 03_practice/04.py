# First half: increasing stars
for i in range(1, 6):  # i goes from 1 to 5
    for j in range(i):  # inner loop prints i stars
        print("*", end="")
    print()  # move to next line

# Second half: decreasing stars
for i in range(4, 0, -1):  # i goes from 4 to 1
    for j in range(i):  # inner loop prints i stars
        print("*", end="")
    print()  # move to next line
