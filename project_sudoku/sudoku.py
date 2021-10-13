from math import floor


def find_next_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col]== -1:
                return row, col
    
    return None, None


def is_valid_guess(puzzle, row, col, guess):
    
    if guess in puzzle[row]:
        return False
    
    col_values = [puzzle[i][col] for i in range(9)]

    if guess in col_values:
        return False

    row_start = floor(row / 3)*3
    col_start = floor(col/3)*3

    for r in range(row_start, row_start+3):
        for c in range(col_start,col_start+3):
            if guess == puzzle[r][c]:
                return False

    return True


def solve_sudoku(puzzle):

    row, column = find_next_empty(puzzle)

    if row == None:
        return True

    for guess in range(1,10):

        if is_valid_guess(puzzle,row,column,guess):
            puzzle[row][column]=guess
            
            if solve_sudoku(puzzle):
                return True
    
        puzzle[row][column] = -1

    return False
