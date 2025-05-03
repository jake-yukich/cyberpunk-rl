"""TODO: playable gangs"""

class Unit:
    pass

# class Solo(Unit):
#     pass

# # ... techies and other units...

class Gang:
     def __init__(self):
          self.name = None

          self.solos = []
          self.techies = []
          self.drones = []
          self.netrunners = []

          self.street_cred = 0
          self.eurodollars = 0
          self.contraband = 0
          self.corporate_secrets = 0

          self.actions = {
               "available": [],
               "reclaim": [],
          }

          self.starting_district = None
          self.abilities = {}
          self.hideouts = {}

class TygerClaws(Gang):
     pass

class Valentinos(Gang):
     pass

class VoodooBoys(Gang):
     pass

class Maelstrom(Gang):
     pass