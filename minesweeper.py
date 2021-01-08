import random
import re

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

        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] #2d board

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) #return a random int N such that a <= N <= b
            row = loc // self.dim_size ##how many times does my dim size go into whatever location i've chose
            col = loc % self.dim_size

            if board[row][col] == '*': #if there is a bomb already planted, continue
                continue

            board[row][col] = '*'
            bombs_planted += 1
        return board

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

    def dig(self, row, col):
        self.dug.add((row, col)) #keeps track of where we dug

        if self.board[row][col] == '*': #return false if we hit a bomb
            return False 
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row-1), min(self.dim_size - 1, row+1)+1): 
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1): 
                if (r, c) in self.dug:
                    continue #don't dig where you've already dug
                self.dig(r, c)
        #if our initial dig didn't hit a bomb, we shoudn't hit a bomb here
        return True

    def __str__(self):
         #if you call print on the obj, it'll print what the func returns
         # return a string that shows the board to the player
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] #creates a 2D board
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug: #if a user already dug here
                    visible_board[row][col] = str(self.board[row][col]) #show the user the value
                else:
                    visible_board[row][col] = ' '
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
    


def play(dim_size=10, num_bombs=10):
    #step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    #step 2: show the user the board and ask where they want to dig
    #step 3a: if location is a bomb, show game over msg
    #step 3b: if location is not a bomb, dig recursively until ea square is at least
    #   next to a bomb
    #step 4: repeat steps 2 - 3 until there are no more places to dig -> victory
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("where would you like to dig? Input as row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        
        safe = board.dig(row, col) #we know this will return True if we dug successfully or False if not
        if not safe:
            break #game over
    
    if safe:
        print("CONGRATULATIONS! YOU SURVIVED")
    else:
        print("Sorry, game over :( ")
        #reveal whole board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)] #double for loop to show all the spots on the board
        print(board)

if __name__ == '__main__':
    play()
