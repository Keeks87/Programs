'''Create a file called search_replace.py. Here, create a program that
implements a search and replace function recursively. Your program
should allow a user to enter a string, a substring they wish to find and
another string with which they wish to replace the found substring.
The output of your program should be similar to the output given below:
Please enter a string: Hello world
Please enter the substring you wish to find: llo
Please enter a string to replace the given substring: @@
Your new string is: he@@ world'''

def search_and_replace(string, substring, replacement):
  # Base case: return an empty string if the input string is empty
  if len(string) == 0:
    return ""
  # If the first part of the string matches the substring, replace it
  elif string[:len(substring)] == substring:
    return replacement + search_and_replace(string[len(substring):], substring, replacement)
  # If the first part of the string does not match the substring, keep the first character and
  # perform the search and replace on the rest of the string
  else:
    return string[0] + search_and_replace(string[1:], substring, replacement)

string = "Hello world"
substring = "llo"
replacement = "@@"
new_string = search_and_replace(string, substring, replacement)
print(f"Your new string is: {new_string}")