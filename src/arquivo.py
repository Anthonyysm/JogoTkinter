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
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 1
        if position[3] >= self.canvas_height:
            self.y = -1

        



ball = Ball(canvas, '#21a3ff')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.006)

