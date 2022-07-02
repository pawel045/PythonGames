import turtle
import pandas
from my_class import *

data = pandas.read_csv('kraje.csv')
country_names = data.Kraj.to_list()

screen = turtle.Screen()
screen.setup(width=750, height=750)
screen.title('Map of Europe')
background = "mapa_gif.gif"

screen.addshape(background)
turtle.shape(background)

sc = ScoreBoard(-150, 315)
sc.show_board()

play = True
while play:

    country = turtle.textinput(title='', prompt='Enter the name of country (or \"quit\"):')
    if country.title() in country_names:
        x_cor = int(data.x[data.Kraj == country.title()] * 0.75)
        y_cor = int(data.y[data.Kraj == country.title()] * 0.75)
        good_answer(x_cor, y_cor)
        sc.show_board()
        country_names.remove(country.title())

    if country.lower() == 'quit':
        quit()

    if sc.points == 47:
        play = False

screen.bye()
print('Congratulations, that\'s all of Europe countries.')
input('Clik enter to exit.')
