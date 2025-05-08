"""
Opportunities are underground deals that Gangs can fulfill.
They cost Contraband 📦 to be seized and often have specific requirements.

There are 3 main types of opportunities:
    - BRAINDANCE
    - CYBERWARE
    - WEAPON
"""
from enum import Enum, auto

class OpportunityType(Enum):
    BRAINDANCE = auto()
    CYBERWARE = auto()
    WEAPON = auto()
    SPECIAL = auto()

class Opportunity:
    def __init__(self, name: str, type: OpportunityType, requirement: str, effect: str, cost: int):
        self.name = name
        self.type = type
        self.requirement = requirement
        self.effect = effect
        self.cost = cost # contraband
    
    def _check_requirement(self):
        pass

    def _apply_effect(self):
        pass
    
    def seize(self):
        pass

# BRAINDANCE
# ------------------------------------------------------------
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

SPIKED_BD = Opportunity(
    name="Spiked BD",
    type=OpportunityType.BRAINDANCE,
    requirement="PRESENCE in: At least 2 DISTRICTS.",
    effect="Gain 1 Street Cred for each BRAINDANCE DEAL you have. Then, you may steal 1 resource from every Opponent with more Street Cred than you.",
    cost=3
)

SYNTHCOKE_DEAL = Opportunity(
    name="Synthcoke Deal",
    type=OpportunityType.BRAINDANCE,
    requirement="",
    effect="Gain 1 Street Cred for each BRAINDANCE DEAL you have. Then, you may move up to 3 friendly units.",
    cost=2
)

UPSCALE_VRCADE = Opportunity(
    name="Upscale VRcade",
    type=OpportunityType.BRAINDANCE,
    requirement="PRESENCE in: CITY CENTER or WESTBROOK.",
    effect="Gain 1 Street Cred for each BRAINDANCE DEAL you have. Then, you may replace an Opportunity card in the market, putting it at the bottom of the Opportunity deck.",
    cost=1
)

XBD_DEALER = Opportunity(
    name="XBD Dealer",
    type=OpportunityType.BRAINDANCE,
    requirement="PRESENCE in: WATSON or SANTO DOMINGO.",
    effect="Gain 1 Street Cred for each BRAINDANCE DEAL you have. Then, you may replace an Opportunity card in the market, putting it at the bottom of the Opportunity deck.",
    cost=1
)

# CYBERWARE
# ------------------------------------------------------------
BACK_ALLEY_RIPPERDOC = Opportunity(
    name="Back Alley Ripperdoc",
    type=OpportunityType.CYBERWARE,
    requirement="",
    effect="Gain 1 Street Cred for each CYBERWARE DEAL you have. Then, gain 1 Eurodollar.",
    cost=1
)

BODYSHOPPE_CYBERTUNING = Opportunity(
    name="Body Shoppe Cybertuning",
    type=OpportunityType.CYBERWARE,
    requirement="",
    effect="Gain 1 Street Cred for each CYBERWARE DEAL you have. Then, you may perform a free Upgrade, drawing 1 extra Combat Upgrade card.",
    cost=3
)

CHIPPIN_IN = Opportunity(
    name="Chippin' In",
    type=OpportunityType.CYBERWARE,
    requirement="PRESENCE in: CITY CENTER.",
    effect="Gain 1 Street Cred for each CYBERWARE DEAL you have. Then, you may move any friendly unit directly into City Center.",
    cost=1
)

CORP_WARE_AUGMENTATIONS = Opportunity(
    name="Corp Ware Augmentations",
    type=OpportunityType.CYBERWARE,
    requirement="CONTROL any: DATA FORTRESS POI.",
    effect="Gain 1 Street Cred for each CYBERWARE DEAL you have. Then, you may kill any unit.",
    cost=2
)

CYBERED_UP = Opportunity(
    name="Cybered Up",
    type=OpportunityType.CYBERWARE,
    requirement="",
    effect="Gain 1 Street Cred for each CYBERWARE DEAL you have. Then, gain 1 Street Cred for every 2 Hideouts you have in play, rounded down.",
    cost=1
)

CYBERFASHION_UPGRADES = Opportunity(
    name="Cyberfashion Upgrades",
    type=OpportunityType.CYBERWARE,
    requirement="CONTROL any: DATA FORTRESS POI.",
    effect="Gain 1 Street Cred for each CYBERWARE DEAL you have. Then, you may spend 2 📁 to gain 3 Street Cred.",
    cost=1
)

