class Pilot:
    def __init__(self, name, attributes={}, skills=[], inventory=[]):
        self.name = name
        self.rank = "Cadet"
        self.attributes = attributes
        self.skills = skills
        self.inventory = inventory

    def printSelf(self):
        print([self.name, self.rank, self.attributes, self.skills, self.inventory])

    def setName(self, name):
        self.name = name
