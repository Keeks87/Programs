'''In a file called largest_number.py, create:
    - A function that returns the largest number in a list of integers taken as an argument.
    - This needs to be solved recursively without using loops.
Examples of input and output:
largest_number([1, 4, 5, 3])
=> 5
largest_number([3, 1, 6, 8, 2, 4, 5])
=> 8'''

def largest_number(int_list):
  if len(int_list) == 1:
    return int_list[0]
  else:
    return max(int_list[0], largest_number(int_list[1:]))

#Examples of input and output:

example = largest_number([1, 4, 5, 3])
print(example)

example = largest_number([3, 1, 6, 8, 2, 4, 5])
print(example)
