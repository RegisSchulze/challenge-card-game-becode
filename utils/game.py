from utils.card import Deck
from math import floor


class Board:
    """
    Class Board, that represents the status of the game
    containing four attributes
    -attribute players that is a list of Player containing all the players
    -attribute turn_count that is an int and keeps record of how many rounds have been played
     a round is done when all players have played one card
    -attribute active_cards is a list of Card containing the last card played by each player
    -attribute history_cards is a list of Card containing all cards that have been played up to this point
     with the exception of the cards in attribute active_cards
    """

    def __init__(self, players):
        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        card_deck = Deck()  # creating an object of type Deck after importing from card.py
        card_deck.fill_deck()  # fill the deck using method fill_deck of Deck
        card_deck.shuffle()  # shuffle the deck using method shuffle of Deck
        card_deck.distribute(self.players)  # distribute the deck among the players, each player gets same amouts
                                            # of cards
        number_of_players = len(self.players)
        number_of_rounds = floor(52 / number_of_players)
        for i in range(number_of_rounds):  # iterate over the number of rounds
            highest_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            highest_value_index = 0
            icon = ['♥', '♦', '♣', '♠']
            icon_index = 0
            player = 0
            for j in range(number_of_players):  # iterate over the number of players
                active_card = self.players[j].play()  # method play of Player is called upon
                if highest_value.index(active_card.value) >= highest_value_index:  # NICE TO HAVE FEATURES
                    highest_value_index = highest_value.index(active_card.value)
                    if icon.index(active_card.icon) >= icon_index:
                        icon_index = icon.index(active_card.icon)
                        winner = player  # winner of the round
                if self.turn_count != 0:  # in the first round no history cards allowed
                    self.history_cards.append(self.active_cards.pop(0))
                self.active_cards.append(active_card)   # the cards that have been played in this round are added to
                                                        # active_cards
                player += 1
            self.players[winner].count += 1  # increase score of winner of the round
            print(f'Player {self.players[winner].name} has won this round')
            self.turn_count += 1
            print(f'The turn count is {self.turn_count}'  #print turn_count
                  f'\nThe list of active cards is')
            for l in range(len(self.active_cards)):  # print the cards in active_cards
                print(f'{self.active_cards[l].value} {self.active_cards[l].icon}')
            print(f'The number of cards in the history_cards is {len(self.history_cards)}')     #print number of cards in
            print("=====================================================================================")                                                                                   # history_cards
        end_winner = 0  # retrieving winner with highest score
        current_winner = 0
        highest_score = 0
        for i in self.players:
            if i.count >= highest_score:
                highest_score = i.count
                end_winner = current_winner
            current_winner += 1
            print(f'Player {i.name} has a score of {i.count}')
        print(f'Player {self.players[end_winner].name} has won the game!')
        print('Well done, the game is finished. Hope you enjoyed it!!!')
