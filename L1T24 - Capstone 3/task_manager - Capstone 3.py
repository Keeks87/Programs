
import datetime

# Function to register new user
def reg_user(current_user):
    if current_user == "admin":
        # Get new user's username and password
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        password_confirm = input("Confirm password: ")

        # Check if username already exists in user.txt
        with open("user.txt", "r") as f:
            users = f.readlines()
        existing_users = [line.split(",")[0] for line in users]
        if username in existing_users:
            print("Username already exists, please choose a different username.")
            return
        # Check if the passwords match
        if password == password_confirm:
            with open("user.txt", "a") as f:
                f.write(f"{username},{password}\n")
            print("User added successfully!")
        else:
            print("Passwords do not match, user not added.")
    else:
        print("You do not have permission to register a new user.")

# Function to add a new task
def add_task():
    username = input("Enter username of task assignee: ")
    title = input("Enter title of task: ")
    description = input("Enter description of task: ")
    due_date = input("Enter due date of task (YYYY-MM-DD): ")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("tasks.txt", "a") as f:
        f.write(f"{username},{title},{description},{current_date},{due_date},No\n")
    print("Task added successfully!")

# Function to view all tasks
def view_all():
    with open("tasks.txt", "r") as f:
        for line in f:
            username, title, description, current_date, due_date, _ = line.strip().split(",")
            print(f"Username: {username}\nTitle: {title}\nDescription: {description}\nDate Added: {current_date}\nDue Date: {due_date}")


# Function to view tasks assigned to current user
def view_mine(current_user):
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    my_tasks = [line for line in tasks if line.startswith(current_user)]
    if not my_tasks:
        print("You have no tasks.")
        return
    while True:
        # Display tasks with corresponding numbers
        for i, task in enumerate(my_tasks):
            task = task.strip().split(",")
            print(f"{i+1}. {task[1]} - {task[4]}")
        choice = input("Select a task number to edit or mark as complete or -1 to return to main menu: ")
        if choice == "-1":
            break
        if not choice.isnumeric() or int(choice) > len(my_tasks):
            print("Invalid choice, please try again.")
            continue
        task_num = int(choice) - 1
        task = my_tasks[task_num].strip().split(",")
        task_status = task[5]
        if task_status == "Yes":
            print("Task already complete, cannot edit.")
            continue
        task_edit = input("Do you want to edit task or mark as complete(e/c): ").lower()
        if task_edit == "e":
            # Allow user to edit username or due date
            new_username = input("Enter new username of task assignee: ")
            new_due_date = input("Enter new due date of task (YYYY-MM-DD): ")
            task[0] = new_username
            task[4] = new_due_date
            my_tasks[task_num] = ",".join(task) + "\n"
            with open("tasks.txt", "w") as f:
                f.writelines(my_tasks)
            print("Task has been edited")
        elif task_edit == "c":
            task[5] = "Yes"
            my_tasks[task_num] = ",".join(task) + "\n"
            with open("tasks.txt", "w") as f:
                f.writelines(my_tasks)
            print("Task has been marked as complete")

# function to display statistics
def display_statistics():
                # Display statistics
                try:
                    with open("task_overview.txt", "r") as f:
                        for line in f:
                            print(line)
                except FileNotFoundError:
                    generate_report()
                    with open("task_overview.txt", "r") as f:
                        for line in f:
                            print(line)
                try:
                    with open("user_overview.txt", "r") as f:
                        for line in f:
                            print(line)
                except FileNotFoundError:
                    generate_report()
                    with open("user_overview.txt", "r") as f:
                        for line in f:
                            print(line)

