#Write a Python program called John.py that takes in a user’s input as a string.
#While the string is not “John”, add every string entered to a list until “John” is entered. 
#This program basically stores all incorrectly entered strings in a list where “John” is the
#only correct string.
#Print out the list of incorrect names.
#Example program run (what should show up in the Python Console when you run it):
#Enter your name : <user enters Tim>
#Enter your name : <user enters Mark>
#Enter your name: <user enters John>
#Incorrect names: [‘Tim’, ‘Mark’]
#HINT: When testing your While loop, you can make use of .upper() or .lower() to eliminate case sensitivity.

#Create empty list
inc_names = []

#Infinite loop for user to enter names
while True:
    #User input
    user_string = input("Please enter a name: ")
    
    #Convert the input to lowercase and compare it to "stop"
    #If the input is "stop", break
    if user_string.lower() == "john":
        break
    
    #If not "stop", add to list
    inc_names.append(user_string)
print(inc_names)