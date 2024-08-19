from tkinter import *
import random
import time

tk = Tk()
tk.title("JOGO COM TKINTER")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1200, height=800, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 550, 250)
        start = [-3, -2, -1, 0, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        # colisão nas bordas do eixo Y
        if position[1] <= 0:
            self.y = 3
        if position[3] >= self.canvas_height:
            self.y = -3
        # colisão nas bordas do eixo X
        if position[0] <= 0:
            self.x = 3
        if position[2] >= self.canvas_width:
            self.x = -3


class Bar:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 200, 10, fill=color)
        self.canvas.move(self.id, 500, 200)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        position = self.canvas.coords(self.id)

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2


ball = Ball(canvas, '#21a3ff')
bar = Bar(canvas, '#ffc2c2')

while True:
    bar.draw()
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
