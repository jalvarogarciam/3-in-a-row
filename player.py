from cell import Cell
from board import Board


class Player:
    '''
    A class that represents a player in a 3-in-a-row game
    '''

    @property
    def symbol(self): return self.__symbol
    @property
    def name(self): return self.__name

    def __init__(self, name:str, symbol:str):
        self.__name = name
        self.__symbol = symbol

    def __str__(self)->str: return self.name
    def __repr__(self)->str: return str(self)

    def play(self, board:Board, row:int, col:int)->bool:
        '''
        Places the player's symbol in the cell at the given row and column
        Returns True if the symbol is placed successfully, False otherwise
        '''
        if self.symbol == Cell.CROSS: return board.cross(row, col)
        else:                         return board.circle(row, col)






            
        

    