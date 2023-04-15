#Create a new Python file in your folder called float_manipulation.py
#You will need to import the math module and use its built-in functions to complete this task.
#Write a program that starts by asking the user to input 10 floats (these can be a combination 
#of whole numbers and decimals). Store these numbers in a list.
    #Find the total of all the numbers and print the result.
    #Find the index of the maximum and print the result.
    #Find the index of the minimum and print the result.
    #Calculate the average of the numbers and round off to 2 decimal places.
    #Print the result.
    #Find the median number and print the result.

import math
import statistics

# Get user input and store in a list
floats = []
for i in range(10):
    # Prompt user for float input and store in list
    floats.append(float(input(f"Enter float {i+1}: ")))

# Find the total of all the numbers
total = sum(floats)
print(f"Total: {total}")

# Find the index of the maximum and print the result
max_index = floats.index(max(floats))
print(f"Index of max: {max_index}")

# Find the index of the minimum and print the result
min_index = floats.index(min(floats))
print(f"Index of min: {min_index}")

# Calculate the average of the numbers and round off to 2 decimal places
average = round(sum(floats) / len(floats), 2)
print(f"Average: {average}")

# Find the median number
median = statistics.median(floats)
print(f"Median: {median}")
