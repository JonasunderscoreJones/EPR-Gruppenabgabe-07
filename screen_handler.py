'''EPR 07 Aufgabe 3'''
__author__ = "7987847, Werner, 7347119, Fajst, 7735965, Melikidze"

from time import sleep
from cmd_interface import Matrix, Terminal
from game_player import PLAYER
from game_bot import BOT


def console_input(text:str, input_str:str, screen:Matrix, fullscreen=False):
    '''
    Prints a text and waits for user input
    input:
        - text: str
            text to print
        - input_str: str
            input string
        - screen: Matrix
            screen to print on
        - fullscreen: bool
            if the screen is fullscreen
    output:
        - input: str
            user input
    '''
    screen.set_string(2, Terminal.get_lines() - 2, text)
    screen.set(0, Terminal.get_lines() - 2, "│")
    screen.set_string(0, Terminal.get_lines() - 3,
                      "╭─────────────────────────── ── ── ─ ─ ─")
    if fullscreen:
        screen.set_string(0, Terminal.get_lines() - 3,
                          "├─────────────────────────── ── ── ─ ─ ─")
        screen.set_string(0, Terminal.get_lines() - 1,
                    "                                         ─ ─ ─ ── ── ")
    screen.print()
    return input("╰→ " + input_str + " ")


def game_rules(screen:Matrix):
    '''
    Prints the game rules
    input:
        - screen: Matrix
            screen to print on
    '''
    screen.refresh()
    screen.set_frame(0, 0, Terminal.get_columns() - 1,
    Terminal.get_lines() - 1, rounded=True, title="Game Rules")
    screen.set_string(2, int(Terminal.get_lines() /2 - 6), "How to play:")
    screen.set_string(2, int(Terminal.get_lines() /2 - 5),
        "1. The goal is to play the highest card.")
    screen.set_string(2, int(Terminal.get_lines() /2 - 4),
        "2. The trumpf color outweights all other colors.")
    screen.set_string(2, int(Terminal.get_lines() /2 - 3),
        "3. The player who wins the most amounts of tricks\
 (Stiche) wins the game.")
    screen.set_string(2, int(Terminal.get_lines() /2 + 3),
        "Press ENTER key to continue...")
    screen.print()
    input()


def config_sequence(screen:Matrix):
    '''
    Prints the game configuration sequence
    input:
        - screen: Matrix
            screen to print on
    output:
        - config: list
            list of the game configuration
    '''
    screen.refresh()
    screen.set_frame(int(Terminal.get_columns() / 2 - 25),
                     int(Terminal.get_lines() / 2 - 10), 50, 20, rounded=True,
                     title="Game Configuration")
    screen.set_string_center(int(Terminal.get_lines() /2 - 6),
                            "Please answer the questions below:")
    config = ['', '1', '1']
    question_possible_asnwers = ['0 - 5', '']
    previous_question = ""
    question_no = 0
    for i in ['How many players are playing?',
              'How many bots should be playing?']:
        wrong_input = True
        while wrong_input:
            screen.set_string(int(Terminal.get_columns() / 2 - 24),
                              int(Terminal.get_lines() /2 - 4 + question_no),
                        "                                                 ")
            screen.set_string(int(Terminal.get_columns() / 2 - 24),
                              int(Terminal.get_lines() /2 - 2 + question_no),
                        "                                                 ")
            screen.set_string_center(int(Terminal.get_lines() /2 - 4 +\
                question_no), previous_question + " " + config[question_no])
            screen.set_string_center(int(Terminal.get_lines() /2 - 2 +\
                question_no), i)
            screen.set_frame(int(Terminal.get_columns() / 2 - 24),
                             int(Terminal.get_lines() / 2 - 3 + question_no),
                             48, 2,double=True)
            input = console_input(i, "[" +\
                question_possible_asnwers[question_no] + "]", screen)
            if input.isdigit():
                if int(question_possible_asnwers[question_no].split(" - ")[0])\
                    <= int(input) <=\
                        int(question_possible_asnwers[question_no].split(" - "\
                            )[1]):
                    wrong_input = False
        config[question_no + 1] = input
        previous_question = i
        question_no += 1
        question_possible_asnwers[1] = f"{'0' if config[1] == '5' else '2' if config[1] == '0' else '1'} -\
 {5 - int(config[1])}"
    return config


def starting_screen(screen:Matrix, players:list):
    '''
    Prints the starting screen
    input:
        - screen: Matrix
            screen to print on
        - players: list
            list of the players
    '''
    screen.refresh()
    screen.set_frame(int(Terminal.get_columns() / 2 - 25),
                     int(Terminal.get_lines() / 2 - 10), 50, 20, rounded=True,
                     title="Preparing...")
    screen.set_string_center(int(Terminal.get_lines() /2 - 6),
                             "The game is starting...")
    screen.set_string_center(int(Terminal.get_lines() /2 - 4),
                             "Here are the players:")

    for i in range(len(players)):
        screen.set_string_center(int(Terminal.get_lines() /2 - 3 + i),
                                 players[i].get_name())

    screen.print()


