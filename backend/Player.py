# Shawn Mai
# 11/11/2023
# This class defines a Player object for clue less

from backend.Card import Card

class Player:
    def __init__(self, id, characterId, name, roomId, hand):
        self.name=name
        self.id = id  #unique player id
        self.characterId = characterId  #unique character id
        self.roomId = roomId  #unqiue room id 
        self.hand = hand  # List of Card objects

    def move(self, new_roomId):
        # Before calling this method, need to check if the room id is valid 
        # Update the roomId if the move is valid
        self.roomId = new_roomId

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

