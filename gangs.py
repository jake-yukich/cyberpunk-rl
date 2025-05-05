"""TODO: playable gangs"""

HEYWOOD = "Heywood"
PACIFICA = "Pacifica"
WATSON = "Watson"
WESTBROOK = "Westbrook"

class Gang:
     def __init__(self, name: str):
          self.name = name

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

          self.abilities = {}
          self.hideouts = {}

class TygerClaws(Gang):
     def __init__(self):
          super().__init__(name="Tyger Claws")
          self.starting_district = WESTBROOK

          self.actions["available"] = [
               "Activate Solo",
               "Activate Techies",
               "Upgrade a Combat Card",
               "Activate Netrunners",
               "Build a Hideout",
               "Action Wildcard",
          ]

          self.abilities = {
               "REVENGE",
               "PAYBACK",
          }

class Valentinos(Gang):
     def __init__(self):
          super().__init__(name="Valentinos")
          self.starting_district = HEYWOOD

          self.actions["available"] = [
               "Activate Solo",
               "Activate Techies",
               "Upgrade a Combat Card",
               "Activate Netrunners",
               "Build a Hideout",
               "Action Wildcard",
          ]

          self.abilities = {
               "COMMUNITY SUPPORT",
               "PERSONAL OPPORTUNITY",
          }

class VoodooBoys(Gang):
     def __init__(self):
          super().__init__(name="Voodoo Boys")
          self.starting_district = PACIFICA

          self.actions["available"] = [
               "Activate Solo",
               "Activate Techies",
               "Upgrade a Combat Card",
               "Activate Netrunners",
               "Build a Hideout",
               "Action Wildcard",
          ]

          self.abilities = {
               "NETWATCH COUNTERMEASURES",
               "MYSTIC NETRUNNERS",
          }

class Maelstrom(Gang):
     def __init__(self):
          super().__init__(name="Maelstrom")
          self.starting_district = WATSON

          self.actions["available"] = [
               "Activate Solo",
               "Activate Techies",
               "Upgrade a Combat Card",
               "Activate Netrunners",
               "Build a Hideout",
               "Action Wildcard",
          ]

          self.abilities = {
               "WELL-ARMED",
               "RAGE",
          }
          self.rage_track = 0