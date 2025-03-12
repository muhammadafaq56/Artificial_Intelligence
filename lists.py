# LISTS IN PYTHON
# A list is a collection of items enclosed in square brackets [].
# Items in a list can be of different types.

# Creating lists with different data types
list1 = [10, 20, 30, 40]  # List of integers
print(list1)
print(type(list1))

list2 = ["apple", "banana", "cherry"]  # List of strings
print(list2)
print(type(list2))

list3 = [5.6, "hello", 42]  # Mixed data type list
print(list3)
print(type(list3))

# EMPTY LIST
empty_list = []
print(empty_list)

# LIST INDICES
# List elements can be accessed using indices, starting from 0.
colors = ["Red", "Blue", "Green", "Black"]

print(colors[0])   # First element
print(colors[-1])  # Last element
print(colors[1:3]) # Slicing (from index 1 to 2)

# INDEX OUT OF RANGE ERROR
# print(colors[4])  # Uncommenting this will cause an error

# LIST SLICING
# Lists can be sliced using the syntax list[start:end]
print(colors[:2])   # First two items
print(colors[1:])   # From index 1 to end
print(colors[:-1])  # All except the last

# CONDITIONAL STATEMENTS
# Used to check conditions in Python.

a = 5
b = 10

if a == b:
    print("a is equal to b")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# COMPARISON OPERATORS
# ==  : Equal to
# !=  : Not equal to
# <   : Less than
# <=  : Less than or equal to
# >   : Greater than
# >=  : Greater than or equal to