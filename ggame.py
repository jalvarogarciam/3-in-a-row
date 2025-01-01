from board import Board, Cell
from random import choice
import flet as ft
# Antes
#from websockets.legacy.server import serve

# Después
from websockets import serve





class VisualCell(ft.Button):
    def __init__(self, cell:Cell, button_clicked):
        super().__init__()
        self.cell=cell
        self.text = ' ' if self.cell.empty() else self.cell.symbol
        self.expand = False
        self.on_click = button_clicked
        self.bgcolor = ft.colors.WHITE
        self.color = ft.colors.BLACK
        self.width = self.height = 60

    def update(self):
        self.text = self.data = self.cell.symbol
        super().update()

    def cross(self):
        if self.cell.cross():
            self.update()
            return True
        return False
    def circle(self):
        if self.cell.circle():
            self.update()
            return True
        return False



class Panel(ft.Column):
    
    def __init__(self):
        super().__init__()
        self.board = Board()

        self.buttons = [
            [VisualCell( cell , button_clicked=self.button_clicked) for cell in row] for row in self.board
        ]

        self.controls = [ ft.Row(controls=row) for row in self.buttons ]


        self.turn = choice([Cell.CROSS, Cell.CIRCLE])


    def button_clicked(self, e):

        if self.turn == Cell.CROSS and e.control.cross():  self.turn = Cell.CIRCLE
        elif e.control.circle(): self.turn = Cell.CROSS

        self.update()
        







def main(page: ft.Page):
    page.title = "3 in a Row"
    # create application instance
    board = Panel()

    page.window.width = board.width  # Ajusta el ancho de la ventana
    page.window.height = board.height  # Ajusta la altura de la ventana


    # add application's root control to the page
    page.add(ft.Row([board], alignment=ft.MainAxisAlignment.CENTER,))


ft.app(target=main)