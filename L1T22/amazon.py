#Write code to read the content of the text file input.txt.
#For each line in input.txt, write a new line in the new text file output.txt that computes the
#answer to some operation on a list of numbers.
#If the input.txt has the following:
    #Min: 1,2,3,5,6
    #Max: 1,2,3,5,6
    #Avg: 1,2,3,5,6
#Your program should generate output.txt as follows:
    #The min of [1, 2, 3, 5, 6] is 1.
    #The max of [1, 2, 3, 5, 6] is 6.
    #The avg of [1, 2, 3, 5, 6] is 3.4.
#Assume that the only operations given in the input file are min, max, and avg, and that the operation
#is always followed by a list of comma-separated integers.
#You should define the functions min, max, and avg that take in a list of integers and return the min, 
#max, or avg of the list.
#Your program should handle any combination of operations and any length of input numbers.
#You can assume that the list of input numbers are always valid integers and that the list is never 
#empty, so as not to have to write code to check for these cases.
#Hint: there is something strange about the first line of input.txt.

# Import statement
import math 

# Define functions to compute min, max, and avg of a list of numbers
def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_avg(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum / len(numbers)

# Define function to compute the x percentile of a list of numbers
def find_percentile(numbers, percentile):
    index = (percentile / 100) * len(numbers)
    # round up the index
    index = math.ceil(index) - 1 
    return sorted(numbers)[index]

# Open input and output files
with open("input.txt", "r", encoding="utf-8-sig") as input_file, open("output.txt", "w") as output_file: # it was hard to figure out the encoding part
    # Iterate over each line in the input file
    for line in input_file:
        # Split the line by the colon delimiter to separate the operation from the numbers
        operation, numbers_str = line.strip().split(":")
        # Convert the comma-separated numbers string to a list of integers
        numbers = [int(x) for x in numbers_str.split(",")]
        # Check the operation and call the corresponding function
        operation = operation.upper()
        if operation == "MIN":
            result = find_min(numbers)
            output_file.write(f"The min of {numbers} is {result}.\n")
            # Print the result to the console
            print(f"The min of {numbers} is {result}.")
        elif operation == "MAX":
            result = find_max(numbers)
            output_file.write(f"The max of {numbers} is {result}.\n")
            # Print the result to the console
            print(f"The max of {numbers} is {result}.")
        elif operation == "AVG":
            result = find_avg(numbers)
            output_file.write(f"The avg of {numbers} is {result}.\n")
            # Print the result to the console
            print(f"The avg of {numbers} is {result}.")
        elif operation[0] == "P" and int(operation[1:]) >= 10 and int(operation[1:]) <= 90:
            percentile = int(operation[1:])
            result = find_percentile(numbers, percentile)
            output_file.write(f"The {percentile}th percentile of {numbers} is {result}.\n")
            print(f"The {percentile}th percentile of {numbers} is {result}.")
        elif operation == "SUM":
            result = sum(numbers)
            output_file.write(f"The sum of {numbers} is {result}.\n")
            print(f"The sum of {numbers} is {result}.")