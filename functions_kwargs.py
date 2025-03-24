# Function with keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")

# Extra Example: Function with arbitrary keyword arguments
def person_info(kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

person_info(name="Afaq", age=25, country="Pakistan")