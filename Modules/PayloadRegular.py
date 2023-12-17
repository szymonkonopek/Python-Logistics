from Abstract.APayload import APayload

class PayloadRegular(APayload):
    def __init__(self, name, type, maxAllowedSpeed, weight):
        super().__init__(name, type, maxAllowedSpeed)
        self.weight = weight