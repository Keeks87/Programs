def print_values_of(dictionary, keys):
    for k in keys: # changed key to k (KeyError)
        print(dictionary[k])

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"} # I changed the 'd'oh' to "d'oh" (SyntaxError)

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) # I added [] to the code (TypeError)

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

