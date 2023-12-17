from abc import ABC, abstractmethod
import uuid

class APayload(ABC):

    def __init__(self, name, type, maxAllowedSpeed):
        # uuid4 is used because it creates a unique id despite the time of creation
        self.id = uuid.uuid4()
        self.name = name
        self.type = type
        self.maxAllowedSpeed = maxAllowedSpeed