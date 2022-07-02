from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.speed('fastest')
        self.penup()
        self.color('Black')
        self.goto(x, y)
        self.points = -1

    def show_board(self):
        self.clear()
        self.points += 1
        self.write(f'{self.points}/47', align='center', font=('TimesNewRoman', 24, 'normal'))
        self.hideturtle()


def good_answer(x, y):

    new_x = x - 375
    new_y = -(y - 375)
    new_turtle = Turtle()
    new_turtle.speed('fastest')
    new_turtle.penup()
    new_turtle.goto(new_x, new_y)
    new_turtle.dot(10, 'red')
    new_turtle.hideturtle()
