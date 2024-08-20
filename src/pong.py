import random
from tkinter import *


def generate_pastel_color():
    r = random.randint(150, 255)
    g = random.randint(150, 255)
    b = random.randint(150, 255)
    return f'#{r:02x}{g:02x}{b:02x}'


def get_random_dark_color():
    dark_colors = ['#00b1ed', '#15c702',
                   '#01da78', '#65028c', '#c70215', '#ed00b1']
    return random.choice(dark_colors)


tk = Tk()
tk.title("PONG COM TKINTER")
tk.resizable(0, 0)

bg_color = generate_pastel_color()
ball_color = get_random_dark_color()
bar_color = generate_pastel_color()

tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1000, height=800, bd=0, highlightthickness=0)
tk.iconbitmap('image\icon.ico')
canvas.configure(bg=bg_color)
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, bar, color):
        self.canvas = canvas
        self.bar = bar
        self.id = canvas.create_oval(1, 1, 20, 20, fill=color)
        self.canvas.move(self.id, 550, 250)
        start = [-6, -5, -4, 4, 5, 6]
        random.shuffle(start)
        self.x = start[0]
        self.y = -6
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_bar(self, position):
        bar_position = self.canvas.coords(self.bar.id)
        return (position[2] >= bar_position[0] and position[0] <= bar_position[2] and
                position[3] >= bar_position[1] and position[3] <= bar_position[3])

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        # Colisão nas bordas do eixo Y
        if position[1] <= 0:
            self.y = 6
        if position[3] >= self.canvas_height:
            self.hit_bottom = True
            self.show_game_over()

        # Colisão nas bordas do eixo X
        if position[0] <= 0:
            self.x = 6
        if position[2] >= self.canvas_width:
            self.x = -6
        if self.hit_bar(position):
            self.y = -6

    def show_game_over(self):
        x_center = self.canvas_width / 2
        y_center = self.canvas_height / 2

        canvas.create_rectangle(
            x_center - 150, y_center - 50, x_center + 150, y_center + 50, fill="black")
        canvas.create_text(
            x_center, y_center, text='GAME OVER', font=("Segoe UI", 30), fill="white")


class Bar:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 160, 8, fill=color)
        self.canvas.move(self.id, 500, 500)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        position = self.canvas.coords(self.id)
        if position[0] <= 0 or position[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -6

    def turn_right(self, event):
        self.x = 6


bar = Bar(canvas, bar_color)
ball = Ball(canvas, bar, ball_color)


def game_loop():
    if not ball.hit_bottom:
        bar.draw()
        ball.draw()
    tk.after(13, game_loop)  # aproxima de 75 fps


game_loop()
tk.mainloop()
