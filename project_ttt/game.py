import time
from player import HumanPlayer, RandomComputerPlayer



class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves =[]
        for(i, tile) in enumerate(self.board):
            if tile == ' ':
                moves.append(i)
        return moves
        # with list comprehension return [i for i,tile in enumerate(self.board) if tile == ' ']
    
    def make_move(self, tile, letter):
        if self.board[tile] == ' ':
            self.board[tile] = letter
            if self.winner(tile, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, tile, letter):
        #checking if won in a row
        row_index = tile //3
        row = self.board[row_index*3:(row_index+1)*3]       
        if all([tile == letter for tile in row]):
            return True
        
        #checking if won in column
        col_index = tile % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([tile == letter for tile in column]):
            return True

        # checking if won in diagonal
        if tile % 2 == 0:          
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([tile == letter for tile in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([tile == letter for tile in diagonal2]):
                return True

        return False
        

def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()
    
    letter = 'X'

    while len(game.available_moves()) > 0:
        move = o_player.get_move(game) if letter == 'O' else x_player.get_move(game)
        if game.make_move(move, letter):
            if print_game:
                print(letter, f' makes a move to tile {move}\n')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter, ' player wins!')
                return letter
        
            letter = 'O' if letter == 'X' else 'X'
            
    
    if print_game:
        print(f'It\'s a tie')



x_player = HumanPlayer('X')
o_player = RandomComputerPlayer('O')
ttt = TicTacToe()
play(ttt, x_player, o_player, print_game = True)
