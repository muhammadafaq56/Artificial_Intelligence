# Class with constructor (__init__ method)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Extra Example: Creating multiple instances
p2 = Person("Afaq", 25)
print(p2.name, p2.age)
