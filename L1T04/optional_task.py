#Create a new Python file in this folder called optional_task.py
#Use input to get any two numbers from the user.
#Store these numbers in variables called num1 and num2.
#Now swap these tow numbers around. The numbers stored in num2 should now be stored in num1.
#Print out the values of num1 and num2 before the swap and the values of num1 and num2 after the swop.

#I used link https://www.geeksforgeeks.org/python-program-to-swap-two-variables/ to assit me as I was unable 
#to get the correct output in my code. (I ended up using a temp variable "temp" to fix my code)

#Input for num1 and num2
num1 = input("Please insert a number")
num2 = input("Please insert a second number")

#pint num1 and num2 before swap
print(num1)
print(num2)

#swap num1 with num2 value and num2 with num1 value
temp = num1
num1 = num2
num2 = temp


#pint num1 and num2 after swap
print(num1)
print(num2)
