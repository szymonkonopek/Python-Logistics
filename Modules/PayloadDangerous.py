from Modules.Abstract.APayload import APayload

class PayloadDangerous(APayload):
    def __init__(self, name, maxAllowedSpeed, levelOfDanger):
        super().__init__(name, maxAllowedSpeed)
        self.type = __class__.__name__
        self.levelOfDanger = levelOfDanger