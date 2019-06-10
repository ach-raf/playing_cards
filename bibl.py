import random


class Card:

    def __init__(self, suit='x', number=-1):
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
        self.last_card_played = Card()

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
            self.last_card_played = temp_card
            return temp_card
        except IndexError:
            return False

    def __str__(self):
        """Format: the suit on the left and number on the right"""
        return 'Hand: {}'.format(self.hand)

    def __repr__(self):
        return self.__str__()


class Board:
    def __init__(self, last_card):
        self.board = []
        self.board.append(last_card)
        self.last_card = last_card
        self.current_suit = last_card.suit
        self.current_number = last_card.number

    def add_card(self, card):
        self.board.append(card)

    def clear(self):
        self.board = []

    """def last_card

    def current_suit(self):
        return self.current_suit

    def current_number(self):
        return self.current_number"""

    def __str__(self):
        """Format: the suit on the left and number on the right"""
        return 'Board: {}\nLast Card: {}\nCurrent Suit: {}\nCurrent Number: {}'.format(self.board, self.last_card,
                                                                                       self.current_suit,
                                                                                       self.current_number)

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self.cards = []
        self.len = 40
        suits = ['gold', 'sword', 'cup', 'club']
        default_cards = {'gold': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12],
                         'sword': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12],
                         'cup': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12],
                         'club': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]}

        random.shuffle(default_cards['gold'])
        random.shuffle(default_cards['sword'])
        random.shuffle(default_cards['cup'])
        random.shuffle(default_cards['club'])

        while len(self.cards) != 40:
            suit = random.choice(suits)
            if len(default_cards[suit]) == 1:
                num = default_cards[suit].pop(0)
                suits.remove(suit)
            else:
                num = default_cards[suit].pop(0)
            card = Card(suit, num)
            self.cards.append(card)

        random.shuffle(self.cards)

    def get_card(self):
        try:
            self.len -= 1
            return self.cards.pop(len(self.cards) - 1)
        except IndexError:
            return False

    def re_shuffle(self, my_board):
        [self.cards.append(card) for card in my_board]

    def __str__(self):
        """Format: the suit on the left and number on the right"""
        return 'Deck:\n{}'.format(self.cards)

    def __repr__(self):
        return self.__str__()


def setup_game():
    my_deck = Deck()
    first_card = my_deck.get_card()
    my_board = Board(first_card)
    number_of_players = int(input('How many players, MAX is 4 '))
    while number_of_players > 4 or number_of_players < 1:
        number_of_players = input('choose between 1 and 4 players')
    my_players = []
    for indx in range(number_of_players):
        my_players.append([])
        for num_of_cards in range(5):
            my_players[indx].append(my_deck.get_card())

    return my_deck, my_board, my_players


deck, board, players = setup_game()

print(deck)
print(players)
print(board)
