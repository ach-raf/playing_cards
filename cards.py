import random


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        """Format: the suit on the left and number on the right"""
        result = '[{0}, {1}]'.format(self.suit, self.number)
        return result

    def __repr__(self):
        return self.__str__()


def setup_deck():
    suits = ['gold', 'sword', 'cup', 'club']

    cards = {'gold': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12],
             'sword': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12],
             'cup': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12],
             'club': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]}

    random.shuffle(cards['gold'])
    random.shuffle(cards['sword'])
    random.shuffle(cards['cup'])
    random.shuffle(cards['club'])

    deck = []
    while len(deck) != 40:
        suit = random.choice(suits)
        if len(cards[suit]) == 1:
            num = cards[suit].pop(0)
            suits.remove(suit)
        else:
            num = cards[suit].pop(0)
        card = Card(suit, num)
        deck.append(card)

    shuffle_deck(deck)
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)


def check_suit(card):
    if card.suit == current_suit:
        return True
    else:
        return False


def check_number(card):
    if card.number == current_number:
        return True
    else:
        return False


def card_is_playable(card):
    if check_suit(card) or check_number(card):
        return True
    else:
        return False


def card_is_special(card):
    if card.number in special_cards:
        return True
    else:
        return False


def show_info():
    print('board', board)
    print('current suit : ', current_suit)
    print('current number : ', current_number)


# def next_turn():
special_cards = [1, 2, 7]

my_deck = setup_deck()
players = {'One': [], 'Two': []}

while len(players['Two']) < 5:
    players['One'].append(my_deck.pop(len(my_deck) - 1))
    players['Two'].append(my_deck.pop(len(my_deck) - 1))

print(my_deck)

board = []

first_card = random.choice(my_deck)
while first_card.number in special_cards:
    first_card = random.choice(my_deck)
my_deck.remove(first_card)
board.append(first_card)
current_suit = first_card.suit
current_number = first_card.number
show_info()

current_player = 'One'
turn = 1
end_game = True
while True:
    if turn % 2 == 0:
        current_player = 'Two'
        print('player two ', players['Two'])
    else:
        current_player = 'One'
        print('player one ', players['One'])
    card_choice = int(
        input('player {0} turn : write the index of the card you wanna play and 0 to draw a card :'.format(
            current_player))) - 1
    chosen_card = players[current_player][card_choice]
    if card_is_playable(chosen_card):
        print(chosen_card)
        players[current_player].remove(chosen_card)
        board.append(chosen_card)
        current_suit = chosen_card.suit
        current_number = chosen_card.number
        print('===========\n')
        show_info()
        print('===========\n')
        turn += 1
    else:
        print('cant play that')
