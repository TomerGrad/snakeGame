"""
Classic snake game.
(c) Tomer Grad plain games package.
Play with fun and care!
"""

import turtle as trt
from time import sleep
from random import randint
from tkinter.simpledialog import SimpleDialog


def set_food(f, lim):
    f.goto(randint(-lim, lim), randint(-lim, lim))

def score_update(adj, s):
    adj.undo()
    adj.write(f"Score: {s}", font=('Ariel', 12, 'bold'))

def in_border(head, lim):
    return abs(head.xcor()) < lim and abs(head.ycor()) < lim

def eat(head, f):
    step = getattr(head, 'step')
    return abs(head.xcor() - f.xcor()) < step and abs(head.ycor() - f.ycor()) < step

def turn(head, direction):
    if int(direction // 10 % 2) ^ int(head.heading() // 10 % 2):
        head.setheading(direction)

def game(head, board, food, caption, step, speed=0.2):
    score = 0
    limit = int(step * 19)
    segments = []
    snake_draw = snake.clone()
    snake_draw.hideturtle()
    writer.write(f"Score: {score}", font=('Ariel', 12, 'bold'))

    while in_border(head, limit) and head.pos() not in segments:
        segments.insert(0, head.pos())
        segments = segments[:score]
        head.fd(step)
        snake_draw.clearstamps()
        for seg in segments:
            snake_draw.goto(*seg)
            snake_draw.stamp()
        if eat(head, food):
            score += 1
            score_update(caption, score)
            set_food(food, limit - step)
        board.update()
        sleep(speed)
    trt.done()


screen = trt.Screen()
writer = trt.Turtle()
snake = trt.Turtle('square')
fruit = trt.Turtle('circle')

screen.bgcolor("dark blue")
screen.setup(520, 520)
screen.tracer(False)
screen.title('My Python Snake')

stepsize = screen.window_height() // 40

writer.color('white')
writer.hideturtle()
writer.up()

fruit.color('red')
fruit.shapesize(0.5)
fruit.up()

snake.color('light green')
snake.up()
snake.shapesize(0.5)
snake.step = stepsize

writer.goto(-stepsize*19, stepsize*18)
set_food(fruit, stepsize*19)
screen.update()

screen.onkey(lambda: turn(snake, 0), 'Right')
screen.onkey(lambda: turn(snake, 180), 'Left')
screen.onkey(lambda: turn(snake, 90), 'Up')
screen.onkey(lambda: turn(snake, 270), 'Down')
screen.listen()

if __name__ == '__main__':
    # TODO difficult/speed choicer
    # s = SimpleDialog(screen.cv.master, buttons=['easy', 'medium', 'hard'], title='mode')
    game(snake, screen, fruit, writer, stepsize)
