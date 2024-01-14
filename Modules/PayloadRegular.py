from Modules.Abstract.APayload import APayload

# An implementation of regular payload. Price depends on the weight.
class PayloadRegular(APayload):
    def __init__(self, name, maxAllowedSpeed, weight):
        super().__init__(name, maxAllowedSpeed)
        self.type = __class__.__name__
        self.weight = weight