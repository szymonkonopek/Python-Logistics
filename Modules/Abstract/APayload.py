from abc import ABC, abstractmethod
import uuid

# An abstract Payload class to implement different types of Payload
class APayload(ABC):

    def __init__(self, name, maxAllowedSpeed):
        # uuid4 is used because it creates an unique id despite the time of creation
        self.id = uuid.uuid4()
        self.name = name
        self.maxAllowedSpeed = maxAllowedSpeed

    def getName(self):
        return self.name
    
    def getMaxAllowedSpeed(self):
        return self.maxAllowedSpeed