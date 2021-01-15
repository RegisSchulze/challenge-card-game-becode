from random import randint


class Player:
    """
    Class player, that will keep the information about each different player
    containing six attributes
    -extra chosen attribute name which is a String to be able to identify the different players
    -attribute cards which is a list of Card these contain the cards that the player has in his hand
    -attribute turn_count is an int, starting at 0, and keeps track of the number of turns this player has done
    -attribute number_of_cards is an int, starting at 0, and keeps track of the number of cards this player has
    -attribute history which is a list of Card that will contain all the cards played by the player
    -extra chosen attribute count which represent the score of this player
    """

    def __init__(self, name):  # constructor of class Player
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []
        self.count = 0

    def play(self):  # method play of Class Player
        random_card = randint(0, self.number_of_cards-1)  # choose a random card from the player hand
        self.number_of_cards -= 1  # this will lead to one less card in the player hand
        print(f'Player {self.name} has {self.number_of_cards} cards left')
        self.history.append(self.cards.pop(random_card))    #remove the card from list cards and add it to the players
                                                            # history

        print(f'Player {self.name} turn count:{self.turn_count} played following card: {self.history[self.turn_count].value} '
              f'{self.history[self.turn_count].icon}')
        self.turn_count += 1  # increment the turn count now that the play is finished with 1
        return self.history[self.turn_count-1]
