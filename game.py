'''EPR 07 Aufgabe 3'''
__author__ = "7987847, Werner, 7347119, Fajst, 7735965, Melikidze"

from random import randint

RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen',
'King']
SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

def create_cards():
    '''
    Creates a deck of cards

    output:
        - card_deck: list
            list of cards
    '''
    card_deck = []
    # add every combination of suit and rank to the deck
    for suit in SUITS:
        for rank in RANKS:
            card = {'rank': rank, 'suit': suit}
            card_deck.append(card)
    return card_deck


def deal_cards(card_deck:list, players:int, cards_per_player:int):
    '''
    Deals cards to players

    input:
        - card_deck: list
            list of cards
        - players: int
            number of players
        - cards_per_player: int
            number of cards per player
    output:
        - player_cards: tuple
            tuple of lists, each list contains the cards of a player
    '''
    # create a list of lists, each list contains the cards of a player in the
    # order of their occurance in the players list in the game loop of main.py
    temp_cards = []
    for player in range(players):
        temp_cards.append([])
        for _ in range(cards_per_player):
            # add a random card to the player's list and remove it from the
            # deck
            temp_cards[player].append(card_deck.pop(randint(0,
                                                    len(card_deck)-1)))
    # if the number of players is not equal to 5, add empty lists to the list
    # until it has 5 elements
    while len(temp_cards) < 5:
        temp_cards.append([])
    # return the list of lists as a tuple
    return (temp_cards[0], temp_cards[1], temp_cards[2], temp_cards[3],
        temp_cards[4])


def compare_cards(cards_to_compare:list, trumpf_color:str):
    '''
    Compares the given cards and returns the winner

    input:
        - cards_to_compare: list
            list of cards to compare
    output:
        - winner: int
            index of the winning card
    '''
    # first player is defined as winner
    winner = 0
    # no possible trump card has been detected yet
    # list contains all indices of trump cards
    # index maps to index in cards_to_compare
    trumpf = []
    # index of all trump cards are added to trumpf
    for i in cards_to_compare:
        if i.get('suit') == trumpf_color:
            trumpf.append(cards_to_compare.index(i))
    if len(trumpf) == 1:
        # if only one trump card is present, it is the winner
        return trumpf[0]
    elif len(trumpf) > 1:
        winner = 0
        for j in trumpf:
            # loop through all trump cards and compare them
            # highest rank is the winner
            if RANKS.index(cards_to_compare[j].get('rank')) > RANKS.index(
                cards_to_compare[winner].get('rank')):
                winner = j
        winner = j
    else:
        # no trump card is present
        winner = 0
        # loop through all cards and compare them
        # highest rank is the winner
        for j in cards_to_compare:
            if RANKS.index(j.get('rank')) > RANKS.index(
                    cards_to_compare[winner].get('rank')):
                winner = cards_to_compare.index(j)
                print(winner, j, cards_to_compare)

    return winner


if __name__ == '__main__':
    card_deck = create_cards()
    print(card_deck)

    print(deal_cards(card_deck, 5, 5))

if __name__ == '__main__':
    # Testcases
    deck = create_cards()
    print(deck)
    print(deal_cards(create_cards(), deck, 5))
    print(deal_cards(create_cards(), deck, 0))
    try:
        print(deal_cards(create_cards(), deck, 100))
    except:
        print('Exception')

    print(compare_cards([{'rank': 'Ace', 'suit': 'Spades'}, {'rank': 'Ace', 'suit': 'Spades'}]), 'Spades')
    print(compare_cards([{'rank': 'Ace', 'suit': 'Spades'}, {'rank': 'Ace', 'suit': 'Hearts'}]), 'Hearts')
    print(compare_cards([{'rank': 'Ace', 'suit': 'Spades'}, {'rank': 'Ace', 'suit': 'Diamond'}]), 'Hearts')
