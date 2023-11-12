class Room:
    def __init__(self, Id: int, isHallway: bool, location: str):
        self.Id = Id
        self.isHallway = isHallway
        self.location = location


class Gameboard:
    def __init__(self):
        # Initialize all rooms and hallways
        room_names = ["study", "hall", "lounge", "library", "billiard", "dining", "conservatory", "ballroom", "kitchen"]
        hallway_names = ["StudyHall", "LoungeHall", "StudyLibrary", "BilliardHall", "DiningLounge", "LibraryBilliard", 
                         "BilliardDining", "LibraryConservatory", "BilliardBall", "DiningKitchen", "ConservatoryBall", "KitchenBall"]
        self.rooms = {name: Room(i * 2 + 1, False, name) for i, name in enumerate(room_names)}
        self.hallways = [Room(i * 2 + 2, True, name) for i, name in enumerate(hallway_names)]
    
    def createLayout(self):
        # Create the Layout in a Graph
        self.layout = {self.rooms["study"]: [self.rooms["library"], self.rooms["hall"], self.rooms["kitchen"], self.hallways[0], self.hallways[2]],
                       self.rooms["hall"]: [self.rooms["study"], self.rooms["billiard"], self.rooms["lounge"], self.hallways[0], self.hallways[1], self.hallways[3]],
                       self.rooms["lounge"]: [self.rooms["hall"], self.rooms["dining"], self.rooms["conservatory"], self.hallways[1], self.hallways[4]],
                       self.rooms["library"]: [self.rooms["study"], self.rooms["billiard"], self.rooms["conservatory"], self.hallways[2], self.hallways[5], self.hallways[7]],
                       self.rooms["billiard"]: [self.rooms["hall"], self.rooms["library"], self.rooms["dining"], self.rooms["ballroom"], self.hallways[3], self.hallways[5], self.hallways[6], self.hallways[8]],
                       self.rooms["dining"]: [self.rooms["billiard"], self.rooms["lounge"], self.rooms["kitchen"], self.hallways[4], self.hallways[6], self.hallways[9]],
                       self.rooms["conservatory"]: [self.rooms["library"], self.rooms["billiard"], self.rooms["lounge"], self.hallways[7], self.hallways[10]],
                       self.rooms["ballroom"]: [self.rooms["conservatory"], self.rooms["billiard"], self.rooms["kitchen"], self.hallways[8] , self.hallways[10], self.hallways[11]],
                       self.rooms["kitchen"]: [self.rooms["ballroom"], self.rooms["dining"], self.rooms["study"], self.hallways[9] , self.hallways[11]]}
        
    def get_room_by_id(self, room_id):
        # Check in rooms
        for room in self.rooms.values():
            if room.Id == room_id:
                return room

        # Check in hallways
        for room in self.hallways:
            if room.Id == room_id:
                return room

        # If no room is found
        return None