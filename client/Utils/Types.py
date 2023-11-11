class Room:
    def __init__(self, Id: int, isHallway: bool, location: str):
        self.Id = Id
        self.isHallway = isHallway
        self.location = location


class Gameboard:
    def __init__(self):
        room_names = ["study", "hall", "lounge", "library", "billiard", "dining", "conservatory", "ballroom", "kitchen"]
        hallway_names = ["StudyHall", "LoungeHall", "StudyLibrary", "BilliardHall", "DiningLounge", "LibraryBilliard", 
                         "BilliardDining", "LibraryConservatory", "BilliardBall", "DiningKitchen", "ConservatoryBall", "KitchenBall"]
        rooms = {name: Room(i * 2 + 1, False, name) for i, name in enumerate(room_names)}
        hallways = [Room(i * 2 + 2, True, name) for i, name in enumerate(hallway_names)]
        self.layout = {rooms["study"]: [rooms["library"], rooms["hall"], hallways[0], hallways[2]],
                       rooms["hall"]: [rooms["study"], rooms["billiard"], rooms["lounge"], hallways[0], hallways[1], hallways[3]],
                       rooms["lounge"]: [rooms["hall"], rooms["dining"], hallways[1], hallways[4]],
                       rooms["library"]: [rooms["study"], rooms["billiard"], rooms["conservatory"], hallways[2], hallways[5], hallways[7]],
                       rooms["billiard"]: [rooms["hall"], rooms["library"], rooms["dining"], rooms["ballroom"], hallways[3], hallways[5], hallways[6], hallways[8]],
                       rooms["dining"]: [rooms["billiard"], rooms["lounge"], rooms["kitchen"], hallways[4], hallways[6], hallways[9]],
                       rooms["conservatory"]: [rooms["library"], rooms["billiard"], hallways[7], hallways[10]],
                       rooms["ballroom"]: [rooms["conservatory"], rooms["billiard"], rooms["kitchen"], hallways[8] , hallways[10], hallways[11]],
                       rooms["kitchen"]: [rooms["ballroom"], rooms["dining"], hallways[9] , hallways[11]]}