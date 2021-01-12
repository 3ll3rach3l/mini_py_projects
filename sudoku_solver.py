def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that's not filled yet
    #return row, col tuple (or (None,None) if there is none)

    for r in range(9): # nine rows
        for c in range(9):
            if puzzle[r][r] == -1:
                return r, c
    return None, None #if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    #determines whether the guess at row/col is valid guess according to sudoku rules
    
    #checking rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #checking columns
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    
    #let's use list comprehension instead
    col_vals= [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
def solve_sudoku(puzzle):
    #soluve using backtracking!
    #our puzzle is a list of lists, where ea innter list is a row in our puzzle
    #return whether a solution exists
    #mutates puzzle to be the solution

    #step 1: choose somwhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #step 1.1: if there's nowhere left, then we're done
    if row is None:
        return True
    