def add_bot_font(screen:Matrix, bot:int):
    '''
    Adds the bot font to the screen
    input:
        - screen: Matrix
            screen to print on
        - bot: int
            bot number
    '''
    line_1 = "$$$$$$$\             $$\          "
    line_2 = "$$  __$$\            $$ |         "
    line_3 = "$$ |  $$ | $$$$$$\ $$$$$$\        "
    line_4 = "$$$$$$$\ |$$  __$$\\_$$  _|       "
    line_5 = "$$  __$$\ $$ /  $$ | $$ |         "
    line_6 = "$$ |  $$ |$$ |  $$ | $$ |$$\      "
    line_7 = "$$$$$$$  |\$$$$$$  | \$$$$  |     "
    line_8 = "\_______/  \______/   \____/      "

    if bot == 1:
        screen.set_string_center(4, line_1 + "   $$\   ")
        screen.set_string_center(5, line_2 + " $$$$ |  ")
        screen.set_string_center(6, line_3 + " \_$$ |  ")
        screen.set_string_center(7, line_4 + "    $$ |  ")
        screen.set_string_center(8, line_5 + "   $$ |  ")
        screen.set_string_center(9, line_6 + "   $$ |  ")
        screen.set_string_center(10, line_7 + " $$$$$$\ ")
        screen.set_string_center(11, line_8 + " \______|")

    elif bot == 2:
        screen.set_string_center(4, line_1 + " $$$$$$\  ")
        screen.set_string_center(5, line_2 + "$$  __$$\ ")
        screen.set_string_center(6, line_3 + "\__/  $$ |")
        screen.set_string_center(7, line_4 + " $$$$$$   |")
        screen.set_string_center(8, line_5 + "$$  ____/ ")
        screen.set_string_center(9, line_6 + "$$ |      ")
        screen.set_string_center(10, line_7 + "$$$$$$$$\ ")
        screen.set_string_center(11, line_8 + "\________|")

    elif bot == 3:
        screen.set_string_center(4, line_1 + " $$$$$$\  ")
        screen.set_string_center(5, line_2 + "$$ ___$$\ ")
        screen.set_string_center(6, line_3 + "\_/   $$ |")
        screen.set_string_center(7, line_4 + "  $$$$$ / ")
        screen.set_string_center(8, line_5 + "  \___$$\ ")
        screen.set_string_center(9, line_6 + "$$\   $$ |")
        screen.set_string_center(10, line_7 + "\$$$$$$  |")
        screen.set_string_center(11, line_8 + " \______/ ")

    elif bot == 4:
        screen.set_string_center(4, line_1 + "$$\   $$\ ")
        screen.set_string_center(5, line_2 + "$$ |  $$ |")
        screen.set_string_center(6, line_3 + "$$ |  $$ |")
        screen.set_string_center(7, line_4 + " $$$$$$$$ |")
        screen.set_string_center(8, line_5 + "\_____$$ |")
        screen.set_string_center(9, line_6 + "      $$ |")
        screen.set_string_center(10, line_7 + "      $$ |")
        screen.set_string_center(11, line_8 + "      \__|")
    
    elif bot == 5:
        screen.set_string_center(4, line_1 + "$$$$$$$\  ")
        screen.set_string_center(5, line_2 + "$$  ____| ")
        screen.set_string_center(6, line_3 + "$$ |      ")
        screen.set_string_center(7, line_4 + "$$$$$$$\  ")
        screen.set_string_center(8, line_5 + "\_____$$\ ")
        screen.set_string_center(9, line_6 + "$$\   $$ |")
        screen.set_string_center(10, line_7 + "\$$$$$$  |")
        screen.set_string_center(11, line_8 + " \______/ ")


    screen.print()


