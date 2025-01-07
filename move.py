from cell import Cell

class Move:
    '''
    A class that represents a move in a 3-in-a-row game
    '''
    @property
    def symbol(self)->str: return self.__symbol

    def __init__(self, row:int, col:int, symbol:str):
        '''
        Creates a move with the given row, column and symbol
        '''
        self.__row=row
        self.__col=col
        self.__symbol=symbol
        if symbol not in (Cell.CIRCLE, Cell.CROSS):
            raise ValueError(f"Invalid symbol, only '{Cell.CIRCLE}' or '{Cell.CROSS}' are allowed")
    
    def cross(self)->bool: return self.symbol == Cell.CROSS
    def circle(self)->bool: return self.symbol == Cell.CIRCLE
    def index(self)->tuple[int]: return self.__row, self.__col
    def __eq__(self, other:'Move')->bool: 
        return self.index() == other.index() and self.symbol == other.symbol
    def __ne__(self, other:'Move')->bool: return not self == other

    def __str__(self)->str: return f"{self.symbol}{self.index()}"
    def __repr__(self)->str: return str(self)

    