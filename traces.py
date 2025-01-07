from game import Game
from cell import Cell
from trace import Trace
from threading import Thread



class Traces:
    '''
    A class that represents all the possible traces of a 3-in-a-row game
    '''

    def __init__(self):
        self.__root =      Trace() # The initial trace of the game
        self.__traces =         [] # All the possible traces of the game from the initial trace
        self.__winning_traces = [] # Those traces that lead to a win
        self.__draw_traces =    [] # Those traces that lead to a draw
    
    def __getitem__(self, symbol:str)->list[Trace]:
        '''
        Returns all the traces of the given symbol
        '''
        try: return self.__traces[symbol]
        except KeyError: raise ValueError(f"Invalid symbol, only '{Cell.CIRCLE}' or '{Cell.CROSS}' are allowed")

    def __clear(self):
        '''
        Clears all the traces
        '''
        self.__traces.clear()
        self.__winning_traces.clear()
        self.__draw_traces.clear()

    def __calculate(self, game:Game):
        '''
        Calculates all the possible traces of the given game
        '''
        if not game.end(): # If the game is not over
            for move in game.board.empty_cells(): # For each empty cell
                new_game = Game(game) # Create a new game
                new_game.play(*move.index())
                new_trace = Trace(game.trace)
                new_trace.calculate()
        

    def calculate(self, game:Game=Game()):
        '''
        Calculates all the possible traces of the given game
        '''
        self.__clear()

        self.__trace = game.trace
        self.__calculate(game)



        
        
        
