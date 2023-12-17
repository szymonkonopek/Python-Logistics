from Payload import Payload

class PayloadDangerous(Payload):
    def __init__(self, name, type, maxAllowedSpeed, levelOfDanger):
        super().__init__(name, type, maxAllowedSpeed)
        self.levelOfDanger = levelOfDanger