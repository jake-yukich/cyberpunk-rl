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

class District:
    def __init__(self, name: str):
        self.name = name
        self.pois = []
        self.control = None
        self.rewards = []

class POI:
    def __init__(self, name: str):
        self.name = name

class Fixer(POI):
    def __init__(self, name: str):
        super().__init__(name)

class Business(POI):
    def __init__(self, name: str):
        super().__init__(name)

class DataFortress(POI):
    def __init__(self, name: str):
        super().__init__(name)

class Market:
    def __init__(self):
        self.deck = []

class CombatUpgradeMarket(Market):
    def __init__(self):
        pass

class EdgerunnersMarket(Market):
    def __init__(self):
        pass

class OpportunitiesMarket(Market):
    def __init__(self):
        pass

class TheNet:
    pass

class CombatUpgrade:
    pass

class Opportunity:
    pass

class Edgerunner:
    pass