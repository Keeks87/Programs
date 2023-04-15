'''Create a simple calculator application that asks a user to enter two
numbers and the operation (e.g. +, -, x, etc.) that they’d like to perform on
the numbers. Display the answer to the equation. Every equation entered
by the user should be written to a text file. Use defensive programming to
write this program in a manner that is robust and handles unexpected
events and user inputs.
● Now extend your program to give the user the option to either enter two
numbers and an operator, like before or to read all of the equations from a
new txt file (the user should add the name of the txt file as an input) and
print out all of the equations together with the results. Use defensive
coding to ensure that the program does not crash if the file does not exist
and that the user is prompted again to enter the name of the file.'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return

def calculator(input_mode):
    # Define the operations that the calculator can perform
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    if input_mode == "manual":
        # Ask user to enter two numbers and operation
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        op = input("Enter operation (+, -, *, /): ")

        # Check if the operation entered is valid
        if op not in operations:
            print("Invalid operation. Please enter a valid operation.")
            return

        # Calculate and display result
        result = operations[op](num1, num2)
        print("Result: ", result)

        # Write equation and result to a text file
        with open("calculations.txt", "a") as f:
            f.write(f"{num1} {op} {num2} = {result}\n")
    elif input_mode == "file":
        # Ask user to enter the file name
        file_name = input("Enter the name of the file: ")

        # Read equations from the file
        try:
            with open(file_name, "r") as f:
                equations = f.readlines()
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")
            calculator("file")
            return

        # Print the equations and results
        for equation in equations:
            num1, op, num2, _, result = equation.split()
            num1 = float(num1)
            num2 = float(num2)
            result = float(result)
            print(f"{num1} {op} {num2} = {result}")
    else:
        print("Invalid input mode. Please enter either 'manual' or 'file'.")
        return

if __name__ == "__main__":
    while True:
        try:
            input_mode = input("Enter input mode ('manual' or 'file'): ")
            calculator(input_mode)
            repeat = input("Do you want to perform another calculation (y/n)? ")
            if repeat.lower() != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
