__author__ = "7987847, Werner, 7347119, Fajst, 1234567, dalimeli"

def create_cards():
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
                'Queen', 'King']
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

    card_deck = []

    for suit in suits:
        for rank in ranks:
            card = f'{rank} of {suit}'
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


card_deck = create_cards()
print(card_deck)

print(deal_cards(card_deck, 5, 5))
