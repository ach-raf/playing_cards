import random


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        if self.number in [1, 2, 7]:
            self.special = True
        else:
            self.special = False

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


class Board:
    def __init__(self, last_card):
        self.board = []
        self.last_card = last_card
