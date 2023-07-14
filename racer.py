import turtle
import random
import string


player_one_colour = input("Player 1: Choose a colour: ")
if player_one_colour == "":
    colour = '#'
    for i in range(6):
        colour = colour + random.choice(string.hexdigits)
        print(colour)
    player_one_colour = colour

player_two_colour = input("Player 2: Choose a colour: ")
if player_two_colour == "":
    colour = '#'
    for i in range(6):
        colour = colour + random.choice(string.hexdigits)
    player_two_colour = colour


screen = turtle.Screen()

screen.setup(height=400, width=1000)

def create_turtle(x, y, colour):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.color(colour)
    new_turtle.shape("turtle")
    new_turtle.setx(x)
    new_turtle.sety(y)
    return new_turtle

player_one = create_turtle(-400, 100, player_one_colour)

player_two = create_turtle(-400, -100, player_two_colour)

def create_banner(x, y, colour):
    message = turtle.Turtle()
    message.color(colour)
    message.penup()
    message.hideturtle()
    message.goto(x, y)
    return message

header = create_banner(0, 150, "red")
header.write("Tuuuuuurtle Raaaaacer!",
             font=("Courier", 24, "normal"),
             align="center")

def have_they_won(player, player_name):
    x_coordinate = player.xcor()
    if x_coordinate >= 400:
        header.clear()
        header.write(player_name + " Won! Well Done!",
                font=("Courier", 24, "normal"),
                align="center")

def move_player_one():
    current_x = player_one.xcor()
    player_one.setx(current_x + 20)
    have_they_won(player_one, "Player 1")

def move_player_two():
    current_x = player_two.xcor()
    player_two.setx(current_x + 20)
    have_they_won(player_two, "Player 2")


screen.listen()
screen.onkeypress(move_player_one, "a")
screen.onkeypress(move_player_two, "n")






screen.mainloop()
