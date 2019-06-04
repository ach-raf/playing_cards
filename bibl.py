import random


class Card:
    def __init__(self):
        print('Card created')

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def is_special(self):
        if self.number in [1, 2, 7]:
            return True
        else:
            return False

    def __str__(self):
        """Format: the suit on the left and number on the right"""
        result = '[{0}, {1}]'.format(self.suit, self.number)
        return result

    def __repr__(self):
        return self.__str__()


class Player:
    def __init__(self, label):
        self.label = label
        self.hand = []
        self.num_cards_left = len(self.hand)
        self.last_card = Card()

    def add_card(self, card):
        self.hand.append(card)

    def add_cards(self, cards):
        [self.hand.append(card) for card in cards]

    def select_card(self, card_index):
        try:
            return self.hand[card_index]
        except IndexError:
            return False

    def throw_card(self, card_index):
        try:
            # remove the card from the hand of the player and storing it in temp_card
            temp_card = self.hand.pop(card_index)
            # last played card by a player
            self.last_card = temp_card
            return temp_card
        except IndexError:
            return False


class Board:
    def __init__(self, last_card):
        self.board = []
        self.last_card = last_card

    def add_card(self, card):
        self.board.append(card)

    def clear(self):
        self.board = []


class Deck:
    def __init__(self):
        self.deck = []
        suits = ['gold', 'sword', 'cup', 'club']
        cards = {'gold': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12],
                 'sword': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12],
                 'cup': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12],
                 'club': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]}

        random.shuffle(cards['gold'])
        random.shuffle(cards['sword'])
        random.shuffle(cards['cup'])
        random.shuffle(cards['club'])

        while len(self.deck) != 40:
            suit = random.choice(suits)
            if len(cards[suit]) == 1:
                num = cards[suit].pop(0)
                suits.remove(suit)
            else:
                num = cards[suit].pop(0)
            card = Card(suit, num)
            self.deck.append(card)

        random.shuffle(self.deck)

    def get_card(self):
        try:
            return self.deck.pop(len(self.deck))
        except IndexError:
            return False

    def re_shuffle(self, board):
        [self.deck.append(card) for card in board]
        
    

