"""
Opportunities are underground deals that Gangs can fulfill.
They cost Contraband 📦 to be seized and often have specific requirements.

There are 3 types of opportunities:
    - BRAINDANCE
    - CYBERWARE
    - WEAPON
"""

from enum import Enum, auto

class OpportunityType(Enum):
    BRAINDANCE = auto()
    CYBERWARE = auto()
    WEAPON = auto()

class Opportunity:
    def __init__(self, name: str, type: OpportunityType, requirement: str, effect: str, cost: int):
        self.name = name
        self.type = type
        self.requirement = requirement
        self.effect = effect
        self.cost = cost # contraband
    
    def seize(self):
        pass

CORPORATE_ELITE_BD = Opportunity(
    name="Corporate Elite BD",
    type=OpportunityType.BRAINDANCE,
    requirement="",
    effect="Gain 1 Street Cred for each BRAINDANCE DEAL you have. Then, you may spend 1 📁 to gain 2 Street Cred.",
    cost=2
)

ORGANITSKAYA_BD = Opportunity(
    name="Organitskaya BD",
    type=OpportunityType.BRAINDANCE,
    requirement="",
    effect="Gain 1 Street Cred for each BRAINDANCE DEAL you have. Then, you may replace an Edgerunner card in the market, putting it at the bottom of the Edgerunner deck.",
    cost=1
)

PREEM_BD = Opportunity(
    name="Preem BD",
    type=OpportunityType.BRAINDANCE,
    requirement="PRESENCE in HEYWOOD.",
    effect="Gain 1 Street Cred for each BRAINDANCE DEAL you have. Then, you may replace an Opportunity card in the market, putting it at the bottom of the Opportunity deck.",
    cost=1
)

REALITY_JUNKIE_REQUEST = Opportunity(
    name="Reality Junkie Request",
    type=OpportunityType.BRAINDANCE,
    requirement="PRESENCE in CITY CENTER or PACIFICA.",
    effect="Gain 1 Street Cred for each BRAINDANCE DEAL you have. Then, you may replace an Opportunity card in the market, putting it at the bottom of the Opportunity deck.",
    cost=1
)

RIPPERDOC_BD = Opportunity(
    name="Ripperdoc BD",
    type=OpportunityType.BRAINDANCE,
    requirement="",
    effect="Gain 1 Street Cred for each BRAINDANCE DEAL you have. Then, gain 1 Street Cred for each District where you control a POI.",
    cost=3
)


