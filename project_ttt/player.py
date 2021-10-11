import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        return random.choice(game.available_moves())
        
    

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        valid_tile = False
        tile_value = None
        
        while not valid_tile:
            chosen_tile = input(f'{self.letter}\'s turn.\nChoose move (0-8): ')

            try:
                tile_value = int(chosen_tile)
                if tile_value not in game.available_moves():
                    raise ValueError
                valid_tile = True
            except ValueError:
                print("Invalid move! Try again.")

        return tile_value