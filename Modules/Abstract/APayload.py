from abc import ABC, abstractmethod
import uuid

class APayload(ABC):

    def __init__(self, name, maxAllowedSpeed):
        # uuid4 is used because it creates a unique id despite the time of creation
        self.id = uuid.uuid4()
        self.name = name
        self.maxAllowedSpeed = maxAllowedSpeed

    def getName(self):
        return self.name
    
    def getMaxAllowedSpeed(self):
        return self.maxAllowedSpeed