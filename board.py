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

class District:
    def __init__(self, name: str):
        self.name = name
        self.pois = []
        self.rewards = []
        self.presence = []
        self.dominance = None

        self._pois()

    def _poi(self):
        if self.name == "City Center" or self.name == "Heywood":
            self.pois.append(Fixer(self.name))
            self.pois.append(DataFortress(self.name))
        elif self.name == "Santo Domingo" or self.name == "Watson":
            self.pois.append(Business(self.name))
            self.pois.append(DataFortress(self.name))
        else:
            self.pois.append(Business(self.name))
            self.pois.append(Fixer(self.name))

class POI:
    def __init__(self, name: str):
        self.name = name
        self.is_occupied = False
        self.occupant = None

class Fixer(POI):
    def __init__(self, name: str):
        super().__init__(name)

    def hire_edgerunner(self):
        pass

class Business(POI):
    def __init__(self, name: str):
        super().__init__(name)

    def seize_opportunity(self):
        pass

class DataFortress(POI):
    def __init__(self, name: str):
        super().__init__(name)

    def add_corporate_secrets(self):
        pass

class Market:
    def __init__(self):
        self.deck = []

class CombatUpgradeMarket(Market):
    def __init__(self):
        super().__init__()

class EdgerunnersMarket(Market):
    def __init__(self):
        super().__init__()

class OpportunitiesMarket(Market):
    def __init__(self):
        super().__init__()

class TheNet:
    pass

class CombatUpgrade:
    pass

class Opportunity:
    pass
