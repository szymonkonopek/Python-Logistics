from abc import ABC, abstractmethod
import uuid

class AVehicle(ABC):

    def __init__(self, brand, model, capacity, fuelEconomy):
        self.id = uuid.uuid4()
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.fuelEconomy = fuelEconomy
    # @property
    # @abstractmethod
    # def brand(self):
    #     return self._brand
    # def model(self):
    #     return self._model
    # def capacity(self):
    #     return self._capacity
    # def fuelEconomy(self):
    #     return self._fuelEconomy
   