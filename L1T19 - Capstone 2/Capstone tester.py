# read the current list of usernames and passwords from the file
credentials = {}
with open("user.txt", "r") as f:
    for line in f:
        username, password = line.strip().split(":")
        credentials[username] = password

# prompt the user for their username and password
while True:
    print("Enter your username and password:")
    username = input("Username: ")
    password = input("Password: ")

    # check if the username and password are correct
    if credentials.get(username) == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")

# store the logged in user's username in a variable
logged_in_user = username

# prompt the user for a new task or to view their tasks
while True:
    print("Enter 'add' to add a new task or 'view' to view your tasks:")
    action = input().lower()

    # add a new task
    if action == "add":
        # request the new task information from the user
        print("Enter the following information for the new task:")
        title = input("Title of the task: ")
        description = input("Description of the task: ")
        due_date = input("Due date of the task (YYYY-MM-DD): ")

        # get the current date
        from datetime import datetime
        date_added = datetime.now().strftime("%Y-%m-%d")

        # add the task to the file
        with open("task.txt", "a") as f:
            f.write(f"{logged_in_user}: {title}: {description}: {date_added}: {due_date}: No\n")

        print("Task added successfully!")

    # view the logged in user's tasks
    elif action == "view":
        # read the tasks from the file and print them to the console
        with open("task.txt", "r") as f:
            for line in f:
                assignee, title, description, date_added, due_date, status = line.strip().split(": ")
                if assignee == logged_in_user:
                    print(f"Assignee: {assignee}\nTitle: {title}\nDescription: {description}\nDate added: {date_added}\nDue date: {due_date}\nStatus: {status}\n")
    else:
        print("Invalid action. Please try again.")
