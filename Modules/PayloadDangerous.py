from Payload import Payload
class PayloadDangerous(Payload):
    def __init__(self, name, type, maxAllowedSpeed, levelOfDanger):
        self.name = name
        self.type = type
        self.maxAllowedSpeed = maxAllowedSpeed
        self.levelOfDanger = levelOfDanger
        