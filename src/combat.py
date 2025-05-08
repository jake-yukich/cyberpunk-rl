"""
"""
from enum import Enum, auto

class CombatUpgrade:
    def __init__(self, name: str, type: str, firepower: int, modifier: str = None, street_cred_condition: str = None, cost: int = 1):
        self.name = name
        self.type = type
        self.cost = cost
        self.modifier = modifier
        self.street_cred_condition = street_cred_condition
        self.firepower = firepower

    def upgrade(self):
        pass

class WeaponType(Enum):
    STARTING = auto()
    PROTOTYPE = auto()

# STARTERS
# ------------------------------------------------------------

CRUSHER = CombatUpgrade(
    name="Crusher",
    type=WeaponType.STARTING,
    firepower=3,
    street_cred_condition="1 Street Cred if you didn't lose any units.",
)

CYBERPSYCHOSIS = CombatUpgrade(
    name="Cyberpsychosis",
    type=WeaponType.STARTING,
    firepower=1,
    street_cred_condition="1 Street Cred if you have no units left in the District.",
)

SHORT_CIRCUIT = CombatUpgrade(
    name="Short Circuit",
    type=WeaponType.STARTING,
    firepower=2,
    street_cred_condition="1 Street Cred if an Opponent lost any Drones.",
)

SUBDERMAL_ARMOR = CombatUpgrade(
    name="Subdermal Armor",
    type=WeaponType.STARTING,
    firepower=2,
    street_cred_condition="1 Street Cred if an Opponent lost any non-Drone units.",
)

# (REGULAR)
# ------------------------------------------------------------

ARASAKA_MK_4 = CombatUpgrade(
    name="Arasaka MK-4",
    type=None,
    firepower=1,
    modifier="REVEAL: If there is a friendly Netrunner in the District, you may play another Combat card. Add the firepower, modifier, and Street Cred Condition to this card.",
    street_cred_condition="You may spend up to 4 📁 to gain that many Street Cred.",
)

CYBERWARE_MALFUNCTION = CombatUpgrade(
    name="Cyberware Malfunction",
    type=None,
    firepower=2,
    modifier="REVEAL: Every other Combat Card Modifier (including Reveals) is treated as blank in this Firefight.",
    street_cred_condition="3 Street Cred if an Opponent lost any units.",
)

EMP_GRENADE = CombatUpgrade(
    name="EMP Grenade",
    type=None,
    firepower=2,
    modifier="CASUALTIES: You may sacrifice 1 friendly Drone in the District to kill any unit in it.",
    street_cred_condition="2 Street Cred if an Opponent lost any Techies.",
)

KIROSHI_OPTICS = CombatUpgrade(
    name="Kiroshi Optics",
    type=None,
    firepower=4,
    modifier="CASUALTIES: If you have the single highest firepower, you decide which opposing units to kill.",
    street_cred_condition="3 Street Cred if an Opponent lost any Edgerunners.",
)

# TODO: add the rest of the regular upgrades



# PROTOTYPES
# ------------------------------------------------------------

SMART_WEAPON = CombatUpgrade(
    name="Smart Weapon",
    type=WeaponType.PROTOTYPE,
    firepower=2,
    modifier="CASUALTIES: Kill any 1 unit in this District.",
    street_cred_condition="2 Street Cred if there are no opposing units left in the District.",
)
