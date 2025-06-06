class District:
    def __init__(self, name: str):
        self.name = name
        self.pois = []
        self.rewards = []
        self.presence = []
        self.dominance = None
        self.units = []  # List of all units in this district

        self._pois()
    
    def can_enter_poi(self, unit, poi):
        """Check if unit can enter a POI."""
        from units import UnitType
        # Drones and hideouts cannot enter POIs
        if unit.type in [UnitType.DRONE, UnitType.HIDEOUT]:
            return False
        # POI must not be occupied
        return not poi.is_occupied
    
    def enter_poi(self, unit, poi):
        """Move unit into a POI."""
        if self.can_enter_poi(unit, poi):
            poi.is_occupied = True
            poi.occupant = unit
            print(f"{unit.gang.name} {unit.type.name} entered {poi.name} POI in {self.name}")
            return True
        return False
    
    def exit_poi(self, unit):
        """Remove unit from any POI they're occupying."""
        for poi in self.pois:
            if poi.occupant == unit:
                poi.is_occupied = False
                poi.occupant = None
                print(f"{unit.gang.name} {unit.type.name} exited {poi.name} POI in {self.name}")
                return True
        return False

    def _pois(self):
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