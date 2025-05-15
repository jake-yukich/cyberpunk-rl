from markets import CombatUpgradeMarket, EdgerunnersMarket, OpportunitiesMarket
from district import District
from net import TheNet

class Board:
    def __init__(self, players: int):
        self.combat_upgrade_market = CombatUpgradeMarket()
        self.edgerunners_market = EdgerunnersMarket()
        self.opportunities_market = OpportunitiesMarket()
        self.the_net = TheNet()
        self.street_cred = {}
        self.story_card_slots = []
        self.districts = {
            "City Center": District("City Center"),
            "Heywood": District("Heywood"),
            "Pacifica": District("Pacifica"),
            "Santo Domingo": District("Santo Domingo"),
            "Watson": District("Watson"),
            "Westbrook": District("Westbrook")
        }
        self.neighbors = {
            "City Center": {"Heywood", "Watson", "Westbrook"},
            "Heywood": {"City Center", "Pacifica", "Santo Domingo", "Westbrook"},
            "Pacifica": {"Heywood", "Santo Domingo"},
            "Santo Domingo": {"Heywood", "Pacifica", "Santo Domingo"},
            "Watson": {"City Center", "Westbrook"},
            "Westbrook": {"City Center", "Heywood", "Santo Domingo", "Watson"}
        }
