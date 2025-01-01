from cell import Cell



class Board:
    '''
    A class that represents a 3x3 board for a 3-in-a-row game
    '''

    @property
    def grid(self): return tuple([tuple(row) for row in self.__grid])
    @property
    def dim(self): return self.__dim

    def __init__(self):
        self.__dim = 3
        self.__grid: tuple[tuple[Cell]] = [
            [Cell() for _ in range(self.dim)] for _ in range(self.dim)
        ]

    def __call__(self, row:int, col:int)->Cell:
        '''
        Returns the cell at the given row and column
        '''
        try: return self.__grid[row][col]
        except IndexError: raise ValueError("Invalid row or column")
    
    def __iter__(self): return iter(self.grid)
    

    
    def circle(self, row:int, col:int)->bool:
        '''
        Places a circle in the cell at the given row and column
        Returns True if the circle is placed successfully, False otherwise
        '''
        return self(row,col).circle()
    

    def cross(self, row:int, col:int)->bool:
        '''
        Places a cross in the cell at the given row and column
        Returns True if the cross is placed successfully, False otherwise
        '''
        return self(row,col).cross()
    
    def free_cells(self)->list[tuple[int]]:
        '''
        Returns a list of tuples containing the row and column of the free cells
        '''
        return [(i,j) for i in range(self.dim) for j in range(self.dim) if self(i,j).empty()]

    def __ways(self)->tuple[tuple[Cell]]:
        '''
        Returns a tuple of all the ways to win the game
        '''
        if self.dim == None:return # if nrows != ncols, the method will not work

        ways: list[tuple[str]] = []

        for i in range(self.dim): # rows and columns
            ways.append(tuple([self(i,j) for j in range(self.dim)])) # rows
            ways.append(tuple([self(j,i) for j in range(self.dim)])) # columns
        # diagonals
        ways.append(tuple([self(i,i) for i in range(self.dim)]))
        ways.append(tuple([self(i,self.dim-1-i) for i in range(self.dim)]))
    
        return tuple(ways)

    def winner(self)->str:
        '''
        Returns the winner of the game ('x' or 'o') if there is one, otherwise returns '-'
        '''
        for way in self.__ways():
            if all( cell.circled() for cell in way): return Cell.CIRCLE
            if all( cell.crossed() for cell in way): return Cell.CROSS
        return Cell.EMPTY
    
    def end(self)->bool:
        '''
        Returns True if the game has ended, False otherwise
        '''
        if self.winner() != Cell.EMPTY : return True 
        else : return self.free_cells() == []

    def __str__(self)->str: 
        return '\n'.join([' '.join([str(c) for c in row]) for row in self.__grid])
    def __repr__(self)->str: return str(self)



