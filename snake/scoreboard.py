from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 270)

    def show_board(self, score, high_score):
        self.clear()
        self.write(f'High score: {high_score}   Score: {score}', align='center', font=('TimesNewRoman', 16, 'normal'))
        self.hideturtle()
