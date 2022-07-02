# Blackjack in cmd

import os
from time import sleep
from random import shuffle

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')


# function -> clear console if too much information
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def you_win(value_player, value_cp = 0):
    if value_player > 21 or (value_cp > value_player and value_cp < 22):
        return False

    elif value_player > value_cp or value_cp >= 22:
        return True

    else:
        return None


def starting(player, computer):

    clear_console()

    global deck
    deck = Deck()
    deck.shuffle()

    player.cards_held = []
    cp.cards_held = []
    player.jackpot = 0

    player.show_cash()
    player.hit(deck)
    player.hit(deck)
    player.show_board()
    computer.hit(deck)
    computer.show_board()

    return deck, player.cards_held, cp.cards_held


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return str(self.rank) + ' of ' + str(self.suit)


class Deck:

    def __init__(self):
        self.all_cards = []

        for s in suits:
            for r in ranks:
                card = Card(r, s)
                self.all_cards.append(card)

    def shuffle(self):
        shuffle(self.all_cards)

    def remove_card(self):
        return self.all_cards.pop(0)

    def count_card_in_deck(self):
        return len(self.all_cards)


class Player:

    def __init__(self, name, cash=1000):
        self.name = name
        self.cash = cash
        self.cards_held = []
        self.jackpot = 0
        self.sum_value = 0

    def bet(self, bet_money):
        self.cash -= bet_money
        self.jackpot += bet_money

    def hit(self, current_deck):

        self.cards_held.append(current_deck.remove_card())

    def show_board(self):

        print(f'{self.name}\'s cards on table: ')
        for card in self.cards_held:
            print(card)

        self.sum_value = 0

        for card in self.cards_held:
            self.sum_value += card.value

        print(f'Value of {self.name} card(s): {self.sum_value}', end='\n\n')
        return self.sum_value

    def show_cash(self):
        print(f'{self.name}\'s cash: {self.cash}$')

    def stay(self):

        for card in self.cards_held:
            self.sum_value += values[card[0]]

        return self.sum_value


# Intro to the game.
good_answer = False
play_the_game = False

while not good_answer:

    lets_play = input('Hello, this is Blackjack card game.\nWould you play with me? (yes/no) ')

    if lets_play == 'yes':
        good_answer = True
        play_the_game = True

    elif lets_play == 'no':
        print('That\'s great. It\'s a gambling game.\nGoodbye :)')
        input()
        quit()

    else:

        clear_console()
        print('Please enter your answer again.')

# Game logic
while play_the_game:

    print('Let\'s play!')
    player_name = input('Enter Your name: ')
    clear_console()

    player = Player(player_name)
    cp = Player(name='Croupier')

    # Starting position of cards
    starting(player, cp)

    # Player can move right now
    player_move = True
    while player_move:
        bet_move = False
        while not bet_move:
            try:
                money = int(input('Bet money: '))

                if money > player.cash:
                    print('Too much money! Enter less value.')
                    continue

                elif money <= 0:
                    print('It can\'t be a zero or negative value.')
                    continue

                player.bet(money)
                player.show_cash()
                print(f'Jackpot: {player.jackpot}$')
                bet_move = True

            except:
                print('It must be an integer!')

        # Players move -> he can hit or stay. If hit, he draws a card. If he stays, program compute players point, and
        # croupier starts his turn.
        move_bool = True
        while move_bool:
            move = input('Pick your move (hit/stay): ')

            # Player says 'hit'
            if move == 'hit':
                clear_console()
                player.hit(deck)
                player.show_board()
                cp.show_board()

                # loss condition
                if player.sum_value > 21:

                    # Change an ace value, if it's necessary.
                    for card in player.cards_held:
                        if card.rank == 'Ace' and card.value == 11:
                            card.value = 1
                            clear_console()
                            player.show_board()
                            cp.show_board()

                            if player.sum_value < 22:
                                break
                    # If player still loss.
                    if not you_win(player.sum_value):
                        print('You loose!', end='\n\n')
                        # No money conditions.
                        if player.cash <= 0:
                            print('You don\'t have anymore money. Back to your wife/husband and tell '
                                  'her\him, \nthat you\'re addicted gambler and you had lost all your belongings!')

                            print('Have a nice day :)')
                            input()
                            quit()

                        sleep(3)
                        starting(player, cp)
                        move_bool = False

            elif move == 'stay':
                print(f'Your score is: {player.sum_value}'
                      '\nCroupier is playing now.')
                sleep(3)
                move_bool = False

                # Croupier moves
                croupier_plays = True
                while croupier_plays:
                    # Croupier has more points than player, but max 21.
                    if cp.sum_value > player.sum_value and cp.sum_value < 22:
                        # Croupier win
                        print('Croupier wins!')
                        sleep(3)
                        starting(player, cp)
                        croupier_plays = False
                        move_bool = False

                    # Croupier has fewer points than player.
                    elif cp.sum_value < player.sum_value:
                        cp.hit(deck)
                        clear_console()
                        player.show_board()
                        cp.show_board()
                        sleep(3)

                    # Croupier has equal points like player.
                    elif cp.sum_value == player.sum_value:
                        # Croupier takes a tie.
                        if player.sum_value > 15:
                            print('It\'s draw!\nYour money back to You.')
                            sleep(3)
                            player.cash += player.jackpot
                            starting(player, cp)
                            croupier_plays = False
                            move_bool = False

                        # Croupier still plays.
                        else:
                            cp.hit(deck)
                            clear_console()
                            player.show_board()
                            cp.show_board()
                            sleep(3)

                    # Croupier has more than 21 points.
                    elif cp.sum_value > 21:
                        # Change an ace value, if it's necessary.
                        for card in cp.cards_held:
                            if card.rank == 'Ace' and card.value == 11:
                                card.value = 1
                                clear_console()
                                player.show_board()
                                cp.show_board()

                                if cp.sum_value < 22:
                                    break

                        # Can croupier play? Double check.
                        if cp.sum_value < player.sum_value:
                            cp.hit(deck)
                            clear_console()
                            player.show_board()
                            cp.show_board()
                            sleep(3)
                            continue

                        # Player wins in this case.
                        if you_win(player.sum_value, cp.sum_value):
                            print('You win!', end='\n\n')
                            player.cash += 2 * player.jackpot

                            starting(player, cp)
                            croupier_plays = False
                            move_bool = False

            else:
                print('Wrong text. Try again!')

            bet_move = False
        player_move = True
    play_the_game = False

input()
