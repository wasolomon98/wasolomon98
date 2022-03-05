class Mech:
    def __init__(self, name, __serial_number='', tier=0):
        self.name = name
        self.__serial_number = __serial_number
        self.tier = tier

    def printSelf(self):
        print([self.name, self.__serial_number, self.tier])

test_mech = Mech('Test Machina')
test_mech.printSelf()
