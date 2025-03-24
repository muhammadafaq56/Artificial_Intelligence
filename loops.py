# Loops in Python

# While loop example
count = 0
while count < 3:
    count += 1
    print("Hello Geek")

# Infinite while loop (use with caution)
# count = 0
# while count == 0:
#     print("Hello Geek")

# For loop with a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# For loop with a tuple
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# For loop with a string
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

# Extra Example: Looping through a dictionary
print("\nDictionary Iteration")
d = {"name": "Afaq", "age": 25}
for key, value in d.items():
    print(key, ":", value)