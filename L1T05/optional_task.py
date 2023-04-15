#create a new file called optional_task.py
#Write Python code to take the name of a user's favourite restuarant and
#store it in a variable called fav_rest.
#Below this, write a statement to take in the user's favourite number. Use
#casting to store it in an integer variable called int_fav.
#Print out both of these using two separate print statements below what
#you have written. Be careful!
#Once this is working, try cast fav_rest to an integer. What happens? Add a
#comment in your code to explain why this is.

#Input user's favourite restuarant

fav_rest = input("What is your favourite restuarant?")

#Input user's favourite number

int_fav = int(input("What is your favourite number?"))

#Print out both 

print(fav_rest)
print(int_fav)

#Cast fav_rest to an integer

print(int(fav_rest)) #ValueError is received, because you can't cast a character string using this method

