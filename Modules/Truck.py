from Modules.Abstract.AVehicle import AVehicle
class Truck(AVehicle):
    def __init__(self, brand, model, capacity, fuelEconomy, otherThings):
        super().__init__(brand, model, capacity, fuelEconomy)
        self.otherThings = otherThings
