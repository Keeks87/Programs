#Define a list of strings of your 5 favourite movies.
#Now, loop over the list. For each item in the list, print out "Movie: " plus the movie's name.
#Can you figure out how to print out Movie 1: <Movie 1's name>. Movie 2: ... etc?
#HINT: YOU WILL NEED TO LOOK UP the enumerate command in Python using a Google search. This 
#command allows you to loop over a list retaining both the item at every position and its 
#index (i.e. position in the list).

#Define a list of strings of your 5 favourite movies
movies_in = ["Avatar", "The god father", "Saving private Ryan", "Love Actually", "Deadpool"]

#Loop over the list
for index, movie in enumerate(movies_in):
    #For each item in the list, print out "Movie: " plus the movie's name.
    print(f"Movie {index+1}: {movie}")
