from Payload import Payload
class PayloadAlive(Payload):
    def __init__(self, name, type, maxAllowedSpeed, specialNeeds):
        self.name = name
        self.type = type
        self.maxAllowedSpeed = maxAllowedSpeed
        self.specialNeeds = specialNeeds
        