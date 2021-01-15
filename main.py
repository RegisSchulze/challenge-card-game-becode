from utils.game import Board
from utils.player import Player
from copy import deepcopy

all_player_names = []  # list of strings containing the names of all players
list_of_players = []  # list of all players of type Player
number_of_players = int(input('How may players?'))

for i in range(number_of_players):  # add name of players to list all_player_names
    all_player_names.append(input('What is your name?'))

for i in range(number_of_players):  # creating the list list_of_players of type Player
    k = Player(all_player_names[i])
    list_of_players.append(k)

player_board = Board(list_of_players)  #creating object of type Board from game.py
player_board.start_game()  #method start_game from class Board





