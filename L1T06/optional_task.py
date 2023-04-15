#Ask the user to enter the length of all three sides of a triangle.
#Calculate the area of the triangle.
#Print out the area.
#Hint: if side1, side2 and side3 are the sides of the triangle:
    #s = (side1 + side2 + side3) / 2 and
    #area = √(s(s-a)*(s-b)*(s-c))


import math

#input lengths of all three sides of a triangle.

side1 = int(input("enter first side of triangle"))
side2 = int(input("enter second side of triangle"))
side3 = int(input("enter third side of triangle"))

#Calculate the area of the triangle.

s = (side1 + side2 + side3) / 2
area = math.sqrt(s) #I couldn't get the root sign into the code, I used https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter. link do import the math functions. 

#Print out the area.

print(area)

