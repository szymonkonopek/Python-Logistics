from Abstract.APayload import APayload

class PayloadAnimal(APayload):
    def __init__(self, name, type, maxAllowedSpeed, specialNeeds):
        super().__init__(name, type, maxAllowedSpeed)
        self.specialNeeds = specialNeeds