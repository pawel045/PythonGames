import os
import sys
import time
from turtle import Screen
import snake
import food
import scoreboard


while True:

    high_score_txt = open('high_score.txt', 'r')
    high_score = int(high_score_txt.readlines()[0])

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)

    new_snake = snake.Snake(screen)
    new_food = food.Food()
    screen.listen()
    sb = scoreboard.ScoreBoard()

    play = True

    while play:

        # wyswietlenie wyniku na gorze ekranu
        sb.show_board(new_snake.points, high_score)

        #poruszanie sie weza
        new_snake.move_fd()
        new_snake.turning()

        # zdobycie punktu
        if new_snake.head.distance(new_food) < 15:

            new_food.move_food()
            new_snake.add_segment()

            ok_pos = False

            while not ok_pos:

                for segment in new_snake.segments:

                    if new_food.pos() == segment.pos():
                        new_food.move_food()

                else:
                    ok_pos = True

        # kolizja z ogonem
        for seg in new_snake.segments[1:]:
            if new_snake.head.distance(seg) == 0:
                play = False

        if new_snake.head.ycor() > 299 or \
                new_snake.head.ycor() < -299 or \
                new_snake.head.xcor() > 299 or \
                new_snake.head.xcor() < -299:
            play = False

    screen.resetscreen()

    if new_snake.points > high_score:

        high_score_txt = open('high_score.txt', 'w')
        high_score_txt.write(f'{new_snake.points}')
        high_score_txt.close()

    time.sleep(2)
