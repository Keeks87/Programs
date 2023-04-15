#Follow these steps:
    #In this task, you will be creating a program for a small business that can help it to manage tasks assigned
    #to each member of the team. Copy the template program provided, task_template.py, and rename it task_manager.py
    #in this folder. This template has been provided to make this task a little easier for you. Your job is to 
    #open and then modify the template to achieve the rest of the compulsory task set out below. Remember to save
    #your work as you go along.
#This program will work with two text files, user.txt and tasks.txt. Open each of the files that accompany this
#project and take note of the following:
    #tasks.txt stores a list of all the tasks that the team is working on. Open the tasks.txt file that accompanies
    #this project. Note that this text file already contains data about two tasks. The data for each task is stored
    #on a separate line in the text file. Each line includes the following data about a task in this order:
        #The username of the person to whom the task is assigned.
        #The title of the task.
        #A description of the task.
        #The date that the task was assigned to the user.
        #The due date for the task.
        #Either a ‘Yes’ or ‘No’ value that specifies if the task has been completed yet.
    #user.txt stores the username and password for each user that has permission to use your program (task_manager.py).
    #Open the user.txt file that accompanies this project. Note that this text file already contains one default 
    #user that has the username, ‘admin’ and the password, ‘adm1n’. The username and password for each user must be
    #written to this file in the following format:
        #First, the username followed by a comma, a space and then the password.
        #One username and corresponding password per line.
    #Your program should allow your users to do the following:
        #Login. The user should be prompted to enter a username and password. A list of valid usernames and passwords
        #are stored in a text file called user.txt. Display an appropriate error message if the user enters a username
        #that is not listed in user.txt or enters a valid username but not a valid password. The user should repeatedly
        #be asked to enter a valid username and password until they provide appropriate credentials. The following menu
        #should be displayed once the user has successfully logged in:
            #If the user chooses ‘r’ to register a user, the user should be prompted for a new username and password.
            #The user should also be asked to confirm the password. If the value entered to confirm the password matches
            #the value of the password, the username and password should be written to user.txt in the appropriate format.
                #If the user chooses ‘a’ to add a task, the user should be prompted to enter the username of the person 
                #the task is assigned to, the title of the task, a description of the task and the due date of the task.
                #The data about the new task should be written to tasks.txt. The date on which the task is assigned 
                #should be the current date. Also assume that whenever you add a new task, the value that indicates 
                #whether the task has been completed or not is ‘No’.
            #If the user chooses ‘va’ to view all tasks, display the information for each task on the screen in an easy 
            #to read format.
            #If the user chooses ‘vm’ to view the tasks that are assigned to them, only display all the tasks that have
            #been assigned to the user that is currently logged-in in a user-friendly, easy to read manner.

#=====importing libraries===========
import datetime

#====Login Section====
# Read usernames and passwords from user.txt file
credentials = []
with open("user.txt", "r") as f:
    for line in f:
        username, password = line.strip().split(',')
        credentials.append((username,password))
# Login loop
while True:
    # Prompt user for username and password
    current_user = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if entered credentials are valid
    if any((username,password) == (current_user, password) for username,password in credentials):
        # Login successful, break out of loop
        print("Login successful!")
        break
    else:
        print("Invalid username or password, please try again.")

# Main menu loop
while True:
    # Present menu to user and get menu choice
    if current_user == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds - display statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == "r":
        # Add new user
        if current_user == "admin":
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            password_confirm = input("Confirm password: ")
            if password == password_confirm:
                # Add user to user.txt file
                with open("user.txt", "a") as f:
                    f.write(f"{username},{password}\n")
                print("User added successfully!")
            else:
                print("Passwords do not match, user not added.")
        else:
            print("You do not have permission to register a new user.")

    elif menu == "a":
        # Add new task
        username = input("Enter username of task assignee: ")
        title = input("Enter title of task: ")
        description = input("Enter description of task: ")
        due_date = input("Enter due date of task (YYYY-MM-DD): ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        # Add task to task.txt file
        with open("tasks.txt", "a") as f:
            f.write(f"{username},{title},{description},{current_date},{due_date},No\n")
        print("Task added successfully!")

    elif menu == "va":
        # View all tasks
        with open("tasks.txt", "r") as f:
            for line in f:
                username, title, description, current_date, due_date, _ = line.strip().split(",")
                print(f"Username: {username}\nTitle: {title}\nDescription: {description}\nDate Added: {current_date}\nDue Date: {due_date}")

    elif menu == "vm":
    # View tasks assigned to current user
        with open("tasks.txt", "r") as f:
            for line in f:
                username, title, description, current_date, due_date, _ = line.strip().split(',')
                if username == current_user:
                    print(f"Username: {username}\nTitle: {title}\nDescription: {description}\nDate Added: {current_date}\nDue Date: {due_date}")
    
    elif menu == "ds":
        # Display statistics
        task_count = 0
        user_count = 0

        # Count number of tasks
        with open("tasks.txt", "r") as f:
            for _ in f:
                task_count += 1
        # Count number of users
        with open("user.txt", "r") as f:
            for _ in f:
                user_count += 1

        # Print statistics
        print(f"Total number of tasks: {task_count}")
        print(f"Total number of users: {user_count}")

    elif menu == "e":
        print("Goodbye!!!")
        exit()
