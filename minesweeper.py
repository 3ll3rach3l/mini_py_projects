import random

#board obj to represent the game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
    
    #create the board using helper function
    self.board = self.make_new_board() #plant the bombs
    self.assign_value_to_board()

    #init a set to keep track of locations dug up
    #we'll save (row, col) tuples in this set
    self.dug = set()

    def make_new_board(self):

        board = [[None for _ in rang(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) #return a random int N such that a <= N <= b
            row = loc // self.dim_size ##how many times does my dim size go into whatever location i've chose
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'

    def assign_value_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self, row, col):
        #iterate through ea of the neighboring positions and sum num bombs
        #top left: (row-1, col-1)
        #top middle: (row-1, col)
        #top right: (row-1, col+1)
        #left: (row, col-1)
        #right: (row, col+1)
        #bottom left: (row+1, col-1)
        #bottom middle: (row+1, col)
        #bottom right: (row+1, col+1)

        num_neighboring_bombs = 0
        #we use max and min in the range to make sure we aren't going out of bounds/off the board
        for r in range(max(0, row-1), min(self.dim_size - 1, row+1)+1): #for the current row, we're checking above and below
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1): #for current col, we're checking left and right
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
                
        return num_neighboring_bombs






def play(dim_size=10, num_bombs=10):
    #step 1: create the board and plant the bombs
    #step 2: show the user the board and ask where they want to dig
    #step 3a: if location is a bomb, show game over msg
    #step 3b: if location is not a bomb, dig recursively until ea square is at least
    #   next to a bomb
    #step 4: repeat steps 2 - 3 until there are no more places to dig -> victory
