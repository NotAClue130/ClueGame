# Shawn Mai
# 11/11/2023
# This class defines a Player object for clue less

from backend.Board import Gameboard
from backend.Card import Card

class Player:
    instances_count = 0
    instances_database = []
    def __init__(self, id, characterId, characterName, name, roomId, room, hand):
        Player.checkIdUniqueness(id)
        self.name=name
        self.id = id  #unique player id
        self.characterId = characterId  #unique character id
        self.characterName = characterName
        self.roomId = roomId  #unqiue room id 
        self.room = room
        self.hand = hand  # List of Card objects
        Player.instances_database.append(self)
        Player.instances_count += 1

    def move(self, new_room):
        # Before calling this method, need to check if the room id is valid 
        # Update the roomId if the move is valid
        self.roomId = new_room.id
        self.room = new_room

    def makeSuggestion(self, roomId, suggested_cards):
        # This method return a list of Card objects representing the suggestion
        if self.roomId != roomId:
            raise ValueError("You must make a suggestion for the room you are in.")

        # Check if all card types are different
        card_types = [card.getType() for card in suggested_cards]
        if len(set(card_types)) != len(suggested_cards):
            raise ValueError("All card types must be different for a suggestion.")
        
        return suggested_cards

    def answerSuggestion(self, suggested_cards):
        # Check the player's hand for any of the suggested cards
        # Return the matching card(s)
        for card in self.hand:
            if card in suggested_cards:
                return card
        # Return False if there are no associated cards
        return False

    def makeAccusation(self, accusation_cards):
        # This method return a list of Card objects representing the accusation

        # Check if all card types are different
        card_types = [card.getType() for card in accusation_cards]
        if len(set(card_types)) != len(accusation_cards):
            raise ValueError("All card types must be different for a suggestion.")

        return accusation_cards

    @classmethod
    def getInstanceById(cls, instance_id):
        res = None
        for instance_each in Player.instances_database:
            if instance_each.id == instance_id:
                res = instance_each
        return res

    @classmethod
    def getInstancesDatabase(cls):
        return cls.instances_database

    @classmethod
    def getInstancesCount(cls):
        return cls.instances_count

    @classmethod
    def checkIdUniqueness(cls, id_for_check):
        res = True
        for instance_each in cls.instances_database:
            if instance_each.id == id_for_check:
                res = False
                break
        if not res:
            raise ValueError("The id already exists!")

    @classmethod
    def gethtmlLocal(cls, room):
        x = room.htmlLocation[0]
        y = room.htmlLocation[1]
        middlex = (x[0] + x[1])/2
        middley = (y[0] + y[1])/2
        return (str(middlex) + "px, " + str(middley) + "px")
