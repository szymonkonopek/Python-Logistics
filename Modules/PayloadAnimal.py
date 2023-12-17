from Abstract.APayload import APayload

class PayloadAnimal(APayload):
    def __init__(self, name, maxAllowedSpeed, specialNeeds):
        super().__init__(name, maxAllowedSpeed)
        self.type = __class__.__name__
        self.specialNeeds = specialNeeds