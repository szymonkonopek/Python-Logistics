from Abstract.APayload import APayload

class PayloadDangerous(APayload):
    def __init__(self, name, type, maxAllowedSpeed, levelOfDanger):
        super().__init__(name, type, maxAllowedSpeed)
        self.levelOfDanger = levelOfDanger