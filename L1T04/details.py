#create a new Python file in this folder called details.py
#Use an input command to get the following information from the user.
#Name
#Age
#House number
#Street name
#Print out a single sentnce containing all the detail of the user.
#For example:
#This is John Smith he is 28 years old and lives at house number 42 on Hamilton Street.


name_surname = input("What is your full name?")

age = input("How old are you?")

house_number = input("What is your house nr?")

street_name = input("What is your street name?")

print("{0} is {1} years old and lives at {2} {3}.".format(name_surname, age, house_number, street_name))
 
