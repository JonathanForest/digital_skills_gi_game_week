import turtle as tt

sc = tt.Screen()
sc.setup(width=1000, height=400)

player_one = tt.Turtle()
player_one.setx(-400)
player_one.sety(100)
player_one.shape("turtle")

player_two = tt.Turtle()
player_two.setx(-400)
player_two.sety(-100)
player_two.shape("turtle")

# Displays the score
sketch = tt.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 150)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))

def update_details():
    p1 = player_one.xcor()
    p2 = player_two.xcor()
    sketch.clear()
    sketch.write("Left_player : {}    Right_player: {}".format(p1, p2),
             align="center", font=("Courier", 24, "normal"))


def show_winner_screen():
    ...


def move1():
    player_one.setx(player_one.xcor() + 10)
    update_details()
    if player_one.xcor() >= 400:
        sc.bye()
        print("player one won!")
def move2():
    player_two.setx(player_two.xcor() + 10)
    update_details()
    if player_two.xcor() >= 400:
        print("player two won!")
        sc.bye()

sc.listen()
sc.onkeypress(move1, "a")
sc.onkeypress(move2, "n")

sc.mainloop()
