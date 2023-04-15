#Create a new Python file in this folder called manipulation.py
#Ask the user to enter a sentence using the input() method. Save the user's
#response in a variable called srt_manip.
#Using this string value, write the code to do the following:
    #Calculate and display the length of str_manip.
    #Find the last letter in str_manip. Replace every occurrence of this letter in str_manip with '@'
        #e.g. if str_manip = "this is a bunch of words", the output would be: "Thi@ i@ a bunch of word@"
    #Print the last 3 characters in str_manip backwards.
        #e.g. if str_manip = "this is a bunch of words", the output would be: "sdr".
    #Create a five-letter word that is made up of the first three character and the last two character in str_manip.
        #e.g. if str_manip = "this is a bunch of words", the output would be: "Thids".
    #Display each word on a new line.


#Ask user for a sentence

str_manip = input("Please enter a sentence")

#Calculate and display the length of str_manip.

print(len(str_manip))

#Find the last letter in str_manip. Replace every occurrence of this letter in str_manip with '@'

last_letter = str_manip [:-2:-1]
print(str_manip.replace(last_letter,"@")) #This was a fun challenge 


#Print the last 3 characters in str_manip backwards.

print(str_manip [:-4:-1])

#Create a five-letter word that is made up of the first three character and the last two character in str_manip.

first_three = str_manip [0:3]
last_two = str_manip [-2:]

print(first_three + last_two)

#Display each word on a new line.

print(*str_manip.split(), sep='\n') #I was stuck on this one, I used https://stackoverflow.com/questions/54122708/print-each-word-in-string-using-index-slicing to solve