#Create a new Python file in this folder called jokes.py
#You are going to create a random joke generator using Python’s random module. 
#This will require a bit of research on your part. For more information on the random module look here.
#Create a list of jokes.
#Use the random module to display a random joke each time the code runs.

import random

# list of jokes
jokes = [
    "My father drank so heavily, when he blew on the birthday cake he lit the candles.", 
    "I was in my car driving back from work. A police officer pulled me over and knocked on my window. I said, 'One minute I'm on the phone.", 
    "I worry about ridiculous things, you know, how does a guy who drives a snowplough get to work in the morning… that can keep me awake for days.", 
    "I used to go out with a giraffe. Used to take it to the pictures and that. You'd always get some bloke complaining that he couldn't see the screen. It's a giraffe, mate. What do you expect? 'Well he can take his hat off for a start!'",
    "Here's a picture of me with REM. That's me in the corner."
    "People say 'Bill, are you an optimist?' And I say, 'I hope so.'"
    "I rang up British Telecom and said: 'I want to report a nuisance caller.' He said: 'Not you again.'"
    "Life is like a box of chocolates. It doesn't last long if you're fat."
    "We weren't very religious. On Hanukkah, my mother had our menorah on a dimmer."
    ]

# repeat the code
while True:
    # randomly select and print a joke from the list
    print(random.choice(jokes))
    # wait for user input before repeating
    input("Press enter to see another joke.")
