from player import Player
from board import Board
from game import Game

class SuperPlayer(Player):
    '''
    A class that represents an invencible player in a x-in-a-row game
    '''

    def __init__(self, name:str, symbol:str):
        super().__init__(name, symbol)
        self.__better_move = []
        self.__draw = False

    def play(self, board:Board, row:int, col:int)->bool:
        '''
        Places the player's symbol in the cell at the given row and column
        Returns True if the symbol is placed successfully, False otherwise
        '''
        # Makes a mental game with the current board
        ''' mental_game = Game("playerx", "playero", self.symbol)
        mental_game.board = board

        self.__better_move(mental_game)
        super().play(board, better_move[0], better_move[1])'''
        ...
    

    def __better_move(self, game:Game):
        '''
        Calculates the best move for the current player
        '''
        
        # If the game is over, return
        if game.end(): return

        # If the game is in the first turn, play in the center
        if len(game.moves) == 0:
            self.__better_move = [game.board.dim//2, game.board.dim//2]
            return
        
        # If the game is in the second turn, play in a corner
        elif len(game.moves) == 1:
            corners = [(0,0), (0, game.board.dim-1), (game.board.dim-1, 0), (game.board.dim-1, game.board.dim-1)]
            for corner in corners:
                if corner in game.board.empty_cells():
                    self.__better_move = corner
                    return
            
