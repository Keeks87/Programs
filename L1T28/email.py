'''In this task, we’re going to be simulating an email message. Some of the logic has
been filled out for you in the email.py file.
    - Open the file called email.py.
    - Create a class definition for an Email which has four variables:
    has_been_read, email_contents, is_spam and from_address.
    - The constructor should initialise the sender’s email address.
    - The constructor should also initialise has_been_read and is_spam to false.
    - Create a function in this class called mark_as_read which should change
    has_been_read to true.
    - Create a function in this class called mark_as_spam which should change is_spam to true.
    - Create a list called inbox to store all emails (note that you can have a list of objects).
    - Then create the following functions:
        - add_email - which takes in the contents and email address from the
        received email to make a new Email object.
        - get_count - returns the number of messages in the store.
        - get_email - returns the contents of an email in the list. For this, allow
        the user to input an index i.e. get_email(i) returns the email stored
        at position i in the list. Once this has been done, has_been_read
        should now be true.
        - get_unread_emails - should return a list of all the emails that haven’t
        been read.
        - get_spam_emails - should return a list of all the emails that have been
        marked as spam.
        - delete - deletes an email in the inbox.
Now that you have these set up, let’s get everything working!
    - Fill in the rest of the logic for what should happen when the user inputs
    send/read/quit etc. so that all of the functions are utilised.. Some of it has
    been done for you.'''

class Email:
    # constructor for email object
    def __init__(self, from_address, email_contents):
        # initializes has_been_read as False
        self.has_been_read = False
        # stores email contents
        self.email_contents = email_contents
        # initializes is_spam as False
        self.is_spam = False
        # stores sender's email address
        self.from_address = from_address
        
    # function to mark email as read
    def mark_as_read(self):
        self.has_been_read = True
        
    # function to mark email as spam
    def mark_as_spam(self):
        self.is_spam = True

# list to store all email objects        
inbox = []

# function to add email to inbox
def add_email(from_address, email_contents):
    # creates email object
    email = Email(from_address, email_contents)
    # adds email to inbox list
    inbox.append(email)
    
# function to get the number of emails in inbox
def get_count():
    return len(inbox)

# function to get email contents for a given index
def get_email(index):
    # checks if index is valid
    if index < 0 or index >= len(inbox):
        return None
    # marks email as read
    email = inbox[index]
    email.mark_as_read()
    # returns email contents
    return email.email_contents

# function to get unread emails
def get_unread_emails():
    # returns a list of unread email contents
    return [email.email_contents for email in inbox if not email.has_been_read]

# function to get spam emails
def get_spam_emails():
    # returns a list of spam email contents
    return [email.email_contents for email in inbox if email.is_spam]

# function to delete email at a given index
def delete(index):
    # checks if index is valid
    if index >= 0 and index < len(inbox):
        del inbox[index]
        
# variable to store user choice
user_choice = ""
# loop until user quits
while user_choice != "quit":
    # get user choice
    user_choice = input("What would you like to do - read/mark spam/send/quit?").lower()
    # action for read option
    if user_choice == "read":
        # check if inbox is empty
        if not inbox:
            print("No emails in inbox.")
        else:
            # iterate over emails in inbox
            for i, email in enumerate(inbox):
                # check if email has been read
                if not email.has_been_read:
                    print("{}. From: {}\n{}".format(i, email.from_address, email.email_contents))
    elif user_choice == "mark spam":
        # Check if there are any emails in the inbox
        if not inbox:
            print("No emails in inbox.")
        else:
            # Ask for the email index to mark as spam
            index = int(input("Enter the email index you want to mark as spam: "))
            # Check if the index is valid
            if index < 0 or index >= len(inbox):
                print("Invalid index.")
            else:
                # Mark the email as spam
                inbox[index].mark_as_spam()
                print("Email marked as spam.")
    elif user_choice == "send":
        # Ask for the sender's email address
        from_address = input("Enter the sender's email address: ")
        # Ask for the email contents
        email_contents = input("Enter the email contents: ")
        # Add the email to the inbox
        add_email(from_address, email_contents)
        print("Email added to inbox.")
    # user choice quit
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")