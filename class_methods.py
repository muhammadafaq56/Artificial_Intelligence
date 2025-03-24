# Class with a method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Extra Example: Another method to display age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_age(self):
        print("My age is", self.age)

p1 = Person("John", 36)
p1.display_age()
