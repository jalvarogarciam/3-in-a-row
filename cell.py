
class Cell:
    '''
    A class that represents a cell of the board in a x-in-a-row game
    Initialy, the cell is empty, and it can be filled with a cross or a circle.
    When filled, the cell cannot be changed.
    '''
    CROSS =  'x'
    CIRCLE = 'o'
    EMPTY =  '-'

    @property
    def symbol(self): return self.__symbol

    def __init__(self, other: 'Cell' = None):
        '''
        Creates an empty cell by default, or a cell with the same 
        symbol as the other cell 
        '''
        self.__symbol = Cell.EMPTY if not other else other.__symbol

    def empty(self)->bool:
        '''
        Returns True if the cell is empty, False otherwise
        '''
        return self.__symbol == Cell.EMPTY
    
    def crossed(self)->bool:
        '''
        Returns True if the cell is crossed, False otherwise
        '''
        return self.__symbol == Cell.CROSS
    
    def circled(self)->bool:
        '''
        Returns True if the cell is circled, False otherwise
        '''
        return self.__symbol == Cell.CIRCLE

    def __fill(self, symbol:str):
        '''
        Fills the cell with the given symbol
        Returns True if the cell is filled successfully, False otherwise
        '''
        if not self.empty():
            return False
        if symbol not in (Cell.CROSS, Cell.CIRCLE): 
            raise ValueError(f"Invalid symbol, only '{Cell.CIRCLE}' or '{Cell.CROSS}' are allowed")
        
        self.__symbol = symbol
        return True
                
    def cross(self):
        '''
        Fills the cell with a cross
        Returns True if the cell is filled successfully, False otherwise
        '''
        return self.__fill(Cell.CROSS)
    
    def circle(self):
        '''
        Fills the cell with a circle
        Returns True if the cell is filled successfully, False otherwise
        '''
        return self.__fill(Cell.CIRCLE)
    
    def __str__(self)->str: return self.__symbol
    def __repr__(self)->str: return str(self)

    def __eq__(self, other): return self.__symbol == other
    def __ne__(self, other): return self.__symbol != other

        