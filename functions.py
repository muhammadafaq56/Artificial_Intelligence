# Function with list parameter
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Extra Example: Function to calculate sum of list elements
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))


print(sum([1,2,3,4]))