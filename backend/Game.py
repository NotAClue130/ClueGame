# Connor Finn
# 11/11/2023
# This class defines a game object for clue less
from backend.Card import Card
from backend.Deck import Deck
from backend.Board import Gameboard, Room


class Game:

    def __init__(self):
        self.players = []  # this is a list of player object
        self.board = []  # this will be the GameBoard object
        self.cards = Deck()
        self.solution = []
        self.characters = []  # this is a list of character object

    # this method will start the game, after this, no players will be added
    def initializeGame(self):
        # we need to deal the cards to the players
        # build a list of all the player ids
        numPlayers = len(self.players)
        playerIds_temp = list(range(0, numPlayers))

        # deal out the cards
        dealt_cards = self.cards.Deal(playerIds_temp)

        # set the solution
        self.solution = dealt_cards["solution"]

        # set the player hands
        for i1 in range(numPlayers):
            self.players[i1].hand = dealt_cards[i1]

        # initialize each player
        for i1 in range(numPlayers):
            self.players[i1].characterId = self.characters[i1].id

    # this method will execute a turn for a player object
    def turn(self, player):
        # do they want to move

        # can they make a suggestion or accusation

        # does someone need to respsond to the suggestion
        pass

    # this method will add a player to the Game object
    def addPlayer(self, player):
        self.players.append(player)

    # compare the guess with the stored solution
    def checkSolution(guess):
        pass

    def get_player_object_based_on_player_name(self, name):
        for player in self.players:
            if player.name==name:
                return player
