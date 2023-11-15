from Abstract.AVehicle import AVehicle
class DeliveryTruck(AVehicle):
    def __init__(self, brand, model, capacity, fuelEconomy, someThings):
        super().__init__(brand, model, capacity, fuelEconomy)
        self.someThings = someThings
