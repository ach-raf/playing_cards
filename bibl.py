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
            return Card(temp_card)
        except IndexError:
            return False

    def __str__(self):
        """Format: the suit on the left and number on the right"""
        return 'Hand: {}'.format(self.hand)

    def __repr__(self):
        return self.__str__()


class Board:
    def __init__(self, card):
        self.board = []
        self.board.append(card)
        self.last_card = card
        self.current_suit = card.suit
        self.current_number = card.number

    def add_card(self, card):
        self.board.append(card)
        self.last_card = card
        self.current_suit = card.suit
        self.current_number = card.number

    def clear(self):
        self.board = []

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
        self.length = 40
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
            self.length -= 1
            return self.cards.pop(len(self.cards) - 1)
        except IndexError:
            return False

    def re_shuffle(self, my_board):
        random.shuffle(my_board)
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
    temp_player_count = 0
    for indx in range(number_of_players):
        my_players.append(Player(temp_player_count))
        temp_player_count += 1
        for num_of_cards in range(5):
            my_players[indx].add_card(my_deck.get_card())

    return my_deck, my_board, my_players


def show_players(my_players):
    player_num = 0
    for temp_player in my_players:
        print('Player {}: {}'.format(player_num, temp_player.hand))
        player_num += 1


def show_info(my_board):
    print(my_board)


def next_turn():
    global current_player
    global current_turn
    if current_player == len(players) - 1:
        current_player = 0
    else:
        current_player += 1
    current_turn += 1


deck, board, players = setup_game()

print(deck)
# show_players(players)
print(board)

current_player = 0
current_turn = 0
end_game = False
while not end_game:
    print('player {} : {}'.format(current_player, players[current_player]))
    card_choice = int(
        input('player {0} turn : write the index of the card you wanna play and 0 to draw a card : '.format(
            current_player)))
    if card_choice == 0:
        if deck.get_card():
            chosen_card = deck.get_card()
        else:
            deck.re_shuffle(board)
            board.clear()
            chosen_card = deck.get_card()
        players[current_player].add_card(chosen_card)
        print('adding {0} to your hand'.format(chosen_card))

    else:
        if players[current_player].throw_card(card_choice):
            chosen_card = players[current_player].throw_card(card_choice)
            if chosen_card.is_special():
                print('special')
            else:
                board.add_card(chosen_card)

    show_info(board)
    next_turn()
