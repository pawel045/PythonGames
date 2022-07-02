# Fun betting game with cool animation

from turtle import Turtle, Screen
from random import shuffle, randint

colors = ['red', 'green', 'orange', 'blue', 'black']
shuffle(colors)
turtles = []

screen = Screen()
screen.setup(width=500, height=400)

good_bet = False
while not good_bet:
    user_bet = screen.textinput(title='Make your bet!',
                                prompt='Which turtle will win the race?\n'
                                'red, green, orange, blue, black\n'
                                'Enter a color: ').lower()

    if user_bet in colors:
        good_bet = True

arrow = Turtle()
for color in colors:

    turtle = Turtle('turtle')
    turtle.color(color)
    turtles.append(turtle)


def start_pos(x, y, pet):

    pet.penup()
    pet.goto(x, y)


def move_turtle(pets):

    for pet in pets:
        pet.fd(randint(0, 10))


#  create start positions for all turtles
y = -150
for turt in turtles:

    start_pos(-230, y, turt)
    y += 75

arrow.penup()
arrow.goto(195, -250)
arrow.lt(90)
arrow.pendown()
arrow.fd(500)
arrow.hideturtle()

a = True
while a:
    move_turtle(turtles)

    for turt in turtles:

        if turt.xcor() > 200:
            a = False
            winner = turt.color()[0]


print(f'{str(winner).title()} won!')

if user_bet == str(winner):
    print('You won the bet!')

else:
    print('Sorry, you lost the bet!')

screen.exitonclick()
