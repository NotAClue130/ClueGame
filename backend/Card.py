# Connor Finn
# 11/11/2023
# This class defines a card object according to the design specifications doc

class Card:
  def __init__(self, id, type, name):
    self.name = name        # e.g. Mr Green, candlestick, 
    self.type = type        # 'room', 'person', 'weapon'
    self.id = id            # unique ID. This should not be changed


# set a couple of getters. This is not explicetely necessary for python
# but I wanted to set the interface.
  def getType(self):
    return self.type

  def getName(self):
    return self.name
  
  def getId(self):
    return self.id