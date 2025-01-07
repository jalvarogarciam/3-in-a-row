from board import Board
from cell import Cell
from game import Game
from random import choice
import flet as ft


DISPLAY_WIDTH = 1920
DISPLAY_HEIGHT = 1080

PANEL_DIM = DISPLAY_HEIGHT*0.3

BOARD_DIM = (PANEL_DIM//3)*3
CELL_DIM = BOARD_DIM*0.25



class VisualCell(ft.Container):
    images = { Cell.CROSS: 'assets/iconx.png', Cell.CIRCLE: 'assets/icono.png'}
    def __init__(self, row:int, col:int, button_clicked):
        super().__init__()
        self.row = row
        self.col = col

        self.on_click=button_clicked

        self.width = self.height = CELL_DIM
        self.alignment=ft.alignment.center
        self.border_radius=5

        self.on_click = button_clicked
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.BLACK


    def __fill(self, symbol:str):
        self.content=ft.Image(
            self.images[symbol],   
            width=self.width*0.6,
            height=self.height*0.6,
        )
        self.update()

    def index(self)->tuple[int]: return self.row, self.col
    def cross(self): self.__fill(Cell.CROSS)
    def circle(self): self.__fill(Cell.CIRCLE)



class VisualBoard(ft.Container):
    
    def __init__(self):
        super().__init__()
        player1 = choice(["Player 1", "Player 2"])
        player2 = "Player 2" if player1 == "Player 1" else "Player 1"
        self.game = Game(playerx=player1, playero=player2)

        self.width = self.height = BOARD_DIM
        
        self.buttons:list[list[VisualCell]] = [
            [VisualCell(i, j, self.button_clicked) for j in range(self.game.board.dim)] 
            for i in range(self.game.board.dim)
        ]

        self.grid = ft.Column(
            controls = [ 
                ft.Row(
                    controls=row,
                    alignment=ft.MainAxisAlignment.CENTER,
                    width=self.width,
                ) for row in self.buttons 
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            height=self.height
        )
    
        self.content = self.grid
        self. margin=10
        self.padding=10
        self.alignment=ft.alignment.center
        self.bgcolor=ft.Colors.BLACK

        self.border_radius=10

    def __update_cells(self):
        for row in self.buttons:
            for button in row:
                button.update()

    def update(self):
        self.__update_cells()
        super().update()

    def button_clicked(self, e):
        if self.game.end(): return

        index = e.control.index()
        self.game.play(*index)
        if self.game.board(*index).symbol == Cell.CROSS:
            self.buttons[index[0]][index[1]].cross()
        else:
            self.buttons[index[0]][index[1]].circle()
        
        self.update()
        




def main(page: ft.Page):
    page.title = "3 in a Row"
    board = VisualBoard()
    page.window.width = board.width+100  # Ajusta el ancho de la ventana
    page.window.height = board.height+100  # Ajusta la altura de la ventana
    page.window.resizable = False  # No permite que la ventana se redimensione
    page.padding = 10  # Añade un relleno de 10 píxeles alrededor de la ventana
    page.update()  # Actualiza la ventana

    # add application's root control to the page
    page.add(ft.Row([board], alignment=ft.MainAxisAlignment.CENTER,))


ft.app(target=main)