from cell import Cell
from board import Board
from player import Player
from move import Move
#from trace import Trace

class Game:
    '''
    A class that represents a 3-in-a-row game
    '''

    @property
    def board(self)->Board: return Board(self.__board)
    @board.setter
    def board(self, other:Board): self.__board = Board(other)
    @property
    def playero(self)->Player: return self.__playero
    @property
    def playerx(self)->Player: return self.__playerx
    @property
    def current_player(self)->Player: return self.__current_player
    @property
    def turn(self)->str: return self.current_player.symbol
    @property
    def trace(self)->tuple: return self.__trace.copy()
    @property
    def log(self)->str: return '#'.join(str(move) for move in self.trace)

    def __init__(self, playerx:str=None, playero:str=None, first_player:str=None):
        '''
        Creates a new game with two players.
        If the first_player (x/o) is not specified, playerx starts first.
        '''
        if not playerx: playerx = 'Player 1'
        if not playero: playero = 'Player 2'
        self.__board:Player = Board()
        self.__playerx:Player = Player(playerx, Cell.CROSS)
        self.__playero:Player = Player(playero, Cell.CIRCLE)
        self.__trace: Trace = Trace()

        if not first_player: self.__current_player = self.__playerx
        else:
            if first_player.lower() in (Cell.CROSS, Cell.CIRCLE):
                self.__current_player = self.__playerx if first_player == Cell.CROSS else self.__playero
            else: raise ValueError("Invalid first player")
        

    def __str__(self)->str: return f"{self.board}\n{self.current_player}'s turn"
    def __repr__(self)->str: return str(self)
    
    def play(self, row:int, col:int)->bool:
        '''
        Places the player's symbol in the cell at the given row and column
        Returns True if the symbol is placed successfully, False otherwise
        '''
        if self.end(): return False
        
        if self.__current_player.play(self.__board, row, col): # if the move is valid
            self.__log_move(row, col) # log the move
            self.__next_player() # change the current player
            return True
        return False

    def end(self)->bool:
        '''
        Returns True if the game is over, False otherwise
        '''
        return self.winner() != None or len(self.board.empty_cells()) == 0

    def winner(self)->str:
        '''
        Returns the name of the winner, or None if there is no winner
        '''
        ways: list[tuple[Cell]] = []

        for i in range(self.board.dim): # rows and columns
            ways.append(tuple([self.board(i,j) for j in range(self.board.dim)])) # rows
            ways.append(tuple([self.board(j,i) for j in range(self.board.dim)])) # columns
        # diagonals
        ways.append(tuple([self.board(i,i) for i in range(self.board.dim)]))
        ways.append(tuple([self.board(i,self.board.dim-1-i) for i in range(self.board.dim)]))

        for way in ways: 

            if self.__winner_way(way):
                return way[0].symbol
        return None
    

    def __winner_way(self, way:tuple[Cell])->bool:
        '''
        Returns True if the given way is a winning way, False otherwise
        '''
        return all( cell.circled() for cell in way) or all( cell.crossed() for cell in way)
    
    def copy(self)->'Game':
        '''
        Returns a deepcopy of the game
        '''
        new_game = Game()
        
        new_game.__board = Board(self.__board) # copy the board
        new_game.__trace = self.__trace.copy() # copy the log
        # copy the players
        new_game.__playerx = Player(self.__playerx.name, self.__playerx.symbol)
        new_game.__playero = Player(self.__playero.name, self.__playero.symbol)
        # copy the current player
        if self.__current_player is self.__playerx: 
            new_game.__current_player = new_game.__playerx
        else: new_game.__current_player = new_game.__playero

        return new_game    

    def __log_move(self, row:int, col:int):
        '''
        Logs the move made by the current player
        '''
        self.__trace.append(Move(row, col, self.current_player.symbol))
    
    def __next_player(self):
        '''
        Changes the current player to the other player
        '''
        if self.__current_player is self.__playerx: 
            self.__current_player = self.__playero
        else: 
            self.__current_player = self.__playerx