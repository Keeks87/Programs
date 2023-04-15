#Write a program that will act as a calculator.
#Create functions named add_num, subtract_num, multiply_num, and divide_num that asks the user to enter
#two numbers and adds, subtracts, multiplies, or divides them, respectively.
#Print out the following menu and ask the user to input a number that corresponds to the option they
#would like to choose:
#Option 1 - add
#Option 2 - subtract
#Option 3 - multiply
#Option 4 - divide
#If the user enters 1 call the add_num function
#If the user enters 2 call the subtract_num function
#If the user enters 3 call the multiply_num function
#If the user enters 4 call the divide_num function
#Make sure that the result of the calculation is printed out to the screen.

# function to add two numbers
def add_num():
    # input for first number
    num1 = float(input("Enter the first number: "))
    # input for second number
    num2 = float(input("Enter the second number: "))
    # return the sum of the two numbers
    return num1 + num2

# function to subtract two numbers
def subtract_num():
    # input for first number
    num1 = float(input("Enter the first number: "))
    # input for second number
    num2 = float(input("Enter the second number: "))
    # return the difference of the two numbers
    return num1 - num2

# function to multiply two numbers
def multiply_num():
    # input for first number
    num1 = float(input("Enter the first number: "))
    # input for second number
    num2 = float(input("Enter the second number: "))
    # return the product of the two numbers
    return num1 * num2

# function to divide two numbers
def divide_num():
    # input for first number
    num1 = float(input("Enter the first number: "))
    # input for second number
    num2 = float(input("Enter the second number: "))
    # return the quotient of the two numbers
    return num1 / num2

# print welcome message
print("Welcome to the Calculator!")

while True:
    # print menu
    print("Please select an option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # input for user selection
    choice = int(input())

    # check user selection and call appropriate function
    if choice == 1:
        result = add_num()
    elif choice == 2:
        result = subtract_num()
    elif choice == 3:
        result = multiply_num()
    elif choice == 4:
        result = divide_num()
    else:
        # handle invalid input
        print("Invalid option selected.")
        continue
    # print result
    print("Result: ", result)
