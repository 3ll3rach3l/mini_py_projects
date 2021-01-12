def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that's not filled yet
    #return row, col tuple (or (None,None) if there is none)

    for r in range(9): # nine rows
        for c in range(9):
            if puzzle[r][c] == -1:
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

    #now we want to get where the 3x3 square starts
    #and iterate over the 3 values in the row/col
    row_start = (row // 3) * 3 # double slashes will round down. we are multiplying by 3 to get index
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    #if we get here, these checks pass
    return True


    
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
    
    #step 2: if there is aplace to put a nu, then make a guess between 1 and 9
    for guess in range(1, 10):
        #step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            #step 3.1: if this is valid, the place that guess on puzzle
            puzzle[row][col] = guess #this mutates the array
            #now recurse using this puzzle
            #step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
        
        #step 5: if not valid OR if our guess does not solve the puzzle, then we 
        #need to backtrack and try a new number
        puzzle[row][col] = -1 #reset the guess
    #step 6: if none of the numbers we try work, the puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    print(solve_sudoku(example_board))
    print(example_board)