class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to rep 3x3 board
        self.current_winner = None #keep track of winner

    def print_board(self):
        #this is defining each row, and indexing into our length 9 list. i*3:(i+1)*3 means which group of 3 spaces are we choosing?
        for row in [self.board[i*3:(i +1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod #static bc it doesn't relate to any specific board
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to which box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] #tell me which indices are in the rows for each row
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
       '''
        moves = []
        for (i, spot) in enumerate(self.board):
            #['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves
        '''
        #list comprehension below is condensed version of above
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_square(self,):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        #if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board(square) == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter): #winner if 3 in a row anywhere. we have to check all of these 
        #check the row
        row_idx = square // 3 #this will round down
        row = self.board[row_idx*3 : (row_idx + 1) * 3] #given the row index, get the row
        if all([spot == letter for spot in row]):
            return True
        #check column
        col_idx = square % 3
        column = [self.board[col_idx+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        #check diagonals --squares must be an even number to win
        if square % == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left
            if all([spot == letter for spot in diagonal2]):
                return True

        return False




def play(game, x_player, o_player, print_game=True):
    #returns the winner of the game or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    #iterate while the game still has empty squares -- we dont have to worry about winner
    #bc we'll just return that which breaks the loop
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        #let's define a function to make a move! (see make_move)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #just empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
            '''
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
            '''
            if print_game:
                print('It\s a tie!')


