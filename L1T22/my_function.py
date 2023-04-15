#Create your own function that prints all the days of the week.
#Create your own function that takes in a sentence and replaces every second word with
#the word “Hello”.

# function that prints all the days of the week
def print_days():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        print(day)

# function that takes in a sentence and replaces every second word with the word “Hello”
def replace_words(sentence):
    # split sentence into a list of words
    words = sentence.split()
    # loop through the list of words starting from the second word (index 1)
    for i in range(1, len(words), 2):
    # replace every second word with "Hello"
        words[i] = 'Hello'
    # join the list of words back into a sentence
    new_sentence = ' '.join(words)
    # return the new sentence
    return new_sentence

#collect sentence from the user
sentence = input("Enter a sentence: ")
print_days()
print(replace_words(sentence))