#Create a function that takes a grid of # and -, where each hash (#) represents a
#mine and each dash (-) represents a mine-free spot.
#Return a grid, where each dash is replaced by a digit, indicating the number of
#mines immediately adjacent to the spot i.e. (horizontally, vertically, and diagonally).
#Example of an input:
#[ ["-", "-", "-", "#", "#"],
#["-", "#", "-", "-", "-"],
#["-", "-", "#", "-", "-"],
#["-", "#", "#", "-", "-"],
#["-", "-", "-", "-", "-"] ]
#Example of the expected output:
#[ ["1", "1", "2", "#", "#"],
#["1", "#", "3", "3", "2"],
#["2", "4", "#", "2", "0"],
#["1", "#", "#", "2", "0"],
#["1", "2", "2", "1", "0"] ]
#Here is a tip. When checking adjacent positions to a specific position in the grid,
#the following table might assist you in determining adjacent indexes:
#Also ensure that when checking adjacent positions in the grid that you take into 
#account that on the edges of the grid, you may go out of bounds.
#Lastly, you could make use of the enumerate function in Python to keep track of
#the index points and values without having to create a count variable and
#explicitly iterate the count variable to keep track of the current row or column
#index.


grid = [['.', '.', '.', '#'],
        ['.', '#', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.']]

def minesweeper(grid):
    n = len(grid)
    m = len(grid[0])
    # Create a 2D list with the same size as the input grid and fill it with zeros
    output = [[0 for _ in range(m)] for _ in range(n)]
    for i, row in enumerate(grid):
        for j, spot in enumerate(row):
            if spot == "#":
                # If the current spot is a mine, set the corresponding spot in the output grid to be a "#"
                output[i][j] = "#"
                continue
            for x in range(-1, 2):
                for y in range(-1, 2):
                    # Check if the adjacent spot is within the boundaries of the grid
                    if i+x < 0 or i+x >= n or j+y < 0 or j+y >= m:
                        continue
                    if grid[i+x][j+y] == "#":
                        # If the adjacent spot is a mine, increment the corresponding spot in the output grid by 1
                        output[i][j] += 1
    return output

output = minesweeper(grid)

for row in output:
    for cell in row:
        print(cell, end=' ')
    print()

