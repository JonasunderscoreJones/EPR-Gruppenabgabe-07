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


card_deck = create_cards()
print(card_deck)
