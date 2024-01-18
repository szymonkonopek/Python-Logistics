from abc import ABC, abstractmethod
import uuid

# Vehicle abstract class as a base class
class AVehicle(ABC):

    def __init__(self, brand, model, capacity, fuelEconomy):
        self.id = uuid.uuid4()
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.fuelEconomy = fuelEconomy

    def getModel(self):
        return self.model