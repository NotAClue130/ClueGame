class Room:
    instances_count = 0
    instances_database = []
    room_names = ["study", "hall", "lounge", "library", "billiard", "dining", "conservatory", "ballroom", "kitchen"]
    hallway_names = ["StudyHall", "HallLounge", "StudyLibrary", "HallBilliard", "LoungeDining", "LibraryBilliard",
                     "BilliardDining", "LibraryConservatory", "BilliardBall", "DiningKitchen", "ConservatoryBall",
                     "BallKitchen"]
    mapping_from_name_to_boolean = {name: False for name in room_names + hallway_names}

    def __init__(self, Id: int, isHallway: bool, name: str):
        Room.checkName(name)
        Room.checkIdUniqueness(id)
        self.Id = Id
        self.isHallway = isHallway
        self.name = name
        # Hi David, I believe that "name" is a better name for this attribute than "location", because it is a string
        # What is more, consider that we have function get_room_by_name
        Room.instances_database.append(self)
        Room.instances_count += 1

    @classmethod
    def checkName(cls, name):
        res = False
        if name in cls.room_names:
            res = True
        if name in cls.hallway_names:
            res = True
        if not res:
            raise ValueError("The room name doesn't belong the game ClueLess!")
        if cls.mapping_from_name_to_boolean[name]:
            raise ValueError("The room name is already taken up by other rooms")

    @classmethod
    def getInstanceById(cls, instance_id):
        res = None
        for instance_each in cls.instances_database:
            print(instance_each.id)
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


class Gameboard:
    def __init__(self):
        # Initialize all rooms and hallways
        room_names = ["study", "hall", "lounge", "library", "billiard", "dining", "conservatory", "ballroom", "kitchen"]
        hallway_names = ["StudyHall", "HallLounge", "StudyLibrary", "HallBilliard", "LoungeDining", "LibraryBilliard",
                         "BilliardDining", "LibraryConservatory", "BilliardBall", "DiningKitchen", "ConservatoryBall",
                         "BallKitchen"]
        # We follow the rule of "from left to right, from up to below" to give hallway their names
        # For example, the hallway between Hall and Billiary should be "HallBilliard", not "BilliardHall"
        self.rooms = {name: Room(i * 2 + 1, False, name) for i, name in enumerate(room_names)}
        self.hallways = [Room(i * 2 + 2, True, name) for i, name in enumerate(hallway_names)]

        self.htmlLayout = {"study": [(96, 239), (138, 255)], "hall": [(312, 482), (138, 255)],
                           "lounge": [(555, 698), (138, 255)], "library": [(96, 239), (335, 486)]
            , "billiard": [(312, 482), (335, 486)], "dining": [(555, 698), (335, 486)],
                           "conservatory": [(96, 239), (555, 685)], "ballroom": [(312, 482), (555, 685)],
                           "kitchen": [(555, 698), (555, 685)]}
        self.htmlSecretPassageLayout = {"kitchen": [(100, 150), (143, 195)], "conservatory": [(630, 688), (147, 210)],
                                        "lounge": [(105, 155), (627, 678)], "study": [(640, 690), (633, 676)]}
        self.htmlHallLayout = {"StudyHall": [(241, 313), (161, 223)], "HallLounge": [(482, 555), (161, 223)],
                               "StudyLibrary": [(120, 192), (270, 334)], "HallBilliard": [(362, 433), (270, 334)],
                               "LoungeDining": [(600, 675), (270, 334)], "LibraryBilliard": [(241, 313), (379, 445)],
                               "BilliardDining": [(482, 555), (375, 445)],
                               "LibraryConservatory": [(120, 192), (490, 554)],
                               "BilliardBall": [(362, 433), (490, 554)], "DiningKitchen": [(600, 675), (490, 554)],
                               "ConservatoryBall": [(241, 313), (600, 665)], "BallKitchen": [(482, 555), (600, 665)]}
        self.layout = {
            self.rooms["study"]: [self.rooms["library"], self.rooms["hall"], self.rooms["kitchen"], self.hallways[0],
                                  self.hallways[2]],
            self.rooms["hall"]: [self.rooms["study"], self.rooms["billiard"], self.rooms["lounge"], self.hallways[0],
                                 self.hallways[1], self.hallways[3]],
            self.rooms["lounge"]: [self.rooms["hall"], self.rooms["dining"], self.rooms["conservatory"],
                                   self.hallways[1], self.hallways[4]],
            self.rooms["library"]: [self.rooms["study"], self.rooms["billiard"], self.rooms["conservatory"],
                                    self.hallways[2], self.hallways[5], self.hallways[7]],
            self.rooms["billiard"]: [self.rooms["hall"], self.rooms["library"], self.rooms["dining"],
                                     self.rooms["ballroom"], self.hallways[3], self.hallways[5], self.hallways[6],
                                     self.hallways[8]],
            self.rooms["dining"]: [self.rooms["billiard"], self.rooms["lounge"], self.rooms["kitchen"],
                                   self.hallways[4], self.hallways[6], self.hallways[9]],
            self.rooms["conservatory"]: [self.rooms["library"], self.rooms["billiard"], self.rooms["lounge"],
                                         self.hallways[7], self.hallways[10]],
            self.rooms["ballroom"]: [self.rooms["conservatory"], self.rooms["billiard"], self.rooms["kitchen"],
                                     self.hallways[8], self.hallways[10], self.hallways[11]],
            self.rooms["kitchen"]: [self.rooms["ballroom"], self.rooms["dining"], self.rooms["study"], self.hallways[9],
                                    self.hallways[11]]}

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

    def get_room_by_name(self, room_name):
        # Check in rooms
        for room in self.rooms.values():
            if room.name == room_name:
                return room

        # Check in hallways
        for room in self.hallways:
            if room.name == room_name:
                return room

        # If no room is found
        return None

    # Determines where user clicked on board and returns the room, hall, or secret passage
    def determine_html_location(self, x, y):
        for room in self.htmlLayout.items():
            location = room[1]
            if (location[0][0] <= x <= location[0][1] and location[1][0] <= y <= location[1][1]):
                if (room[0] == "study" or room[0] == "lounge" or room[0] == "conservatory" or room[0] == "kitchen"):
                    for secret in self.htmlSecretPassageLayout.items():
                        secretpassage = secret[1]
                        if (secretpassage[0][0] <= x <= secretpassage[0][1] and secretpassage[1][0] <= y <=
                                secretpassage[1][1]):
                            return secret[0]
                        else:
                            return room[0]
                else:
                    return room[0]
        for halls in self.htmlHallLayout.items():
            hallLocation = halls[1]
            if (hallLocation[0][0] <= x <= hallLocation[0][1] and hallLocation[1][0] <= y <= hallLocation[1][1]):
                return halls[0]
        return

#       Layout Graph
# Study         Hall       Lounge
# Library       Billiard   Dining
# Conservatory  Ballroom   Kitchen
