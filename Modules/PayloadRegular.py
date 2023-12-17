from Modules.Payload import Payload

class PayloadRegular(Payload):
    def __init__(self, name, type, maxAllowedSpeed, weight):
        super().__init__(name, type, maxAllowedSpeed)
        self.weight = weight