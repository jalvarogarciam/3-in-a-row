from cell import Cell



class Board:
    '''
    A class that represents a 3x3 board for a 3-in-a-row game
    '''

    @property
    def grid(self)->tuple[tuple[Cell]]: 
        return tuple([tuple([Cell(cell) for cell in row ]) for row in self.__grid])
    @property
    def dim(self)->int: return self.__dim

    def __init__(self, *args):
        '''
        Creates a dim x dim board, where dim is specified in the args (default is 3)
        Creates a copy of the board if another board is passed as an argument
        Initially, all cells are empty.
        '''
        if len(args) == 1 and type(args[0]) == Board:
            self.__dim = args[0].dim
            self.__grid = args[0].__grid.copy()

        else:
            self.__dim = 3 if len(args) == 0 or type(args[0]) != int else args[0]
            # create a grid of empty cells
            self.__grid: tuple[tuple[Cell]] = [
                [Cell() for _ in range(self.dim)] for _ in range(self.dim)
            ]



    def __call__(self, row:int, col:int)->Cell:
        '''
        Returns a copy of the cell at the given row and column
        '''
        try: return Cell(self.__grid[row][col]) # return a copy of the cell
        except IndexError: raise ValueError("Invalid row or column")
    
    def __iter__(self): return iter(self.grid)
        
    def circle(self, row:int, col:int)->bool:
        '''
        Places a circle in the cell at the given row and column
        Returns True if the circle is placed successfully, False otherwise
        '''
        try: return self.__grid[row][col].circle()
        except IndexError: return False
    

    def cross(self, row:int, col:int)->bool:
        '''
        Places a cross in the cell at the given row and column
        Returns True if the cross is placed successfully, False otherwise
        '''
        try: return self.__grid[row][col].cross()
        except IndexError: return False
    
    def empty_cells(self)->tuple[tuple[int]]:
        '''
        Returns a tuple of tuples containing the row and column of the free cells
        '''
        return tuple([(i,j) for i in range(self.dim) for j in range(self.dim) if self(i,j).empty()])

    def __str__(self)->str: 
        return '\n'.join([' '.join([str(c) for c in row]) for row in self.__grid])
    def __repr__(self)->str: return str(self)



