'''EPR 07 Aufgabe 3'''
__author__ = "7987847, Werner, 7347119, Fajst, 7735965, Melikidze"

from time import sleep
from random import randint

from cmd_interface import Matrix, Terminal
import screen_handler
import game
from game_bot import BOT
from game_player import PLAYER

# initialize screen
screen = Matrix()

NO = ["n", 'N', 'no', 'No', 'NO', 'nO','']
YES = ["y", 'Y', 'yes', 'Yes', 'YES', 'yES','yEs','YeS','yES', '']

PREVIOUS_CONFIG = None

def main(first_time:bool=True, previous_config = None):
    '''
    The main function of the game
    input:
        - first_time: bool
            if the game is started for the first time
        - previous_config: list
            previous config of the game
        
    output:
        - previous_config: list
            previous config of the game
    '''
    # welcome screen - only shown on first start
    if first_time:
        screen.refresh()
        screen.set_frame(int(Terminal.get_columns() / 2 - 25),
        int(Terminal.get_lines() / 2 - 10), 50, 20, rounded=True,
        title="Welcome to the game")
        screen.set_string_center(int(Terminal.get_lines() /2 - 7),
        "Follow these instructions")
        screen.set_string_center(int(Terminal.get_lines() /2 - 6),
        "for an enhanced gaming experience:")
        screen.set_string_center(int(Terminal.get_lines() /2 - 4),
        "1. Make sure your terminal is")
        screen.set_string_center(int(Terminal.get_lines() /2 - 3),
        " fullscreen or at least 80x24")
        screen.set_string_center(int(Terminal.get_lines() /2),
        "2. Make sure to not resize your")
        screen.set_string_center(int(Terminal.get_lines() /2 + 1),
        " terminal during gameplay")
        screen.set_string_center(int(Terminal.get_lines() /2 + 4),
        "Your terminal currently has the size:")
        screen.set_string_center(int(Terminal.get_lines() /2 + 5),
        f"{Terminal.get_columns()}x{Terminal.get_lines()}")
        screen.set_string_center(int(Terminal.get_lines() /2 + 7),
        "If your terminal is not fullscreen or")
        screen.set_string_center(int(Terminal.get_lines() /2 + 8),
        "at least 80x28, the game will pause")
        screen.set_string_center(int(Terminal.get_lines() /2 + 9),
        "and display an error message until resolved")
        # ask if user wants to see the rules
        if screen_handler.console_input(
            "Would you like to check out the rules of the game?", "[Y/n]",
            screen) in YES:
            screen_handler.game_rules(screen)
    screen.refresh()
    # ask if user wants to reuse the previous config
    # only shown if the game is not started for the first time
    if previous_config is not None and screen_handler.console_input(
        "Would you like to reuse the configuration from the last game?",
        "[Y/n]", screen) in YES:
        pass
    else:
        # else show config screen
        previous_config = screen_handler.config_sequence(screen)
        # previous_config = ['', <Player count>, '<Bot Count>']

    screen.refresh()
    screen.print()

    # game initialization
    # create players and bots
    players = []

    # create players
    # Ask for player names, set cards to empty list
    # PLAYER(name, cards)
    for i in range(0, int(previous_config[1])):
        players.append(PLAYER(screen_handler.console_input(
            f'Name for Player {i + 1}: In der kürze liegt die Würze \
(In short lies the spice :) )', '', screen=screen), []))
    # create bots
    # set cards to empty list
    # id is number of the bot starting from 1
    # name is Bot <id>
    # BOT(name, id, cards)
    for i in range(0, int(previous_config[2])):
        players.append(BOT(f'Bot {i + 1}', i + 1, []))

    screen.refresh()

    # starting screen with player names
    screen_handler.starting_screen(screen, players)

    sleep(1)

    screen.refresh()

    # determine the amount of turns
    # 52 cards per card deck
    max_turns = int(52 / len(players))
    # debug to shorten game
    # max_turns = 3

    # main game loop
    for turn in range(1, max_turns):
        SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        SUITS_SYM = ["♠", "♥", "♦", "♣"]
        # determine trumpf color for this turn
        # is determined randomly
        trumpf_color = SUITS[randint(0, 3)]

        # show trumpf screen
        screen_handler.trumpf_screen(screen, trumpf_color)
        sleep(2)

        # create and deal cards
        card_deck = game.create_cards()
        # deal_cards(card_deck, amount, turn)
        # dealt_cards is a tuple of lists
        dealt_cards = game.deal_cards(card_deck, int(previous_config[1]) +
        int(previous_config[2]), turn)

        # set cards for each player
        for player in players:
            player.set_cards(dealt_cards[players.index(player)])

        # trick loop
        # cards is the list of played cards in the order of the players
        cards = []
        
        for stiche in range(0, turn):
            cards = []
            # each player plays a card
            for player in players:
                # if player is a bot, use bot interface
                if player.is_bot():
                    cards.append(screen_handler.bot_interface(screen, player,
                    turn, stiche + 1))
                    sleep(0.5)
                # else use player interface
                else:
                    cards.append(screen_handler.player_interface(
                        screen, player, turn, stiche + 1, trumpf_color,
                        SUITS_SYM[SUITS.index(trumpf_color)]))
            # both the bot and the player interface return the played card

            # determine winner of the trick
            winner = game.compare_cards(cards, trumpf_color)
            players[winner].add_points(1)

            # show trick winner
            screen_handler.stich_win_screen(screen, players[winner], players,
            cards, trumpf_color, SUITS_SYM[SUITS.index(trumpf_color)])


    # determine winner
    winner = players[0]
    for player in players:
        if player.get_points() > winner.get_points():
            winner = player
    screen_handler.winner_screen(screen, winner, players)







    return previous_config



if __name__ == "__main__":
    try:
        # run the game
        PREVIOUS_CONFIG =  main()
        # main() returns the previous config

        # ask if user wants to play again
        # repeat until user does not want to play again
        while screen_handler.console_input("Would you like to play again?",
        "[Y/n]", screen) in YES:
            screen.refresh()
            # run the game again with the previous config
            PREVIOUS_CONFIG = main(first_time=False,
                                   previous_config=PREVIOUS_CONFIG)
    # if user presses ctrl + c (keyboard interrupt), exit the game
    except KeyboardInterrupt:
        pass
    
    # clear the terminal and print a thank you message
    Terminal.clear()
    print("Thank you for playing!")
