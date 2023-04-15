#Create a new text file in this folder called input.txt. In the input.txt file enter some text, 
#making sure it is at least a few lines long.
#Write a program that will count the number of characters, words and lines in the file.
#Your program should also count the total number of vowels (a, e, i, o and u) in the file.
#Print out your results.


#Open the file
with open("input.txt") as f:
    # Read the contents of the file
    contents = f.read()

#Initialize counters for characters, words, lines, and vowels
char_count = 0
word_count = 0
line_count = 0
vowel_count = 0

#Iterate over the contents of the file, counting characters, words, lines, and vowels
for c in contents:
    #Increment the character count
    char_count += 1
    #Increment the vowel count if the character is a vowel
    if c in "aeiouAEIOU":
        vowel_count += 1
    #Increment the word count if the character is a space or a newline
    if c in " \n":
        word_count += 1
    #Increment the line count if the character is a newline
    if c == "\n":
        line_count += 1

#Adjust the word count to account for the last word
word_count += 1

#Print the results
print("Number of characters:", char_count)
print("Number of words:", word_count)
print("Number of lines:", line_count)
print("Number of vowels:", vowel_count)
