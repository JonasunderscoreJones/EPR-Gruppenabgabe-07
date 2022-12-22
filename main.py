__author__ = "7987847, Werner, 7347119, Fajst, 7735965, Melikidze"

from cmd_interface import Matrix, Terminal
from time import sleep

import screen_handler
import game
from game_bot import BOT
from game_player import PLAYER

screen = Matrix()

NO = ["n", 'N', 'no', 'No', 'NO', 'nO','']
YES = ["y", 'Y', 'yes', 'Yes', 'YES', 'yES','yEs','YeS','yES', '']

previous_config = None


def main(first_time:bool=True, previous_config = None):
    if first_time:
        screen.refresh()
        screen.set_frame(int(Terminal.get_columns() / 2 - 25), int(Terminal.get_lines() / 2 - 10), 50, 20, rounded=True, title="Welcome to the game")
        screen.set_string_center(int(Terminal.get_lines() /2 - 7), "Follow these instructions")
        screen.set_string_center(int(Terminal.get_lines() /2 - 6), "for an enhanced gaming experience:")
        screen.set_string_center(int(Terminal.get_lines() /2 - 4), "1. Make sure your terminal is")
        screen.set_string_center(int(Terminal.get_lines() /2 - 3), " fullscreen or at least 80x24")
        screen.set_string_center(int(Terminal.get_lines() /2), "2. Make sure to not resize your")
        screen.set_string_center(int(Terminal.get_lines() /2 + 1), " terminal during gameplay")
        screen.set_string_center(int(Terminal.get_lines() /2 + 4), "Your terminal currently has the size:")
        screen.set_string_center(int(Terminal.get_lines() /2 + 5), f"{Terminal.get_columns()}x{Terminal.get_lines()}")
        screen.set_string_center(int(Terminal.get_lines() /2 + 7), "If your terminal is not fullscreen or")
        screen.set_string_center(int(Terminal.get_lines() /2 + 8), "at least 80x24, the game will pause")
        screen.set_string_center(int(Terminal.get_lines() /2 + 9), "and display an error message until resolved")
        if screen_handler.console_input("Would you like to check out the rules of the game?", "[Y/n]", screen) in YES:
            # TODO: Show rules
            screen_handler.game_rules(screen)
    screen.refresh()
    if previous_config is not None and screen_handler.console_input("Would you like to reuse the configuration from the last game?", "[Y/n]", screen) in YES:
        pass
    else:
        previous_config = screen_handler.config_sequence(screen)

    screen.refresh()
    screen.print()


    card_deck = game.create_cards()
    dealt_cards = game.deal_cards(card_deck, int(previous_config[1]) + int(previous_config[2]), int(previous_config[3]))

    players = []
    for i in range(0, int(previous_config[1])):
        players.append(PLAYER(screen_handler.console_input(f'Name for Player {i + 1}', '', screen=screen), dealt_cards[i]))
    for i in range(0, int(previous_config[2])):
        players.append(BOT(f'Bot {i + 1}', i + 1, dealt_cards[len(previous_config[1]) + i]))
    
    screen.refresh()

    screen_handler.starting_screen(screen, players)

    sleep(5)

    screen.refresh()

    round_no = 0

    while players[0].get_cards() != []:
        round_no += 1
        cards = []
        for player in players:
            if player.is_bot():
                cards.append(screen_handler.bot_interface(screen, player, round_no))
                sleep(0.5)
            else:
                cards.append(screen_handler.player_interface(screen, player, round_no))
        players[game.compare_cards(cards)].add_points(1)
    
    # determine winner
    winner = players[0]
    for player in players:
        if player.get_points() > winner.get_points():
            winner = player
    screen_handler.winner_screen(screen, winner, players)


    



    
    return previous_config
    


if __name__ == "__main__":
    try:
        previous_config =  main()
        while screen_handler.console_input("Would you like to play again?", "[Y/n]", screen) in YES:
            screen.refresh()
            previous_config = main(first_time=False, previous_config=previous_config)
    except KeyboardInterrupt:
        pass

    Terminal.clear()
    print("Thank you for playing!")