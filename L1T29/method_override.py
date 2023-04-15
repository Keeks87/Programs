'''Create a file named method_override.py and follow the instructions below:
    - Take user inputs that ask for the name, age, hair colour, and eye colour of a
    person.
    - Create an adult class with the following attributes and method:
        - name, age, eye_colour, and hair_colour
        - Method called can_drive() that prints the name of the person and
        that they are old enough to drive.
    - Create a subclass of the adult class named “Child” that has the same
    attributes, but overrides the can_drive method to print the persons name
    and that they are too young to drive.
    - Create some logic that determines if the person is 18 or older and create an
    instance of the Adult class if this is true. Otherwise, create an instance of the
    Child class. Once the object has been created, call the can_drive() method
    to print out whether the person is old enough to drive or not.'''

# Define the Adult class
class Adult:
    # Constructor for the Adult class
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # Method to determine if the person can drive
    def can_drive(self):
        if self.age >= 18:
            print(f"{self.name} is old enough to drive")
        else:
            print(f"{self.name} is not old enough to drive")

# Child class inherits from Adult class
class Child(Adult):
    # Override the can_drive method in the Child class
    def can_drive(self):
        print(f"{self.name} is too young to drive")

# Input for the person's details
name = input("Enter name: ")
age = int(input("Enter age: "))
eye_colour = input("Enter eye colour: ")
hair_colour = input("Enter hair colour: ")

# Create an instance of either Adult or Child class based on the person's age
if age >= 18:
    person = Adult(name, age, eye_colour, hair_colour)
else:
    person = Child(name, age, eye_colour, hair_colour)

# Call the can_drive method to determine if the person can drive
person.can_drive()
