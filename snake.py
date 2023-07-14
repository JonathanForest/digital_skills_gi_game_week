# Importing code other people have written
import turtle
import time
import random

sc = turtle.Screen()
sc.title("Snake")
sc.bgcolor("black")
sc.tracer(1)
sc.setup(600, 600)
GRID_SIZE = 20

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake.setx(0)
snake.sety(0)
snake_direction = "up"

body = [snake]

food = turtle.Turtle()
colors = random.choice(['red', 'orange'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.penup()
food.shape(shapes)
food.color(colors)
food.goto(0, GRID_SIZE*5)


# assigning key directions
def goup():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def godown():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def goleft():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


def goright():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def create_new_body_part(x, y):
    body_part = turtle.Turtle()
    body_part.hideturtle()
    body_part.penup()
    body_part.shape("square")
    body_part.color("green")
    body_part.setx(x)
    body_part.sety(y)
    body_part.showturtle()
    return body_part


sc.listen()
sc.onkeypress(goup, "w")
sc.onkeypress(godown, "s")
sc.onkeypress(goleft, "a")
sc.onkeypress(goright, "d")

while True:

    if snake_direction == "up":
        new_part = create_new_body_part(body[0].xcor(), body[0].ycor()+GRID_SIZE)
        body.insert(0, new_part)
    elif snake_direction == "down":
        new_part = create_new_body_part(body[0].xcor(), body[0].ycor()-GRID_SIZE)
        body.insert(0, new_part)
    elif snake_direction == "left":
        new_part = create_new_body_part(body[0].xcor()-GRID_SIZE, body[0].ycor())
        body.insert(0, new_part)
    elif snake_direction == "right":
        new_part = create_new_body_part(body[0].xcor()+GRID_SIZE, body[0].ycor())
        body.insert(0, new_part)

    if body[0].xcor() == food.xcor() and body[0].ycor() == food.ycor():
        food.setx(random.randrange(-200,200,GRID_SIZE))
        food.sety(random.randrange(-200,200,GRID_SIZE))
    else:
        body_part_to_remove = body.pop()
        body_part_to_remove.reset()
        body_part_to_remove.clear()
        del body_part_to_remove

    for body_part in body[1:]:
        if body[0].ycor() == body_part.ycor() and body[0].xcor() == body_part.xcor():
            exit

    time.sleep(0.05)

sc.mainloop()
