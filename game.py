__author__ = "7987847, Werner, 7347119, Fajst, 1234567, dalimeli"

RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

def create_cards():

    card_deck = []

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
    temp_cards = []
    for player in range(players):
        temp_cards.append([])
        for card in range(cards_per_player):
            temp_cards[player].append(card_deck.pop(0))
    while len(temp_cards) < 5:
        temp_cards.append([])

    return (temp_cards[0], temp_cards[1], temp_cards[2], temp_cards[3], temp_cards[4])


def compare_cards(cards_to_compare:list):
    '''
    Compares the given cards and returns the winner

    input:
        - cards_to_compare: list
            list of cards to compare
    output:
        - winner: int
            index of the winning card
    '''
    winner = 0
    # TODO: wtf is Trumpffarbe? help
    # Trumpffarbe-condition muss auch noch implementiert werden
    for i in range(1, len(cards_to_compare)):
        if RANKS.index(cards_to_compare[i]['rank']) > RANKS.index(cards_to_compare[winner]['rank']):
            winner = i
        if RANKS.index(cards_to_compare[i]['rank']) == RANKS.index(cards_to_compare[winner]['rank']):
            if SUITS.index(cards_to_compare[i]['suit']) > SUITS.index(cards_to_compare[winner]['suit']):
                winner = i
    return winner



card_deck = create_cards()
print(card_deck)

print(deal_cards(card_deck, 5, 5))
