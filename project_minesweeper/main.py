import random
import math
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()


        self.dug = set()

  
    def make_new_board(self):

        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bomb_count = 0

        while bomb_count < self.num_bombs:
            location = random.randint(0, (self.dim_size**2)-1)
            row = math.floor(location/self.dim_size)
            col = location%self.dim_size

            if board[row][col] == '*':
                continue
            else:
                board[row][col] = '*'
                bomb_count += 1
        
        return board

    
    def assign_values_to_board(self):

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == '*':
                    continue
                self.board[row][col] = self.get_num_area_bombs(row,col)

    
    def get_num_area_bombs(self, row, col):

        area_bombs = 0

        for r in range(max(0,row-1),min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1,col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    area_bombs+=1
        
        return area_bombs


    def dig(self,row, col):

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        elif self.board[row][col] == 0:
            for r in range(max(0,row-1),min(self.dim_size-1,row+1)+1):
                for c in range(max(0,col-1), min(self.dim_size-1,row+1)+1):
                    if (r,c) in self.dug:
                        continue
                    else:
                        self.dig(r,c)

        return True

    def __str__(self):
        
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # Copied formatting from Kylie Ying's github at https://github.com/kying18/minesweeper/blob/main/minesweeper.py

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
    
    board = Board(dim_size, num_bombs)

    safe =True

    while len(board.dug)<(dim_size**2-num_bombs):
        
        print(board)
        
        user_input = re.split(',(\\s)*',input("Choose a field to dig! Input as row,col: "))

        row = int(user_input[0])
        col = int(user_input[-1])

        if row<0 or row>=dim_size or col<0 or col>= dim_size:
            print('Invalid field! Try again!')
            continue
        elif (row,col) in board.dug:
            print('You cannot dig there again!')
            continue
        
        if not board.dig(row, col):
            safe = False
            break
    
    if safe:
        print('Congratulations! You won the game!')
    else:
        print('BOOOOOOOOM!!!!\nSorry, you lost!\n')

        board.dug = [(r,c) for r in range(dim_size) for c in range(dim_size)]
        print(board)



if __name__ == '__main__':
    play()