# Function to generate reports
def generate_report():
    # Report of all tasks
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task.strip().split(",")[5] == "Yes"])
    uncompleted_tasks = len([task for task in tasks if task.strip().split(",")[5] == "No"])
    overdue_tasks = len([task for task in tasks if task.strip().split(",")[5] == "No" and datetime.datetime.strptime(task.strip().split(",")[4], "%Y-%m-%d") < datetime.datetime.now()])
    uncompleted_percent = uncompleted_tasks / total_tasks * 100
    overdue_percent = overdue_tasks / total_tasks * 100
    with open("task_overview.txt", "w") as f:
        f.write(f"Total number of tasks: {total_tasks}\n")
        f.write(f"Total number of completed tasks: {completed_tasks}\n")
        f.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        f.write(f"Total number of overdue tasks: {overdue_tasks}\n")
        f.write(f"Percentage of tasks that are incomplete: {uncompleted_percent:.2f}%\n")
        f.write(f"Percentage of tasks that are overdue: {overdue_percent:.2f}%\n")
    print("Task overview report generated.")

    # Report of all users and their tasks
    with open("user.txt", "r") as f:
        users = f.readlines()
    total_users = len(users)
    with open("user_overview.txt", "w") as f:
        f.write(f"Total number of users: {total_users}\n")
        f.write(f"Total number of tasks: {total_tasks}\n\n")
        for user in users:
            user_tasks = [task for task in tasks if task.startswith(user.strip().split(",")[0])]
            total_user_tasks = len(user_tasks)
            user_completed_tasks = len([task for task in user_tasks if task.strip().split(",")[5] == "Yes"])
            user_uncompleted_tasks = len([task for task in user_tasks if task.strip().split(",")[5] == "No"])
            user_overdue_tasks = len([task for task in user_tasks if task.strip().split(",")[5] == "No" and datetime.datetime.strptime(task.strip().split(",")[4], "%Y-%m-%d") < datetime.datetime.now()])
            user_completed_percent = user_completed_tasks / total_user_tasks * 100 if total_user_tasks > 0 else 0
            user_uncompleted_percent = user_uncompleted_tasks / total_user_tasks * 100 if total_user_tasks > 0 else 0
            user_overdue_percent = user_overdue_tasks / total_user_tasks * 100 if total_user_tasks > 0 else 0
            assigned_percent = total_user_tasks / total_tasks * 100
            f.write(f"Username: {user.strip().split(',')[0]}\n")
            f.write(f"Total number of tasks assigned: {total_user_tasks}\n")
            f.write(f"Percentage of total tasks assigned to this user: {assigned_percent:.2f}%\n")
            f.write(f"Percentage of tasks assigned to this user that have been completed: {user_completed_percent:.2f}%\n")
            f.write(f"Percentage of tasks assigned to this user that must still be completed: {user_uncompleted_percent:.2f}%\n")
            f.write(f"Percentage of tasks assigned to this user that have not yet been completed and are overdue: {user_overdue_percent:.2f}%\n\n")
    print("User overview report generated.")

def login():
    current_user = ""
    while True:
    # Main menu code
        username = input("Enter your username: ")
        if not username:
            print("Username cannot be empty. Please try again.")
            continue
        password = input("Enter your password: ")
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
        with open("user.txt", "r") as f:
            users = f.readlines()
        existing_users = [line.split(",")[0] for line in users]
        if username in existing_users:
            current_user = username
            # Code to check if the user is admin or not
        else:
            print("Invalid username, please try again.")

        while True:
            if current_user == "admin":
                menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    ds - display statistics
    gr - generate report
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
                reg_user(current_user)
                

            elif menu == "a":
                add_task()

            elif menu == "va":
                view_all()

            elif menu == "vm":
                view_mine(current_user)

            elif menu == "ds":
                display_statistics()
            
            elif menu == "gr":
                generate_report()

            elif menu == "e":
                print("Goodbye!!!")
                exit() 

def main():
    while not login():
        pass  # keep trying to log in until successful

    # Present the menu to the user
        print("Welcome! Here is the menu:")
        print("1. Option 1")
        print("2. Option 2")

if __name__ == "__main__":
    main()
