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

    def is_playable(self, my_board):
        if self.suit == my_board.current_suit or self.number == my_board.current_number:
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
        self.last_card_played = Card()

    def num_cards(self):
        return len(self.hand)

    def add_card(self, card):
        self.hand.append(card)

    def add_cards(self, cards):
        [self.hand.append(card) for card in cards]

    def select_card(self, card_index):
        try:
            return self.hand[card_index - 1]
        except IndexError:
            return False

    def throw_card(self, card_index):
        # remove the card from the hand of the player and storing it in temp_card
        temp_card = self.hand.pop(card_index - 1)
        # last played card by a player
        self.last_card_played = temp_card
        return temp_card

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

    def get_first_card(self):
        found = False
        while not found:
            temp_card = self.cards[len(self.cards) - 1]
            if temp_card.number not in [1, 2, 7]:
                found = True
                self.cards.pop(len(self.cards) - 1)
                return temp_card
            else:
                random.shuffle(self.cards)

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
    first_card = my_deck.get_first_card()
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


def compare_cards(card_one, card_two):
    if card_one.suit == card_two.suit or card_one.number == card_two.number:
        return True
    else:
        return False


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


def draw_card():
    global chosen_card
    chosen_card = deck.get_card()
    if not chosen_card:
        deck.re_shuffle(board)
        board.clear()
        chosen_card = deck.get_card()
    players[current_player].add_card(chosen_card)
    print('adding {0} to your hand'.format(chosen_card))


deck, board, players = setup_game()

print(deck)
# show_players(players)
print(board)

current_player = 0
current_turn = 0
correct_answer = False
end_game = False
SUITS = ['gold', 'sword', 'cup', 'club']
while not end_game:
    while not correct_answer:
        print('player {} : {}'.format(current_player, players[current_player]))
        card_choice = int(
            input('player {0} turn : write the index of the card you wanna play and 0 to draw a card : '.format(
                current_player)))
        if card_choice == 0:
            correct_answer = True
            draw_card()
        else:
            selected_card = players[current_player].select_card(card_choice)
            if selected_card.is_playable(board):
                correct_answer = True
                chosen_card = players[current_player].throw_card(card_choice)
                print('Played Card: ', chosen_card)
                if chosen_card.is_special():
                    if chosen_card.number == 7:
                        suit_choice = -1
                        while suit_choice not in range(4):
                            suit_choice = int(
                                input(
                                    'player {0} Choose a suit:\n0 : gold\n1 : swords'
                                    '\n2 : cups\n3 : clubs\nYour choice : '.format(
                                        current_player)))
                        board.add_card(chosen_card)
                        board.current_suit = SUITS[suit_choice]
                else:
                    board.add_card(chosen_card)
        show_info(board)
        if players[current_player].num_cards() == 0:
            print('player {} Wins'.format(current_player))
            end_game = True
        else:
            next_turn()