NIGHT_MARKET_TUNE_UP = Opportunity(
    name="Night Market Tune Up",
    type=OpportunityType.CYBERWARE,
    requirement="PRESENCE in: at least 2 DISTRICTS.",
    effect="Gain 1 Street Cred for each CYBERWARE DEAL you have. Then, you may swap a Combat card from your hand with a random Combat card from an Opponent's hand.",
    cost=3
)

PREEM_CYBERWARE = Opportunity(
    name="Preem Cyberware",
    type=OpportunityType.CYBERWARE,
    requirement="",
    effect="Gain 1 Street Cred for each CYBERWARE DEAL you have. Then, you may move up to 2 friendly units.",
    cost=1
)

RONIN_UPGRADES = Opportunity(
    name="Ronin Upgrades",
    type=OpportunityType.CYBERWARE,
    requirement="",
    effect="Gain 1 Street Cred for each CYBERWARE DEAL you have. Then, gain 1 Street Cred for every Opponent with more Street Cred than you.",
    cost=2
)

# WEAPON
# ------------------------------------------------------------
ARMING_THE_CITY = Opportunity(
    name="Arming the City",
    type=OpportunityType.WEAPON,
    requirement="",
    effect="Gain 1 Street Cred for each WEAPON DEAL you have. Then, gain either 2 📦, 2 Eurodollars, or 2 Street Cred.",
    cost=3
)

BOOTLEG_ARASAKA_TECH = Opportunity(
    name="Bootleg Arasaka Tech",
    type=OpportunityType.WEAPON,
    requirement="DOMINANCE in: WATSON.",
    effect="Gain 1 Street Cred for each WEAPON DEAL you have. Then, gain either 1 📦 or 1 Eurodollar.",
    cost=1
)

BUDGET_ARMS_DISPOSABLES = Opportunity(
    name="Budget Arms Disposables",
    type=OpportunityType.WEAPON,
    requirement="DOMINANCE in: HEYWOOD.",
    effect="Gain 1 Street Cred for each WEAPON DEAL you have. Then, gain 1 Eurodollar.",
    cost=1
)

CORP_PROTOTYPES = Opportunity(
    name="Corp Prototypes",
    type=OpportunityType.WEAPON,
    requirement="DOMINANCE in: CITY CENTER.",
    effect="Gain 1 Street Cred for each WEAPON DEAL you have. Then, gain either 1 📦, 1 Eurodollar, or 1 Street Cred.",
    cost=1
)

IRON_TO_THE_MASSES = Opportunity(
    name="Iron to the Masses",
    type=OpportunityType.WEAPON,
    requirement="",
    effect="Gain 1 Street Cred for each WEAPON DEAL you have. Then, gain either 1 📦, 1 Eurodollar, or 1 Street Cred.",
    cost=2
)

MILITECH_SMART_GUNS = Opportunity(
    name="Militech Smart Guns",
    type=OpportunityType.WEAPON,
    requirement="DOMINANCE in: WESTBROOK.",
    effect="Gain 1 Street Cred for each WEAPON DEAL you have. Then, gain 1 Eurodollar or 1 Street Cred.",
    cost=1
)

NOKOTA_WEAPONS_SHIPMENT = Opportunity(
    name="Nokota Weapons Shipment",
    type=OpportunityType.WEAPON,
    requirement="DOMINANCE in: PACIFICA.",
    effect="Gain 1 Street Cred for each WEAPON DEAL you have. Then, gain either 1 📦 or 1 Street Cred.",
    cost=1
)

SMUGGLING_OPERATION = Opportunity(
    name="Smuggling Operation",
    type=OpportunityType.WEAPON,
    requirement="DOMINANCE in: SANTO DOMINGO.",
    effect="Gain 1 Street Cred for each WEAPON DEAL you have. Then, gain 1 📦.",
    cost=1
)

UNPREDICTABLE_SMART_GUN = Opportunity(
    name="Unpredictable Smart Gun",
    type=OpportunityType.WEAPON,
    requirement="PRESENCE in: At least 2 DISTRICTS.",
    effect="Gain 1 Street Cred for each WEAPON DEAL you have. Then, you may hire an Edgerunner without paying their cost.",
    cost=3
)

# SPECIAL
# ------------------------------------------------------------
ARASAKA_BLUEPRINTS = Opportunity(
    name="Arasaka Blueprints",
    type=OpportunityType.SPECIAL,
    requirement="This opportunity can't be put at the bottom of the opportunity deck or discarded.",
    effect="Gain 3 Street Cred, 2 Eurodollars, and you may perform a free Upgrade.",
    cost=4
)

