
class Cell:
    CROSS =  'x'
    CIRCLE = 'o'
    EMPTY =  '-'

    @property
    def symbol(self): return self.__symbol

    def __init__(self, symbol:str=EMPTY):
        self.__symbol = Cell.EMPTY

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

        