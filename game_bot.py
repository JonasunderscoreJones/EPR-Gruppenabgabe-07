__author__ = "7987847, Werner, 7347119, Fajst, 7735965, Melikidze"

class BOT:
    def __init__(self, name, bot_number, cards):
        self.name = name
        self.cards = cards
        self.points = 0
        self.trumpf = False
        self.trumpf_color = None
        self.bot_number = bot_number

    def play_card(self):
        '''
        Plays a card
        output:
            - card: dict
                card to play
        '''
        return self.cards.pop(0)
    
    def add_points(self, points):
        '''
        Adds points to the bot
        input:
            - points: int
                points to add
        '''
        self.points += points

    # Getters
    
    def get_points(self, played_cards):
        '''
        Calculates the points of the played cards
        input:
            - played_cards: list
                list of cards that have been played already
        output:
            - points: int
                points of the played cards
        '''
        points = 0
        for card in played_cards:
            if card['rank'] == 'Jack':
                points += 2
            elif card['rank'] == 'Queen':
                points += 3
            elif card['rank'] == 'King':
                points += 4
            elif card['rank'] == 'Ace':
                points += 11
        return points
    
    def get_trumpf(self, trumpf_color):
        '''
        Sets the trumpf color
        input:
            - trumpf_color: str
                trumpf color
        '''
        self.trumpf = True
        self.trumpf_color = trumpf_color
    
    def get_trumpf_color(self):
        '''
        Returns the trumpf color
        output:
            - trumpf_color: str
                trumpf color
        '''
        return self.trumpf_color

    def get_name(self):
        '''
        Returns the name of the bot
        output:
            - name: str
                name of the bot
        '''
        return self.name

    def get_cards(self):
        '''
        Returns the cards of the bot
        output:
            - cards: list
                list of cards
        '''
        return self.cards

    def get_points(self):
        '''
        Returns the points of the bot
        output:
            - points: int
                points of the bot
        '''
        return self.points

    def get_trumpf(self):
        '''
        Returns if the bot has trumpf
        output:
            - trumpf: bool
                if the bot has trumpf
        '''
        return self.trumpf

    def is_bot(self):
        '''
        Returns if the player is a bot
        output:
            - is_bot: bool
                if the player is a bot
        '''
        return True
    
    def get_bot_number(self):
        '''
        Returns the bot number
        output:
            - bot_number: int
                bot number
        '''
        return self.bot_number

    # Setter

    def set_trumpf(self, trumpf):
        '''
        Sets if the bot has trumpf
        input:
            - trumpf: bool
                if the bot has trumpf
        '''
        self.trumpf = trumpf

    def set_cards(self, cards):
        '''
        Sets the cards of the bot
        input:
            - cards: list
                list of cards
        '''
        self.cards = cards

    def set_points(self, points):
        '''
        Sets the points of the bot
        input:
            - points: int
                points of the bot
        '''
        self.points = points

    def set_trumpf_color(self, trumpf_color):
        '''
        Sets the trumpf color of the bot
        input:
            - trumpf_color: str
                trumpf color of the bot
        '''
        self.trumpf_color = trumpf_color

    def __str__(self):
        return self.name
    