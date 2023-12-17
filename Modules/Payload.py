import uuid

class Payload:
    def __init__(self, name, type, maxAllowedSpeed):
        self.id = uuid.uuid1()
        self.name = name
        self.type = type
        self.maxAllowedSpeed = maxAllowedSpeed