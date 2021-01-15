from random import shuffle, randint
from math import floor


class Symbol:
    """
    Class Symbol, which refers to the symbol of a card
    containing two attributes
    -attribute color that can hold either the string value red or the string value black
    -attribute icon that holds one of the string values in list [♥, ♦, ♣, ♠]
    """

    def __init__(self, icon):  # constructor class Symbol
        self.icon = icon
        if self.icon == '♥' or self.icon == '♦':
            self.color = 'red'
        else:
            self.color = 'black'


class Card(Symbol):
    """
    Class Card that inherits from the class Symbol
    containing 3 attributes (color, icon, value) which define a standard playing card
    -attributes color and icon are inherited from super class Symbol
    -attribute value that holds one of the string values in ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']
    """

    def __init__(self, icon,
                 value):  # constructor class Card which inherits from class Symbol attributes color and icon
        super().__init__(icon)
        self.value = value

    def __eq__(self, other):  # method to check if two cards are the same
        if not isinstance(other, Card):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.icon == other.icon and self.value == other.value


class Deck:
    """
    Class Deck contains all the 52 cards of a standard playing deck
    containing one atrribute
    -attribute cards which is a list of instances of class Card
    """

    def __init__(self):  # constructor of class Deck
        self.cards = []

    def fill_deck(self):  # method of class Deck that fills the attribute cards with an entire deck of 52 Card instances
        icon = ['♥', '♦', '♣', '♠']
        value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in icon:
            for j in value:
                self.cards.append(Card(i, j))

    def shuffle(self):  # method of class Deck that will shuffle the list of cards
        shuffle(self.cards)

    def distribute(self, players):  # method of class Deck that will evenly distribute cards between players
        number_of_players = len(players)
        number_of_rounds = floor(52 / number_of_players)  # all players will get same number of cards
        total_number_of_cards = 52
        for i in range(number_of_rounds):
            for j in players:
                distribute_card = randint(0, total_number_of_cards - 1)
                j.cards.append(self.cards.pop(distribute_card))
                j.number_of_cards += 1
                total_number_of_cards -= 1
