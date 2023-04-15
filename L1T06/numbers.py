#create a new Python file in this folder called numbers.py
#Ask the user to enter three different integers
#Then print out:
#The sum of all the numbers
#The first number minus the second number
#The Third number multiplied by the first number
#The sum of all three numbers divided by the third number

#Input different integers

first_number = int(input("enter a integer"))
second_number = int(input("enter a integer"))
third_number = int(input("enter a integer"))

#Print the sum of all the numbers

sum_numbers = first_number + second_number + third_number
print(sum_numbers)

#Print the first number minus the second number

sub_numbers = first_number - second_number
print(sub_numbers)

#Print the third number multiplied by the first number

mult_numbers = third_number * first_number
print(mult_numbers)

#print the sum of all three numbers divided by the third number

sumdiv_numbers = (sum_numbers) / third_number
print(sumdiv_numbers)

