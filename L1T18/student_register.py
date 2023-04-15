#We will write a program called student_register.py that allows students to register for an exam venue.
#First, ask the user how many students are registering.
#Create a for loop that runs for that amount of students
#Each time the loop runs it needs to ask the next student to enter their ID number.
#Write each of the ID numbers to a Text File called reg_form.txt
#Include a dotted line to sign because this document will be used as an attendance register which the 
#students will sign when they arrive at the exam venue.

#Ask the user for number of students
num_students = int(input("How many students are registering for the exam? "))

#Open the file in write mode
with open("reg_form.txt", "w") as file:
    #Write the header
    file.write("ID Number\tSignature\n")
    file.write("------------------------------\n")

    #Create loop to get the IDs
    for i in range(num_students):
        #Ask the user for the ID number
        id_num = input(f"Enter the ID number for student {i+1}: ")
        #Write the ID number to the file
        file.write(f"{id_num}\t\t\n")
        #Write a dotted line for the signature
        file.write(".......................\n")

print("All IDs have been written to the file reg_form.txt.")
