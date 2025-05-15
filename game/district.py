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