def draw_player_cards(screen:Matrix, cards:list, players = None):
    '''
    Draws the cards of the players
    input:
        - screen: Matrix
            screen to print on
        - cards: list
            list of the cards
        - players: list
            list of the players
    '''
    card1 = "╔═══╗"
    card2 = "║ X ║"
    card3 = "║ X ║"
    card4 = "╚═══╝"

    SUITS = ["♠", "♥", "♦", "♣"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    y = 5
    x = 0

    for i in range(len(cards)):
        card = cards[i]
        if Terminal.get_columns() < x + 10:
            y += 7
            x = 0
        if card.get("suit") == "Spades":
            card2 = "║ ♠ ║"
        elif card.get("suit") == "Hearts":
            card2 = "║ ♥ ║"
        elif card.get("suit") == "Diamonds":
            card2 = "║ ♦ ║"
        elif card.get("suit") == "Clubs":
            card2 = "║ ♣ ║"

        if card.get("rank") == "Ace":
            card3 = "║ A ║"
        elif card.get("rank") == "Jack":
            card3 = "║ J ║"
        elif card.get("rank") == "Queen":
            card3 = "║ Q ║"
        elif card.get("rank") == "King":
            card3 = "║ K ║"
        elif card.get("rank") == "10":
            card3 = "║10 ║"
        else:
            card3 = f"║ {card.get('rank')} ║"
        if players is not None:
            screen.set_string(3 + x, y - 1, "  " + players[i].get_name() + ": \
" + str(players[i].get_points()) + " points")
        else:
            screen.set_string(3 + x, y - 1, "  " + str(i + 1))
        screen.set_string(3 + x, y, card1)
        screen.set_string(3 + x, y + 1, card2)
        screen.set_string(3 + x, y + 2, card3)
        screen.set_string(3 + x, y + 3, card4)

        if players is not None:
            x += 16
        x += 6



def player_interface(screen:Matrix, player:PLAYER, round_no:int, stich:int,
                     trumpf:str, trumpf_sym:str):
    '''
    Draws the interface for the player
    input:
        - screen: Matrix
            screen to print on
        - player: PLAYER
            player object
        - round_no: int
            number of the round
        - stich: int
            number of the stich
        - trumpf: str
            trumpf of the round
        - trumpf_sym: str
            symbol of the trumpf
    '''
    screen.refresh()
    screen.set_frame(0, 0, Terminal.get_columns() - 1,
                     Terminal.get_lines() - 1, rounded=True, title=f"Player \
 '{player.get_name()}' is playing in round NO. \
 {round_no} and trick NO. {stich}")
    screen.set_string(Terminal.get_columns() - len(trumpf + "          ") - 2,
                      2, "Trumpf: " + trumpf + " " + trumpf_sym)
    screen.set_string(2, 2, f"Points of player {player.get_name()}: \
 {player.get_points()}")
    draw_player_cards(screen, player.get_cards())
    screen.print()
    wrong_input = True
    while wrong_input:
        chosen_card = console_input("Choose a card by its number", "[1 - " +\
            str(len(player.get_cards())) + "]", screen, fullscreen=True)
        if chosen_card.isdigit():
            if int(chosen_card) > 0 and int(chosen_card) <=\
                len(player.get_cards()):
                wrong_input = False
    return player.pop_card(int(chosen_card) - 1)

def bot_interface(screen:Matrix, bot:BOT, round_no:int, stich:int):
    '''
    Draws the interface for the bot
    input:
        - screen: Matrix
            screen to print on
        - bot: BOT
            bot object
        - round_no: int
            number of the round
        - stich: int
            number of the stich
    '''
    screen.refresh()
    screen.set_frame(0, 0, Terminal.get_columns() - 1,\
        Terminal.get_lines() - 1, rounded=True, title=f"Bot {bot.get_name()} \
 is playing in round NO. {round_no}, trick NO. {stich}")
    add_bot_font(screen, bot.get_bot_number())
    screen.print()
    return bot.play_card()

def winner_screen(screen, winner, players:list):
    '''
    Draws the screen for the winner
    input:
        - screen: Matrix
            screen to print on
        - winner: PLAYER
            player object
        - players: list
            list of all players
    '''
    screen.refresh()
    screen.set_frame(int(Terminal.get_columns() / 2 - 25),
                      int(Terminal.get_lines() / 2 - 10), 50, 20, rounded=True,
                      title=f"Player '{winner.get_name()}' won the game!")
    screen.set_string_center(4, "Congratulations!")
    screen.set_string_center(5, f"Player '{winner.get_name()}' won the game!")
    screen.print()

def trumpf_screen(screen:Matrix, trumpf:str):
    '''
    Draws the screen for the trumpf
    input:
        - screen: Matrix
            screen to print on
        - trumpf: str
            trumpf of the round
    '''
    screen.refresh()
    screen.set_frame(int(Terminal.get_columns() / 2 - 25),
                     int(Terminal.get_lines() / 2 - 10), 50, 20,
                         rounded=True, title="Trumpf")
    screen.set_string_center( int(Terminal.get_lines() / 2 - 1),
                             "The trumpf is:")
    screen.set_string_center( int(Terminal.get_lines() / 2), trumpf)
    screen.print()

def stich_win_screen(screen:Matrix, winner, players:list, cards:list,
                     trumpf:str, trumpf_sym:str):
    '''
    Draws the screen for the stich winner
    input:
        - screen: Matrix
            screen to print on
        - winner: PLAYER
            player object
        - players: list
            list of all players
        - cards: list
            list of all cards
        - trumpf: str
            trumpf of the round
        - trumpf_sym: str
            symbol of the trumpf
    '''
    screen.refresh()
    screen.set_frame(0, 0, Terminal.get_columns() - 1,
                     Terminal.get_lines() - 1, rounded=True, title=f"Player \
'{winner.get_name()}' won the trick!")
    screen.set_frame(int(Terminal.get_columns() / 2 - 25), 19, 50, 4,
                     double=True)
    screen.set_string_center(20, "Congratulations!")
    screen.set_string_center(21, f"Player '{winner.get_name()}'\
 won the trick!")
    screen.set_string_center(22, "Press ENTER to continue...")
    screen.set_string(Terminal.get_columns() - len(trumpf + "          ") - 2,
                      2, "Trumpf: " + trumpf + " " + trumpf_sym)
    draw_player_cards(screen, cards, players)
    screen.print()
    input()
