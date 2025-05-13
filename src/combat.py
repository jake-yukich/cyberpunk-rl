"""Combat cards. Combat cards are used during firefights. They always have a firepower and a street cred condition."""
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

L_69_ZHUO = CombatUpgrade(
    name="L-69 Zhuo",
    type=None,
    firepower=3,
    modifier="COMPARE: You may sacrifice 1 friendly Drone in the District to gain an extra 1 firepower.",
    street_cred_condition="2 Street Cred if an Opponent lost any non-Drone units.",
)

LYNX_PAWS = CombatUpgrade(
    name="Lynx Paws",
    type=None,
    firepower=0,
    modifier="REVEAL: You may take back all your used Combat cards. OR: Play another Combat card, adding the firepower, modifier, and Street Cred Condition to this card.",
    street_cred_condition="2 Street Cred if you have no units left in the District.",
)

M2067_DEFENDER = CombatUpgrade(
    name="M2067 Defender",
    type=None,
    firepower=5,
    modifier="",
    street_cred_condition="1 Street Cred if an Opponent lost any units.",
)

MANTIS_BLADES = CombatUpgrade(
    name="Mantis Blades",
    type=None,
    firepower=3,
    modifier="CASUALTIES: Whoever doesn't have the single highest firepower loses 1 extra unit in the District.",
    street_cred_condition="3 Street Cred if there are no opposing units left in the District.",
)

MECH_LOOTER = CombatUpgrade(
    name="Mech Looter",
    type=None,
    firepower=2,
    modifier="REVEAL: Every Opponent loses 1 Drone in the District.",
    street_cred_condition="2 Street Cred for every opposing Drone lost in this Firefight.",
)

MONOWIRE = CombatUpgrade(
    name="Monowire",
    type=None,
    firepower=3,
    modifier="CASUALTIES: Whoever doesn't have the single highest firepower loses 1 extra unit in the District.",
    street_cred_condition="2 Street Cred if you didn't lose anyunits.",
)

PAIN_EDITOR = CombatUpgrade(
    name="Pain Editor",
    type=None,
    firepower=3,
    modifier="CASUALTIES: Your opponents lose a unit, even in a tie.",
    street_cred_condition="2 Street Cred if an Opponent lost any units.",
)

PING = CombatUpgrade(
    name="Ping",
    type=None,
    firepower=1,
    modifier="REVEAL: If there is a friendly Drone in the District, you may play another Combat card. Add the firepower, modifier, and Street Cred Condition to this card.",
    street_cred_condition="1 Street Cred if an Opponent lost any units.",
)

RECON_GRENADE = CombatUpgrade(
    name="Recon Grenade",
    type=None,
    firepower=1,
    modifier="REVEAL: If there is a friendly Techie in the District, you may play another Combat card. Add the firepower, modifier, and Street Cred Condition to this card.",
    street_cred_condition="1 Street Cred if you have a Techie left in the District.",
)

SECOND_HEART = CombatUpgrade(
    name="Second Heart",
    type=None,
    firepower=1,
    modifier="CASUALTIES: You cannot lose units in this Firefight.",
    street_cred_condition="2 Street Cred if an Opponent had 4 firepower or more during COMPARE.",
)

SHOCK_N_AWE = CombatUpgrade(
    name="Shock-N-Awe",
    type=None,
    firepower=2,
    modifier="REVEAL: All Opponents lose all of their Drones in the District.",
    street_cred_condition="1 Street Cred for each opposing Drone lost.",
)

SPIDERBOT_SPLINTER = CombatUpgrade(
    name="Spiderbot Splinter",
    type=None,
    firepower=-1,
    modifier="COMPARE: The firepower of this card is equal to the number of all Drones in the District.",
    street_cred_condition="3 Street Cred if an Opponent lost any Drones.",
)

STEPHENSON_TECH_MK_4 = CombatUpgrade(
    name="Stephenson Tech MK-4",
    type=None,
    firepower=1,
    modifier="REVEAL: Gain 1 📁 for each Netrunner in the District.",
    street_cred_condition="1 Street Cred for each 📁 gained in this Firefight.",
)

SYNAPTIC_ACCELERATOR = CombatUpgrade(
    name="Synaptic Accelerator",
    type=None,
    firepower=1,
    modifier="CASUALTIES: You may move 1 surviving unit to an adjacent District.",
    street_cred_condition="2 Street Cred if you do not have Dominance in the District.",
)

TKI_20_SHINGEN = CombatUpgrade(
    name="TKI-20 Shingen",
    type=None,
    firepower=3,
    modifier="CASUALTIES: If you have the single highest firepower, you decide which opposing units to kill.",
    street_cred_condition="2 Street Cred for each opposing Solo lost.",
)

TSUNAMI_ASHURA = CombatUpgrade(
    name="Tsunami Ashura",
    type=None,
    firepower=4,
    modifier="CASUALTIES: If you have the single highest firepower, you decide which opposing units to kill.",
    street_cred_condition="1 Street Cred if you did not lose any units.",
)

TSUNAMI_NEKOMATA = CombatUpgrade(
    name="Tsunami Nekomata",
    type=None,
    firepower=-1,
    modifier="COMPARE: The firepower of this card is equal to the firepower of 1 other card in this Firefight.",
    street_cred_condition="1 Street Cred for each opposing unit lost.",
)

ZETATECH_BERSERK = CombatUpgrade(
    name="Zetatech Berserk",
    type=None,
    firepower=6,
    modifier="CASUALTIES: Sacrifice 1 friendly unit in the District.",
    street_cred_condition="1 Street Cred for each opposing Solo lost.",
)

# PROTOTYPES
# ------------------------------------------------------------

SMART_WEAPON = CombatUpgrade(
    name="Smart Weapon",
    type=WeaponType.PROTOTYPE,
    firepower=2,
    modifier="CASUALTIES: Kill any 1 unit in this District.",
    street_cred_condition="2 Street Cred if there are no opposing units left in the District.",
)
