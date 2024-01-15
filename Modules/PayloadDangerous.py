from Modules.Abstract.APayload import APayload

# An implementation of dangerous payload.
# Price depends on the level of danger which is in the the range from 1 to 3.
class PayloadDangerous(APayload):
    def __init__(self, name, maxAllowedSpeed, levelOfDanger):
        super().__init__(name, maxAllowedSpeed)
        self.type = __class__.__name__
        if (levelOfDanger > 0 and levelOfDanger <= 9):
            self.levelOfDanger = levelOfDanger