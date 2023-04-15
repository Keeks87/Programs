#Create a new Python file in this folder called replace.py.
#Save the sentence: "The!quick!brown!fox!jumps!over!the!lazy!dog!." as a single string.
#Reprint this sentence as: "The quick brown fox jumps over the lazy dog." using
#the replace() function to replace every "!" excleamation mark with a blank space.
#Reprint that sentence as: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG." using the upper() function
#Print the sentence in reverse

#Input sentence

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#Print sentence by removing the "!" using replace()

print(sentence.replace("!"," "))

#Print sentence in all caps using upper()

print(sentence.upper().replace("!"," ")) #this one was fun to figure out

#Print sentence in reverse

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."[::-1] #I had to search for a solution in this link https://www.w3schools.com/python/python_howto_reverse_string.asp

print(sentence.replace("!"," "))
