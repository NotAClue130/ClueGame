mapping_from_character_to_locations={
    "Miis Scarlet": (0,3),
    "Prof Plum": (1,0),
    "Col Mustard": (1,4),
    "Mrs Peacock": (3,0),
    "Mr Green": (4,1),
    "Mrs White": (4,3)
}
class Character:
    def __init__(self,id,startingLocation,icon,name):
        self.id=id
        self.startingLocation=startingLocation
        self.icon=icon
        self.name=name
