class Feeder:

    def __init__(self, level):
        self.water_level = level

    def dispense(self):

        if self.water_level >= 5:
            self.water_level -= 5
            print("Dispensing water...")
        else:
            print("Water tank is empty")
