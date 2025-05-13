"""Playable gangs. One gang per player."""
from enum import Enum, auto

class Action(Enum):
     ACTIVATE_SOLO = auto()
     ACTIVATE_TECHIES = auto()
     UPGRADE_COMBAT_CARD = auto()
     ACTIVATE_NETRUNNERS = auto()
     BUILD_HIDEOUT = auto()
     ACTION_WILDCARD = auto()

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
               "available": {
                    Action.ACTIVATE_SOLO,
                    Action.ACTIVATE_TECHIES,
                    Action.UPGRADE_COMBAT_CARD,
                    Action.ACTIVATE_NETRUNNERS,
                    Action.BUILD_HIDEOUT,
                    Action.ACTION_WILDCARD,
               },
               "reclaim": {},
          }

          self.abilities = {}
          self.hideouts = {}

class TygerClaws(Gang):
     def __init__(self):
          super().__init__(name="Tyger Claws")
          self.starting_district = WESTBROOK
          self.abilities = {
               "REVENGE",
               "PAYBACK",
          }

class Valentinos(Gang):
     def __init__(self):
          super().__init__(name="Valentinos")
          self.starting_district = HEYWOOD
          self.abilities = {
               "COMMUNITY SUPPORT",
               "PERSONAL OPPORTUNITY",
          }

class VoodooBoys(Gang):
     def __init__(self):
          super().__init__(name="Voodoo Boys")
          self.starting_district = PACIFICA
          self.abilities = {
               "NETWATCH COUNTERMEASURES",
               "MYSTIC NETRUNNERS",
          }

class Maelstrom(Gang):
     def __init__(self):
          super().__init__(name="Maelstrom")
          self.starting_district = WATSON
          self.abilities = {
               "WELL-ARMED",
               "RAGE",
          }
          self.rage_track = 0