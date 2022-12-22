__author__ = "7987847, Werner, 7347119, Fajst, 7735965, Melikidze"

from time import sleep
from cmd_interface import Matrix, Terminal
from game_player import PLAYER
from game_bot import BOT


def console_input(text:str, input_str:str, screen:Matrix, fullscreen=False):
    screen.set_string(2, Terminal.get_lines() - 2, text)
    screen.set(0, Terminal.get_lines() - 2, "│")
    screen.set_string(0, Terminal.get_lines() - 3, "╭─────────────────────────── ── ── ─ ─ ─")
    if fullscreen:
        screen.set_string(0, Terminal.get_lines() - 3, "├─────────────────────────── ── ── ─ ─ ─")
        screen.set_string(0, Terminal.get_lines() - 1, "                                         ─ ─ ─ ── ── ")
    screen.print()
    return input("╰→ " + input_str + " ")

def draw_card(card:dict, screen:Matrix, x:int, y:int):
    pass


def game_rules(screen:Matrix):
    screen.refresh()
    screen.set_frame(0, 0, Terminal.get_columns() - 1, Terminal.get_lines() - 1, rounded=True, title="Game Rules")
    screen.set_string(2, int(Terminal.get_lines() /2 - 6), "How to play:")
    screen.set_string(2, int(Terminal.get_lines() /2 - 4), "1. The player with the lowest trumpf card starts the game")
    screen.set_string(2, int(Terminal.get_lines() /2 - 3), "2. The player has to play a card of the same suit as the first card")
    screen.set_string(2, int(Terminal.get_lines() /2 - 2), "3. If the player does not have a card of the same suit, he can play any card")
    screen.set_string(2, int(Terminal.get_lines() /2 - 1), "4. The player with the highest card of the same suit wins the round")
    screen.set_string(2, int(Terminal.get_lines() /2), "5. The player with the most points wins the game")
    screen.set_string(2, int(Terminal.get_lines() /2 + 1), "6. The player with the most points wins the game")
    screen.set_string(2, int(Terminal.get_lines() /2 + 3), "Press ENTER key to continue...")
    screen.print()
    input()


def config_sequence(screen:Matrix):
    screen.refresh()
    screen.set_frame(int(Terminal.get_columns() / 2 - 25), int(Terminal.get_lines() / 2 - 10), 50, 20, rounded=True, title="Game Configuration")
    screen.set_string_center(int(Terminal.get_lines() /2 - 6), "Please answer the questions below:")
    config = ['', '1', '1','1']
    question_possible_asnwers = ['1 - 5', '', '']
    previous_question = ""
    question_no = 0
    for i in ['How many players are playing?','How many bots should be playing?', 'How many cards should be drawn per player?']:
        input = ""
        screen.set_string(int(Terminal.get_columns() / 2 - 24),int(Terminal.get_lines() /2 - 4 + question_no), "                                                 ")
        screen.set_string(int(Terminal.get_columns() / 2 - 24),int(Terminal.get_lines() /2 - 2 + question_no), "                                                 ")
        screen.set_string_center(int(Terminal.get_lines() /2 - 4 + question_no), previous_question + " " + config[question_no])
        screen.set_string_center(int(Terminal.get_lines() /2 - 2 + question_no), i)
        screen.set_frame(int(Terminal.get_columns() / 2 - 24), int(Terminal.get_lines() / 2 - 3 + question_no), 48, 2,double=True)
        config[question_no + 1] = console_input(i, "[" + question_possible_asnwers[question_no] + "]", screen)
        previous_question = i
        question_no += 1
        question_possible_asnwers[1] = f"{'0' if config[1] == '5' else '1'} - {5 - int(config[1])}"
        question_possible_asnwers[2] = f"1 - {str(int(52 / (int(config[1]) + int(config[2]))))}"
    return config


def starting_screen(screen:Matrix, players:list):
    screen.refresh()
    screen.set_frame(int(Terminal.get_columns() / 2 - 25), int(Terminal.get_lines() / 2 - 10), 50, 20, rounded=True, title="Preparing...")
    screen.set_string_center(int(Terminal.get_lines() /2 - 6), "The game is starting...")
    screen.set_string_center(int(Terminal.get_lines() /2 - 4), "Here are the players:")
    # screen.set_string_center(int(Terminal.get_lines() /2 - 3), players[0].get_name())
    # screen.set_string_center(int(Terminal.get_lines() /2 - 2), players[1].get_name())
    # screen.set_string_center(int(Terminal.get_lines() /2 - 1), players[2].get_name())
    # screen.set_string_center(int(Terminal.get_lines() /2), players[3].get_name())
    # screen.set_string_center(int(Terminal.get_lines() /2 + 1), players[4].get_name())

    for i in range(len(players)):
        screen.set_string_center(int(Terminal.get_lines() /2 - 3 + i), players[i].get_name())

    screen.print()


def add_bot_font(screen:Matrix, bot:int):
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


    screen.print()

    
def draw_player_cards(screen:Matrix, cards:list):
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
        
        screen.set_string(3 + x, y - 1, "  " + str(i))
        screen.set_string(3 + x, y, card1)
        screen.set_string(3 + x, y + 1, card2)
        screen.set_string(3 + x, y + 2, card3)
        screen.set_string(3 + x, y + 3, card4)

        x += 6
    


def player_interface(screen:Matrix, player:PLAYER, round_no:int):
    screen.refresh()
    screen.set_frame(0, 0, Terminal.get_columns() - 1, Terminal.get_lines() - 1, rounded=True, title=f"Player '{player.get_name()}' is playing in round NO. {round_no}")
    draw_player_cards(screen, player.get_cards())
    screen.print()
    chosen_card = console_input("Choose a card by its number", str(len(player.get_cards())), screen, fullscreen=True)
    return player.pop_card(int(chosen_card))

def bot_interface(screen:Matrix, bot:BOT, round_no:int):
    screen.refresh()
    screen.set_frame(0, 0, Terminal.get_columns() - 1, Terminal.get_lines() - 1, rounded=True, title=f"Bot {bot.get_name()} is playing in round NO. {round_no}")
    add_bot_font(screen, bot.get_bot_number())
    screen.print()
    return bot.play_card()

def winner_screen(screen, winner, players:list):
    screen.refresh()
    screen.set_frame(int(Terminal.get_columns() / 2 - 25), int(Terminal.get_lines() / 2 - 10), 50, 20, rounded=True, title=f"Player '{winner.get_name()}' won the game!")
    screen.set_string_center(4, "Congratulations!")
    screen.set_string_center(5, f"Player '{winner.get_name()}' won the game!")
    screen.print()
