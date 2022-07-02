import time
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


class Snake:

    def __init__(self, screen):

        # screen is Screen() object
        self.screen = screen
        self.segments = []

        for pos in STARTING_POSITION:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)
            self.screen.update()

        self.head = self.segments[0]
        self.head.color('yellow')
        self.points = 0

    def move_fd(self):
        self.screen.update()
        time.sleep(0.065)

        for num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x, new_y)

        self.head.fd(DISTANCE)

    def up(self):

        direction = self.head.heading()

        if direction == 0:
            self.head.lt(90)

        elif direction == 180:
            self.head.rt(90)

        else:
            pass

    def down(self):

        direction = self.head.heading()

        if direction == 0:
            self.head.rt(90)

        elif direction == 180:
            self.head.lt(90)

        else:
            pass

    def right(self):

        direction = self.head.heading()

        if direction == 90:
            self.head.rt(90)

        elif direction == 270:
            self.head.lt(90)

        else:
            pass

    def left(self):

        direction = self.head.heading()

        if direction == 90:
            self.head.lt(90)

        elif direction == 270:
            self.head.rt(90)

        else:
            pass

    def turning(self):

        self.screen.onkey(self.up, 'Up')
        self.screen.onkey(self.down, 'Down')
        self.screen.onkey(self.right, 'Right')
        self.screen.onkey(self.left, 'Left')

    def add_segment(self):

        self.points += 1

        new_seg_x, new_seg_y = self.segments[-1].pos()
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto((new_seg_x, new_seg_y))
        self.segments.append(new_segment)
