"""

Pong

"""

# Import required library
import turtle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

PLAYER_ONE_X = -400
PLAYER_TWO_X = 400

# Create the screen where the users will play
sc = turtle.Screen()
sc.title("Pong")
sc.bgcolor("black")
sc.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)


# Left paddle
player_one = turtle.Turtle()
player_one.speed(0)
player_one.shape("square")
player_one.color("green")
player_one.shapesize(stretch_wid=6, stretch_len=2)
player_one.penup()
player_one.goto(PLAYER_ONE_X, 0)


# Right paddle
player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape("square")
player_two.color("green")
player_two.shapesize(stretch_wid=6, stretch_len=2)
player_two.penup()
player_two.goto(PLAYER_TWO_X, 0)


# Ball of circle shape
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5


# Initialize the score
left_player = 0
right_player = 0


# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))


# Functions to move paddle vertically
def paddleaup():
    y = player_one.ycor()
    y += 20
    player_one.sety(y)


def paddleadown():
    y = player_one.ycor()
    y -= 20
    player_one.sety(y)


def paddlebup():
    y = player_two.ycor()
    y += 20
    player_two.sety(y)


def paddlebdown():
    y = player_two.ycor()
    y -= 20
    player_two.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")


while True:

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Checking borders
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "normal"))

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                                 left_player, right_player), align="center",
                                 font=("Courier", 24, "normal"))

    # Paddle ball collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < player_two.ycor()+70 and
                                                              ball.ycor() > player_two.ycor()-70):
        ball.setx(360)
        ball.dx*=-1

    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor() < player_one.ycor() + 70 and
                                                            ball.ycor()>player_one.ycor()-70):
        ball.setx(-360)
        ball.dx*=-1





















