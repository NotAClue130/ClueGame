
class Character:
    instances_count = 0
    instances_database = []
    mapping_from_character_to_locations = {
        "Miis Scarlet": (0, 3),
        "Prof Plum": (1, 0),
        "Col Mustard": (1, 4),
        "Mrs Peacock": (3, 0),
        "Mr Green": (4, 1),
        "Mrs White": (4, 3)
    }
    def __init__(self,id,startingLocation,icon,name):
        if not Character.checkIdUniqueness(id):
            raise ValueError("The id already exists!")
        self.id=id
        self.startingLocation=startingLocation
        self.icon=icon
        self.name=name
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
        return res
