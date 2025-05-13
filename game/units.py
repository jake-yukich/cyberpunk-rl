"""Gang units."""
from enum import Enum, auto
from gangs import Gang

class UnitType(Enum):
    TECHIE = auto()
    SOLO = auto()
    SPECIALIST = auto()
    NETRUNNER = auto()
    DRONE = auto()

class Unit:
    def __init__(self, type: UnitType, gang: Gang):
        self.type = type
        self.gang = gang
    
    def move(self):
        pass

class Solo(Unit):
    """Solos initiate firefights to remove opposing units."""
    def __init__(self):
        super().__init__(UnitType.SOLO)

class Techie(Unit):
    """Techies build drones, seize opportunities, and hire Edgerunners."""
    def __init__(self):
        super().__init__(UnitType.TECHIE)
    
    def _build_drone(self):
        pass

    def seize_opportunity(self):
        pass

    def hire_edgerunner(self):
        pass

class Drone(Unit):
    """
    Drones are special units associated with Techies...
    TODO
    """
    def __init__(self):
        super().__init__(UnitType.DRONE)

class Netrunner(Unit):
    """Netrunners attempt netruns for corporate secrets 📁 and other effects."""
    def __init__(self):
        super().__init__(UnitType.NETRUNNER)

    def netrun(self):
        pass

class Edgerunner(Unit):
    def __init__(self, name: str, type: UnitType, cost: int, passive: str, trigger: str, effect: str):
        super().__init__(type)
        self.name = name
        self.cost = cost # in eurodollars
        self.gang = None
        self.district = None

        self.passive = passive
        self.trigger = trigger
        self.effect = effect

    def hire(self):
        pass

JUDY_ALVAREZ = Edgerunner(
    name="Judy Alvarez",
    type=UnitType.TECHIE,
    cost=1,
    passive="Place a Drone when put in play.",
    trigger="Use the Techie Action disc.",
    effect="You may replace an Opportunity card from the market, placing it at the bottom of the Opportunity deck."
)

VIKTOR_VEKTOR = Edgerunner(
    name="Viktor Vektor",
    type=UnitType.TECHIE,
    cost=1,
    passive="Place a Drone when put in play.",
    trigger="Use the Combat Upgrade Action disc.",
    effect="Look at 1 extra card."
)

JACKIE_WELLES = Edgerunner(
    name="Jackie Welles",
    type=UnitType.SOLO,
    cost=1,
    passive="",
    trigger="Involved in a firefight you initiated.",
    effect="Add 1 🔫 during the COMPARE step."
)

RIVER_WARD = Edgerunner(
    name="River Ward",
    type=UnitType.SOLO,
    cost=1,
    passive="",
    trigger="Involved in a firefight with at least 1 other friendly Solo.",
    effect="Add 1 🔫 during the COMPARE step."
)

GORO_TAKEMURA = Edgerunner(
    name="Goro Takemura",
    type=UnitType.SOLO,
    cost=2,
    passive="",
    trigger="Move into a District with an opposing unit.",
    effect="You may look at the hand of an Opponent in Goro's District. Then, you may discard 1 card from their hand."
)

JOHNNY_SILVERHAND = Edgerunner(
    name="Johnny Silverhand",
    type=UnitType.SOLO,
    cost=2,
    passive="When hired, replace 1 friendly Basic unit in play with Johnny Silverhand. Remove the replaced unit from the game.",
    trigger="at the start of your ACTIVATE.",
    effect="Gain 1 Street Cred.",
)

T_BUG = Edgerunner(
    name="T-Bug",
    type=UnitType.NETRUNNER,
    cost=2,
    passive="",
    trigger="At the start of a Netrun.",
    effect="If any Opponent has more Street Cred than you, gain 1 Street Cred.",
)

NIX = Edgerunner(
    name="Nix",
    type=UnitType.NETRUNNER,
    cost=2,
    passive="",
    trigger="Stop on a RED step at the end of a Netrun.",
    effect="Gain 1 📁.",
)

KERRY_EURODYNE = Edgerunner(
    name="Kerry Eurodyne",
    type=UnitType.SPECIALIST,
    cost=2,
    passive="Kerry may move each time you gain Street Cred during an ACTIVATE.",
    trigger="At the end of your RECLAIM.",
    effect="If Kerry is the only friendly unit in his District, gain 2 Street Cred.",
)

ROGUE_AMENDIARES = Edgerunner(
    name="Rogue Amendiares",
    type=UnitType.SPECIALIST,
    cost=2,
    passive="Once per turn, Rogue may move when another friendly unit enters a Fixer POI.",
    trigger="At the end of your RECLAIM.",
    effect="If you control at least 1 Fixer POI, gain 2 Street Cred.",
)
