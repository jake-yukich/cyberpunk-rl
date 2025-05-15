"""TODO"""

MAELSTROM = "Maelstrom"
TYGER_CLAWS = "Tyger Claws"
VALENTINOS = "Valentinos"
VOODOO_BOYS = "Voodoo Boys"

class TheNet:
    """
    NETRUNNER ACTIVATION
        DATA FORTRESS CONTROL NOT REQUIRED
        GAIN 1 📁 PER DATA FORTRESS CONTROLLED
    """
    def __init__(self):
        self.the_net = [
            "START",
            "NETWATCH ROLL 4-\nKICK ALL FRIENDLY UNITS OUT OF EVERY DATA FORTRESS.",
            "GAIN 1 STREET CRED.",
            "AN OPPONENT DISCARDS 1 RANDOM COMBAT CARD.",
            "NETWATCH ROLL 5-\nSACRIFICE 1 FRIENDLY NETRUNNER.",
            "MOVE 1 OPPOSING UNIT.",
            "GAIN 1 STREET CRED, 1 FRIENDLY TECHIE MAY BUILD UP TO 2 DRONES.",
            "NETWATCH ROLL 7-\nSACRIFICE ALL FRIENDLY NETRUNNERS.",
            "GAIN 1 STREET CRED.\nKILL ANY 1 UNIT.",
            "GAIN 2 STREET CRED.\nCONVERT ANY 1 OPPOSING UNIT." # reset net token at the end of this netrun
        ]
        self.net_tokens = {
            MAELSTROM: 0,
            TYGER_CLAWS: 0,
            VALENTINOS: 0,
            VOODOO_BOYS: 0,
        }
    
    def netwatch(self, n: int, roll: int):
        pass

