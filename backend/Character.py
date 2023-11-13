
class Character:
    instances_count = 0
    instances_database = []
    mapping_from_character_to_locations = {
        "Miss Scarlet": (0, 3),
        "Prof Plum": (1, 0),
        "Col Mustard": (1, 4),
        "Mrs Peacock": (3, 0),
        "Mr Green": (4, 1),
        "Mrs White": (4, 3)
    }
    mapping_from_character_to_boolean = {
        "Miss Scarlet": False,
        "Prof Plum": False,
        "Col Mustard": False,
        "Mrs Peacock": False,
        "Mr Green": False,
        "Mrs White": False
    }

    def __init__(self,id,name):
        Character.checkIdUniqueness(id)
        Character.checkCharaterName(name)
        self.id=id
        # self.startingLocation
        # self.icon
        self.name=name
        Character.mapping_from_character_to_boolean[name]=True
        Character.instances_database.append(self)
        Character.instances_count += 1

    @classmethod
    def get_start_locations_of_character(cls, character_name):
        return cls.mapping_from_character_to_locations[character_name]

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

    @classmethod
    def checkCharaterName(cls, characterName):
        if characterName not in cls.mapping_from_character_to_boolean:
            raise ValueError("This character doesn't belong to clue game!!")
        if cls.mapping_from_character_to_boolean[characterName]:
            raise ValueError("This character is already taken up by other users!!")

