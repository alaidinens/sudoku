import random

def solve_sudoku(puzzle):
  # Find the next empty cell
  for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
      if puzzle[i][j] == 0:
        # Try filling the empty cell with a number from 1 to 9
        for k in range(1, 10):
          # Check if the number is valid for the current cell
          if is_valid(puzzle, i, j, k):
            # Fill the cell with the number and recursively try to solve the puzzle
            puzzle[i][j] = k
            if solve_sudoku(puzzle):
              return True
        # If none of the numbers worked, backtrack and try a different number
        puzzle[i][j] = 0
        return False
  # If the puzzle is complete, return True
  return True

def is_valid(puzzle, row, col, num):
  # Check if the number is already in the row
  if num in puzzle[row]:
    return False
  # Check if the number is already in the column
  for i in range(len(puzzle)):
    if puzzle[i][col] == num:
      return False
  # Check if the number is already in the 3x3 block
  start_row = row - row % 3
  start_col = col - col % 3
  for i in range(3):
    for j in range(3):
      if puzzle[start_row + i][start_col + j] == num:
        return False
  # The number is valid
  return True

# Generate a 9x9 grid of empty cells
puzzle = [[0 for j in range(9)] for i in range(9)]

# Write 20 random numbers into the cells, without repeating any numbers in the same row or column
for i in range(20):
  while True:
    row = random.randint(0, 8)
    col = random.randint(0, 8)
    num = random.randint(1, 9)
    if num not in puzzle[row] and num not in [puzzle[i][col] for i in range(9)]:
      puzzle[row][col] = num
      break

# Solve the puzzle 
solve_sudoku(puzzle)


#for row in puzzle:
 #-= print(row)

