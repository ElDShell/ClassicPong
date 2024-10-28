from view import get_names
from game import start_game
from player import Player
player1_name,player2_name = get_names()

player1 = Player(player1_name)
player2 = Player(player2_name)
start_game(player1,player2)
