"""
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""
class Course:
    # Class variable to store the name of the course
    name = "Fundamentals of Computer Science"
    # Class variable to store the website to contact the course
    contact_website = "www.hyperiondev.com"

    # Method to print the contact details for the course
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Method to print the head office location of the course
    def head_office(self):
        print("Head office location: Cape Town")

class OOPCourse(Course):
    # Constructor to initialize the description and trainer attributes
    def __init__(self, description, trainer):
        self.description = description
        self.trainer = trainer

    # Method to print the course description and trainer name
    def trainer_details(self):
        print(f"The course is about {self.description}. The trainer is {self.trainer}.")
        
    # Method to print the course ID number
    def show_course_id(self):
        print("ID number of the course: #12345")

# Creating an object of the OOPCourse class
course_1 = OOPCourse("OOP Fundamentals", "Mr Anon A. Mouse")

# Calling the contact_details, trainer_details and show_course_id methods
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
