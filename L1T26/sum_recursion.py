'''In a file called sum_recursion, create:
    - a function that takes a list of integers and an integer as 2 arguments. The integer 
    will represent an index point.
    - This function needs to add the sum of all the numbers in the list up until and 
    including the given index point by making use of recursion and no loops.
Examples of input and output:
adding_up_to([1, 4, 5, 3, 12, 16], 4)
=> 25
=> adding the number all the way up to index 4 (1 + 4 + 5 + 3 + 12)
adding_up_to([4, 3, 1, 5], 1)
=> 7
=> adding the number all the way up to index 1 (4 + 3)'''

# function that takes a list of integers and an integer as 2 arguments

def adding_up_to(int_list, index):
  if index == 0:
    return int_list[0]
  else:
    return int_list[index] + adding_up_to(int_list, index - 1)

# given examples to compute
example = adding_up_to([1, 4, 5, 3, 12, 16], 4)
print(example)

example = adding_up_to([4, 3, 1, 5], 1)
print(example)
